from sklearn import tree
features = [[140,1],[175,2],[175,1],[140,2]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict[140,2])
