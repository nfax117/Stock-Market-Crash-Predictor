from keras.models import model_from_json
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.preprocessing import sequence
from keras import backend as K


def run(text_input):
    SNP = pd.read_csv('./SP500.csv')

    # get all attributes
    SNP_attributes = SNP.iloc[:,2:7]
    # get last column (y)
    SNP_price = SNP.iloc[:,-1:]

    # normalize the data using MinMax scaller
    scaler = MinMaxScaler()
    scaler.fit(SNP_attributes)
    SNP_attributes = scaler.transform(SNP_attributes)

    K.clear_session()
    f = open("model_architecture.json", 'r+')
    json_string = f.read()
    f.close()
    model = model_from_json(json_string)

    model.load_weights('model_weights.h5')
    model.compile(optimizer='adam', loss='mean_squared_error')
    # 1 set of data x 14 days x 6 pieces of data each day
    # Use past 14 days topredict today's closing price
    # [ [[P/E Ratio,Open,Low,High,Volume,Closing Price]], ... 13 more times]
    # using line 694 of SP500 csv
    info = np.array([[[22.44, 2937.09, 2913.32, 2940.43, 3008450000, 2906.27]], [22.04, 2983.69, 2938.7, 2992.53, 3558040000, 2940.25], [22.62, 3050.72, 3050.72, 3066.95, 3930200000, 3066.91], [22.78, 3147.18, 3139.34, 3150.3, 1743020000, 3113.87], [24.88, 3215.18, 3212.03, 3231.72, 2893810000, 3257.85], [26.42, 3282.33, 3214.68, 3282.33, 4527830000, 3248.92], [22.8, 2916.9, 2855.84, 2959.72, 8563850000, 3090.23], [
                    24.97, 2498.08, 2447.49, 2522.75, 5947900000, 2470.5], [27.82, 2869.09, 2821.61, 2869.09, 4753160000, 2830.71], [31.29, 3038.78, 3031.54, 3062.18, 4673410000, 3055.73], [32.44, 3105.92, 3101.17, 3128.44, 4443130000, 3115.86], [34.41, 3270.45, 3220.26, 3272.17, 5117260000, 3294.61], [34.27, 3507.44, 3494.6, 3528.03, 4083110000, 3526.65], [35.3, 3385.87, 3361.39, 3397.18, 4070530000, 3380.8]])
    #returns a probabilistic output, 
    prediction = model.predict(info)
    prediction = np.repeat(prediction,info.shape[2], axis=-1)
    prediction = scaler.inverse_transform(prediction)[:,0]
    return prediction

    # need 14 data points as 1 time step
    # 1 x 14 x 6

    K.clear_session()
