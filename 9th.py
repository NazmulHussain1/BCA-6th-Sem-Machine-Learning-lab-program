#9)Write a python progran to implement a decession tree using scikit-learn and visualize
import numpy as np
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.tree import export_text
import matplotlib.pyplot as plt
x=np.array([[150,0],[170,1],[120,0],[140,1],[200,1],[130,0]])
y=np.array(['apple','orrange','apple','orange','melon','apple'])
clf=DecisionTreeClassifier(random_state=42)
clf.fit(x,y)
tree_rules=export_text(clf,feature_names=['weight','Texture'])
print("Decision Tree Classifier Rules:\n",tree_rules)
plt.figure(figsize=(10,6))
plot_tree(clf,filled=True,feature_names=['weight','Texture'],class_names=np.unique(y))
plt.show()
