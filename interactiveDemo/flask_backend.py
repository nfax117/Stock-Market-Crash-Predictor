from keras.models import model_from_json
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.preprocessing import sequence
from keras import backend as K


def runMul(day_info):
    SNP = pd.read_csv('../SPX_500_Data.csv')
    SNP = SNP.drop(['Adj Close', 'Date','% Gain/Loss (Close)','% Price Variation'], axis=1)
    # get all attributes
    SNP_attributes = SNP.iloc[:,:]

    # normalize the data using MinMax scaller
    scaler = MinMaxScaler()
    scaler.fit(SNP_attributes)
    SNP_attributes = scaler.transform(SNP_attributes)

    K.clear_session()
    f = open("model_architecture_mulBIG.json", 'r+')
    json_string = f.read()
    f.close()
    model = model_from_json(json_string)

    model.load_weights('model_weights_mulBIG.h5')
    model.compile(optimizer='adam', loss='mean_squared_error')
    if day_info != None:
        day_info =  np.array(day_info)
        day_info = np.reshape(day_info, (5, 1))
        info = []
        info.append([SNP_attributes[-44:,0:5]])
        info = np.array(info)
        info = np.reshape(info, (1,44,5))
        info = np.append(info, day_info)
    else:
        info = []
        info.append([SNP_attributes[-45:,0:5]])
        info = np.array(info)
    info = np.reshape(info, (1,45,5))
    # print(info.shape())

    #returns a probabilistic output, 
    prediction = model.predict(info)
    prediction = np.repeat(prediction,info.shape[2], axis=-1)
    prediction = scaler.inverse_transform(prediction)[:,0]
    return prediction

    K.clear_session()
def runUni(day_info):
    SNP = pd.read_csv('../SPX_500_Data.csv')
    SNP = SNP.drop(['Adj Close', 'Date','% Gain/Loss (Close)','% Price Variation'], axis=1)
    # get all attributes
    SNP_price = SNP['Close']
    SNP_price = np.array(SNP_price)
    SNP_price = np.reshape(SNP_price, (-1,1))

    Price_scaler = MinMaxScaler()
    Price_scaler.fit(SNP_price)
    SNP_price = Price_scaler.transform(SNP_price)

    K.clear_session()
    f = open("model_architecture_uniBIG.json", 'r+')
    json_string = f.read()
    f.close()
    model = model_from_json(json_string)

    model.load_weights('model_weights_uniBIG.h5')
    model.compile(optimizer='adam', loss='mean_squared_error')
    if day_info != None:
        day_info =  np.array(day_info)
        day_info = np.reshape(day_info, (1, 1))
        info = []
        info.append([SNP_price[-44:,0:1]])
        info = np.array(info)
        info = np.reshape(info, (1,44,1))
        info = np.append(info, day_info)
    else:
        info = []
        info.append([SNP_price[-45:,0:1]])
        info = np.array(info)
    info = np.reshape(info, (1,45,1))

    prediction = model.predict(info)
    prediction = np.repeat(prediction,info.shape[2], axis=-1)
    prediction = Price_scaler.inverse_transform(prediction)[:,0]
    return prediction

    K.clear_session()