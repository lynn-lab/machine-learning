
from os import error
from model.knn import KNN as KNN
from utils.dataload import Data 
from utils.analyse import Analyse

datingmat, datinglabel = Data.data_sites('data/datingTestSet2.txt')
tuple = (datingmat[:,1],datingmat[:,2],datingmat[:,0])
analyse_data = Analyse
# analyse_data.draw_relation(['airplane mileage','game rate','ice cream'],
#                         datingmat[:,0],datingmat[:,1],datingmat[:,2],
#                         a = datinglabel)
normMat, ranges, minVal = analyse_data.autoNorm(datingmat)
knn = KNN()
count = 0.0
knn.dating = normMat
knn.datinglabel = datinglabel
knn.k = 5
knn.ratio = 0.2
knn.result()

