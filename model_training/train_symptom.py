# model_training/train_symptom.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# ensure target path exists
os.makedirs("backend/models", exist_ok=True)

# load generated demo data
df = pd.read_csv("data/Training.csv")

# features and target
X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# encode labels
le = LabelEncoder()
y_enc = le.fit_transform(y)

# split and train
X_train, X_test, y_train, y_test = train_test_split(X, y_enc, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

print("Train acc:", model.score(X_train, y_train))
print("Test acc:", model.score(X_test, y_test))

# save model + label encoder to backend/models
pickle.dump(model, open("backend/models/symptom_model.pkl", "wb"))
pickle.dump(le, open("backend/models/label_encoder.pkl", "wb"))



print("Saved symptom_model.pkl and label_encoder.pkl to backend/models/")
