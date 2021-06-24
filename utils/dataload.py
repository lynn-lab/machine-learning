import os
import numpy as np
from numpy.core.defchararray import index
class Data:
    
    def data_sites(filename):
        fr = open(filename)
        arrayOnlines = fr.readlines()
        numberoflines = len(arrayOnlines)
        Mat = np.zeros((numberoflines,3))
        classLabelVector = []
        index = 0
        for line in arrayOnlines:
            line = line.strip()
            listFromLine = line.split('\t')
            Mat[index,:] = listFromLine[0:3]
            classLabelVector.append(int(listFromLine[-1]))
            index += 1
        return Mat, classLabelVector