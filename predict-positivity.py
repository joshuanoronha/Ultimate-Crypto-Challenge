# from sklearn.naive_bayes import GaussianNB
# training_data = [["Bitcoin Set to Challenge Downtrend in Next Couple of Days"],["Says Fundstrat Advisor,Which Way? Bitcoin's Low Volatility May Force Big Move"],["Regulatory Concerns Dampen Bitcoin Volatility"],["Warren Buffett and Jamie Dimon on Bitcoin: Just Beware"],["Bitcoin to hit $14000","Bitcoin to hit $1000"]]
# training_label = ["negative","negative","negative","negative","negative","positive","negative"]
# testing_data = ["Bitcoin price crashes"]
# nb = GaussianNB()
# nb.fit(training_data,training_label)
# prediction = nb.predict(testing_data)
# accuracy = accuracy_score(y_true, y_pred)
# print accuracy

import tflearn
import tensorflow as tf
import tensorflow.contrib as tc
from tflearn.data_utils import to_categorical,pad_sequences
from tflearn.datasets import imdb
# import csv
# with open('data/data-altcoin.csv', 'r') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',')
#     for row in spamreader:
#         print(row)
train, test , _ = imdb.load_data(path='imdb.pkl',n_words=10000,valid_portion=0.1)
# print (_)

# print(train)

trainX, trainY = train
testX, testY = test

trainX = pad_sequences(trainX, maxlen=100, value=0.)
testX = pad_sequences(testX, maxlen=100, value=0.)

print (trainY)

trainY = to_categorical(trainY, nb_classes=2)
testY = to_categorical(testY, nb_classes=2)
print("\n\n" + "="*100)
print (trainY)
print(trainY[5])
print(trainY[6])
print (len(trainY))

import sys
sys.exit(0)
# load a csv
CSV_PATH = 'data/data-altcoin.csv'
dataset = tc.data.make_csv_dataset(CSV_PATH, batch_size=32)
# print (dataset)
print (dir(dataset))
iter = dataset.make_one_shot_iterator()
next = iter.get_next()
# print(next) # next is a dict with key=columns names and value=column data
inputs, labels = next['title'], next['class']
# with  tf.Session() as sess:
#     print(sess.run([inputs,labels]))

n = 8
m = int(n/2)
trainX, trainY = inputs[:m],labels[:m]
testX, testY = inputs[m+1:],labels[m+1:] 
print (labels)
#Data preprocessing
#Sequence Padding
trainX = pad_sequences(trainX,maxlen=100,value=0)
testX = pad_sequences(testX,maxlen=100,value=0)

#Converting labels to binary vectors
trainY = to_categorical(trainY,nb_classes=2)
testY = to_categorical(testY,nb_classes=2)

# Network Building
net = tflearn.input_data([None,100])
net = tflearn.embedding(net,input_dim=10000,output_dim=128)
net = tflearn.lstm(net,128,dropout=0.8)
net = tflearn.fully_connected(net,2,activation="softmax")
net = tflearn.regression(net, optimizer='adam',learning_rate=0.0001,loss='categorical_crossentropy')

#Training
model = tflearn.DNN(net,tensorboard_verbose=0)
model.fit(trainX,trainY,validation_set=(testX,testY),show_metric=True,batch_size=32)
