import pandas as pd
import re
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv("data/urls.csv")

def extract_features(url):
    return[
        len(url),
        url.count('.'),
        url.count('-'),
        url.count('@'),
        int(bool(re.search(r'\d+\.\d+\.\d+\.\d+',url)))
    ]
X=df['url'].apply(lambda x:extract_features(x)).tolist()
y=df['label']

model=RandomForestClassifier()
model.fit(X,y)

pickle.dump(model,open("models/model.pkl","wb"))

print("Model is trained and saved!")