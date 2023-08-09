import pandas as pd

import tensorflow as tensorflow
from tensorflow.keras.processing.text import Tokenizer

from tensorflow.keras.processing.sequence import pad_sequences

train_data_raw = pd.read_excel("./Emoções.xlsx")

train_data = train_data_raw["Text_Emotion"].str.split(";",n=1, expand=True)
train_data.columns = ['Texto', 'Emoção']

encode_emotions = {"raiva":0,"medo":1,"alegria":2,"amor":3, "tristeza":4,"surpresa":5}
train_data['Emoção'] = train_data['Emoção'].map(encode_emotions)

