import pickle
import re

model=pickle.load(open("models/model.pkl","rb"))

def extract_features(url):
    return[
        len(url),
        url.count('.'),
        url.count('-'),
        url.count('@'),
        int(bool(re.search(r'\d+\.\d+\.\d+\.\d+',url)))
    ]
def predict_url(url):
    features=[extract_features(url)]
    prediction=model.predict(features)[0]

    return "SAFE" if prediction==0 else "MALICIOUS"