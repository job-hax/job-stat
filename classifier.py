from sklearn import tree
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def DecisionTree(x_train, y_train, x_test, criterion_name):
    model = tree.DecisionTreeClassifier(criterion = criterion_name)

    model.fit(x_train, y_train)

    y_test = model.predict(x_test)
    return y_test


def SVM(kernel_name,x_train,y_train,x_test,x_train_num,x_test_num):
    model = svm.SVC(kernel=kernel_name)
    for i in range(10):
        valid_set_size = 0.10

        XTrain, XTest, yTrain, yTest = train_test_split(x_train_num, y_train, test_size=valid_set_size)

        model.fit(XTrain, yTrain)

        yPred = model.predict(XTest)
        print('the validation set size: ' + str(valid_set_size))

        score = accuracy_score(yTest, yPred)
        print('the validation accuracy: ' + str(score))
    y_test = model.predict(x_test_num)
    return y_test
