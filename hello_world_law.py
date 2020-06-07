from sklearn.tree import DecisionTreeClassifier
X = [[6,11],[5.5,10],[7,9],[5,12]]
y = [1,1,0,1]
clf = DecisionTreeClassifier()
clf.fit(X,y)
print(clf.predict([5,11]))
