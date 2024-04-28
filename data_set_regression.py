#pandas
import pandas as pd

#matplotlib
import matplotlib.pyplot as plt

#seaborn
import seaborn as sns

#numpy
import numpy as np

#sklearn
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

crop_df = pd.read_csv('/content/Crop_recommendation.csv') #Our test dataset for all classification
crop_df.head()

crop_df.shape

crop_df.isnull().sum()

crop_df['no_label'] = pd.Categorical(crop_df.label).codes

plt.figure(figsize=(8,7))
sns.histplot(x='N',data=crop_df,color='b');
plt.title("Nitrogen for crops",{'fontsize':20});

plt.figure(figsize=(8,7))
sns.histplot(x='K',data=crop_df,color='b');
plt.title("Potassium for crops",{'fontsize':20});

plt.figure(figsize=(8,7))
sns.histplot(x='P',data=crop_df,color='b');
plt.title("Phosphorus for crops",{'fontsize':20});

crop_df.columns

plt.figure(figsize=(10,6))
sns.boxplot(x=crop_df.temperature);

plt.figure(figsize=(10,6))
sns.boxplot(x=crop_df.humidity);

plt.figure(figsize=(8,7))
sns.histplot(x='ph',data=crop_df,color='b');
plt.title("PH for crops",{'fontsize':20});

plt.figure(figsize=(8,7))
sns.histplot(x='rainfall',data=crop_df,color='b');
plt.title("Rainfall feature",{'fontsize':20});

X = crop_df.drop(['label','no_label'],axis=1)
y = crop_df.no_label

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

X_train.head()

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

models = {
    LogisticRegression(max_iter=500):'Logistic Regression',
    RandomForestClassifier():'Random Forest',
    SVC():'Support Vector Machine'
}
for m in models.keys():
    m.fit(X_train,y_train)
for model,name in models.items():
     print(f"Accuracy Score for {name} is : ",model.score(X_test,y_test)*100,"%")

rf = RandomForestClassifier()
rf.fit(X_train,y_train)

y_pred = rf.predict(X_test)

print(classification_report(y_test,y_pred))
