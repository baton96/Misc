from sklearn.datasets import load_iris
from sklearn.tree import _tree, DecisionTreeClassifier


def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [feature_names[i] for i in tree_.feature]

    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print("{}if {} <= {}:".format(indent, name, round(threshold, 2)))
            recurse(tree_.children_left[node], depth + 1)
            print("{}else:  # if {} > {}".format(indent, name, round(threshold, 2)))
            recurse(tree_.children_right[node], depth + 1)
        else:
            print("{}return {}".format(indent, np.argmax(tree_.value[node])))

    recurse(0, 0)


iris = load_iris()
X = iris.data
y = iris.target
model = DecisionTreeClassifier(max_depth=3)
model.fit(X, y)
tree_to_code(model, iris.feature_names)
