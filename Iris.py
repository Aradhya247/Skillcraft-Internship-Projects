from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

iris = load_iris()
X= iris.data
y = iris.target

X_train, X_test, y_train, y_test =train_test_split(
    X, y, test_size=0.2, random_state=42

)
model = DecisionTreeClassifier(max_depth = 3, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Predictions:", y_pred[:5])

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

plt.figure(figsize=(12,8))
plot_tree(model, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()