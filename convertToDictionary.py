import csv
import nltk
import sys
import json
import unicodedata
from nltk.stem.lancaster import LancasterStemmer
import tflearn
import tensorflow as tf
import random
import numpy as np
dictionary = {"0": [], "1": []}
with open('data/data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        description = row[1]
        classification = row[3]
        if classification == "1" or classification == "0":
            print("description", description)
            print("classification", classification)
            if classification == "0":
                dictionary["1"].append(description)
            elif classification == "1":
                dictionary["0"].append(description)
    print(dictionary)

with open('data.json', 'w') as fp:
    json.dump(dictionary, fp)


#Part 2
tbl = dict.fromkeys(i for i in range(sys.maxunicode)
                    if unicodedata.category(chr(i)).startswith('P'))

# method to remove punctuations from sentences.


def remove_punctuation(text):
    return text.translate(tbl)


# initialize the stemmer
stemmer = LancasterStemmer()
# variable to hold the Json data read from the file
data = None

# read the json file and load the training data
with open('data.json') as json_data:
    data = json.load(json_data)
    print(data)

# get a list of all categories to train for
categories = list(data.keys())
words = []
# a list of tuples with words in the sentence and category name
docs = []

for each_category in data.keys():
    for each_sentence in data[each_category]:
        # remove any punctuation from the sentence
        each_sentence = remove_punctuation(each_sentence)
        # print(each_sentence)
        # extract words from each sentence and append to the word list
        w = nltk.word_tokenize(each_sentence)
        # print("tokenized words: ", w)
        words.extend(w)
        docs.append((w, each_category))
# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words]
words = sorted(list(set(words)))

# print(words)
# print(docs)


#Part 3

# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(categories)
 
 
for doc in docs:
    # initialize our bag of words(bow) for each document in the list
    bow = []
    # list of tokenized words for the pattern
    token_words = doc[0]
    # stem each word
    token_words = [stemmer.stem(word.lower()) for word in token_words]
    # create our bag of words array
    for w in words:
        bow.append(1) if w in token_words else bow.append(0)
     
    output_row = list(output_empty)
    output_row[categories.index(doc[1])] = 1
     
    # our training set will contain a the bag of words model and the output row that tells which catefory that bow belongs to.
    training.append([bow, output_row])
 
# shuffle our features and turn into np.array as tensorflow  takes in numpy array
random.shuffle(training)
training = np.array(training)
 
# trainX contains the Bag of words and train_y contains the label/ category
s  =int(len(training) * 0.65)
train_x = list(training[:s,0])
train_y = list(training[:s,1])
testX = list(training[s:,0])
testY =list(training[s:,1])
##Part 4
# reset underlying graph data
tf.reset_default_graph()
# Build neural network
print (len(train_x[0]))
net = tflearn.input_data(shape=[None, len(train_x[0])])
# net = tflearn.embedding(net,input_dim=len(train_x[0]),output_dim=16)
# net = tflearn.lstm(net,16,dropout=0.8)
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)


# net = tflearn.input_data(shape=[None, len(train_x[0])])
# net = tflearn.embedding(net,input_dim=10000,output_dim=32)
# net = tflearn.lstm(net,32,dropout=0.8)
# net = tflearn.fully_connected(net, 8, activation="softmax")
# net = tflearn.fully_connected(net, 2)
# net = tflearn.regression(net, optimizer='adam',learning_rate=0.0001,loss='categorical_crossentropy')
 

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training (apply gradient descent algorithm)

model.fit(train_x, train_y,validation_set=(testX,testY), n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')
#Part 5
