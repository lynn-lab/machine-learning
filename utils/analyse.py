import matplotlib
import matplotlib.pyplot as plt
from numpy.core.records import array
from numpy.lib.shape_base import tile
import numpy as np

class Analyse:

    def draw_relation(title,*args,**kwargs):
        list_x, list_y = [], []
        title_x, title_y = [], []
        for i in range(len(args)-1):
            for j in range(i+1,len(args)):
                list_x.append(args[i])
                list_y.append(args[j])
                title_x.append(title[i])
                title_y.append(title[j])
        len_show = len(list_x)
        labels = [v for k,v in kwargs.items()]
        color = ['b','g','r','c','m','y','k','w']
        plt.figure(figsize=(6.4*len_show,4.8))
        for show in range(len_show):
            ax = plt.subplot(int(str(1)+str(len_show)+str(show+1)))
            ax.set_xlabel(title_x[show])
            ax.set_ylabel(title_y[show])
            for z in range(len(labels[0])):
                color_z = labels[0][z] % 8
                ax.scatter(list_x[show][z], list_y[show][z], c = color[color_z]) 
        plt.savefig('result.jpg')
        plt.close()
    

    def autoNorm(dataSet):
        minVal = dataSet.min(0)
        maxVal = dataSet.max(0)
        ranges = maxVal - minVal
        normDataSet = np.zeros(dataSet.shape)
        m = dataSet.shape[0]
        normDataSet = dataSet-tile(minVal, (m,1))
        normDataSet = normDataSet/tile(ranges, (m,1))
        return normDataSet, ranges, minVal