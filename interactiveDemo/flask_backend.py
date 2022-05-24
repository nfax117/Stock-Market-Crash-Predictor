from keras.models import model_from_json
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.preprocessing import sequence
from keras import backend as K


def run(list_of_days_info):
    SNP = pd.read_csv('../SPX_500_Data.csv')
    SNP = SNP.drop(['Adj Close', 'Date','% Gain/Loss (Close)','% Price Variation'], axis=1)
    # get all attributes
    SNP_attributes = SNP.iloc[:,:]

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
    
    info = np.array([list_of_days_info])
    #returns a probabilistic output, 
    prediction = model.predict(info)
    prediction = np.repeat(prediction,info.shape[2], axis=-1)
    prediction = scaler.inverse_transform(prediction)[:,0]
    return prediction

    K.clear_session()
