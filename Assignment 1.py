import pickle
import numpy as np

def loadData(filename, classnamesFile):
    file = open(filename)
    file2 = open(classnamesFile)
    with open(file, 'rb') as fo:
        dictt = pickle.load(fo, encoding='bytes')
    with open(file2, 'rb') as fo:
        classnames = pickle.load(fo, encoding='bytes')
    onehot = np.zeros(len(dictt), len(classnames))

    for labelNo in range(len(dictt.keys())):
        onehot[labelNo][dictt.keys[labelNo]] = 1
        
    return dictt, onehot
