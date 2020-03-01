from sklearn import tree #import the library
features = [[140,1],[175,2],[175,1],[140,2]] #input
labels = [0,0,1,1] #output
clf = tree.DecisionTreeClassifier() #make a classifier
clf = clf.fit(features,labels) #classify
print(clf.predict[140,2]) #predict
