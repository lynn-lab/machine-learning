from numpy import *
import operator
from unicodedata import name
from tqdm import tqdm


"""  KNN   """
class KNN(object):
    def __init__(self,normMat = [0,0],dating = array([[1.0,1.1],[1.0,1.2],[0,0],[0,0.2]]), datinglabel = ['1'],k=3):
        self.normMat = normMat
        self.datinglabel = datinglabel
        self.dating = dating
        self.k = k
    def classify(self,normMat, dating,labels,k):
        dataSetSize = dating.shape[0]
        diffMat = tile(normMat,(dataSetSize,1)) - dating
        sqDiffMat = diffMat**2
        sqDistances = sqDiffMat.sum(axis=1)
        sortedDisIndices = (sqDistances**0.5).argsort()
        classCount = {}
        for i in (range(k)):
            votelLabel = labels[sortedDisIndices[i]]
            classCount[votelLabel] = classCount.get(votelLabel,0) + 1
        sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
        return sortedClassCount[0][0]
    def result(self):
        test_ratio = int(self.ratio * len(self.datinglabel))
        count = 0.0
        for i in range(test_ratio):
            class_result = self.classify(self.dating[i,:],self.dating[test_ratio:,:],self.datinglabel[test_ratio:], self.k)
            if class_result != self.datinglabel[i]:
                count += 1.0
        print(count/test_ratio)
if __name__=='__main__':
    knn_class = KNN()
    group = array([[1.0,1.1],[1.0,1.2],[0,0],[0,0.2]])
    labels = ['A','A','B','B']
    label = knn_class.classify([0,0],group,labels,k =3)
    print(label)