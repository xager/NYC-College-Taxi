import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import metrics as ms
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt

data = pd.read_csv("./Data/final_data_extraction_for_sept_2015_with_bins.csv")
rows, columns = data.shape
print rows,columns
X = data.iloc[:,0:columns-1]
#X = X.drop("payment_type", 1)
Y = data.iloc[:,-1]
#X_train.shape, X_test.shape, y_train.shape, y_test.shape

lr_accuracy = []
svc_accuracy = []
"""
from sklearn.linear_model import LogisticRegression
reg = LogisticRegression()
reg = reg.fit(X_train, y_train)
y_pred_lr = reg.predict(X_test)


from sklearn.svm import LinearSVC
svc = LinearSVC()
svc = svc.fit(X_train, y_train)
y_pred_svc = svc.predict(X_test)


from sklearn import metrics as ms
svc_accuracy = ms.accuracy_score(y_test, y_pred_svc)
print svc_accuracy

lr_accuracy = ms.accuracy_score(y_test, y_pred_lr)
print lr_accuracy
"""
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
    reg = LogisticRegression()
    reg = reg.fit(X_train, y_train)
    y_pred_lr = reg.predict(X_test)
    lr_accuracy.append(ms.accuracy_score(y_test, y_pred_lr))


    svc = LinearSVC()
    svc = svc.fit(X_train, y_train)
    y_pred_svc = svc.predict(X_test)
    svc_accuracy.append(ms.accuracy_score(y_test, y_pred_svc))

print lr_accuracy
print svc_accuracy

plt.plot(lr_accuracy, 'ro', svc_accuracy, 'b--')
plt.show()