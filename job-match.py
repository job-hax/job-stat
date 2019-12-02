import data_tools as dtt
from classifier import SVM
from classifier import DecisionTree


x_train, y_train = dtt.load_data('train.csv','train')
X, x_test = dtt.load_data('test.csv','test')

# Convert to numeric
x_train_num = dtt.convert_categorical(x_train)
x_test_num = dtt.convert_categorical(x_test)

# Apply one of Classfier Algorithms
classifier = input('Enter classifier: dt or svm ')
if classifier=='svm':
    kernel_name = input('Select kernel function for SVM: linear, poly, rbf or sigmoid: ')
    # Predict using SVM classification
    print('Training and validating via SVM')
    y_test = SVM(kernel_name,x_train,y_train,x_test,x_train_num,x_test_num)
elif classifier=='dt':
    # Predict using Decision Tree classification
    print('Training and validating via Decision Tree')
    y_test = DecisionTree(x_train_num, y_train, x_test_num, 'gini')

# Save results to file
print('The prediction result is saved to file in job_match_'+classifier+'.csv')
dtt.merge_to_file(X, y_test)