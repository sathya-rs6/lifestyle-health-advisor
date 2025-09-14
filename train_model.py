import os
import joblib
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "Sleep_health_and_lifestyle_dataset.csv")
ARTIFACT_DIR = os.path.join(os.path.dirname(__file__), "artifacts")
os.makedirs(ARTIFACT_DIR, exist_ok=True)


def load_and_prepare_dataset(csv_path: str) -> tuple[pd.DataFrame, pd.Series, dict]:
	data = pd.read_csv(csv_path)
	data['Sleep Disorder'] = data['Sleep Disorder'].fillna('None')
	data['BMI Category'] = data['BMI Category'].replace({'Normal Weight': 'Normal'})

	# Split blood pressure
	data[['Systolic', 'Diastolic']] = data['Blood Pressure'].str.split('/', expand=True).astype(int)
	data = data.drop('Blood Pressure', axis=1)

	# Label encoders
	label_encoders: dict[str, preprocessing.LabelEncoder] = {}
	for col, classes in [
		('Gender', ['Female', 'Male']),
		('BMI Category', ['Normal', 'Overweight', 'Obese']),
		('Sleep Disorder', ['None', 'Sleep Apnea', 'Insomnia']),
		('Occupation', ['Software Engineer', 'Doctor', 'Sales Representative', 'Teacher','Nurse', 'Engineer', 'Accountant', 'Scientist', 'Lawyer','Salesperson', 'Manager'])
	]:
		le = preprocessing.LabelEncoder()
		le.fit(classes)
		data[col] = le.transform(data[col])
		label_encoders[col] = le

	# Features and target
	feature_cols = ['Gender', 'Age', 'Occupation', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level', 'BMI Category', 'Heart Rate', 'Daily Steps', 'Systolic', 'Diastolic']
	X = np.asarray(data[feature_cols])
	y = np.asarray(data['Sleep Disorder'])

	# Scale numeric features
	scaler = preprocessing.StandardScaler()
	X_scaled = scaler.fit_transform(X)

	artifacts = {
		'scaler': scaler,
		'label_encoders': label_encoders,
		'feature_cols': feature_cols,
	}

	return pd.DataFrame(X_scaled, columns=feature_cols), pd.Series(y), artifacts


def train_and_save():
	X, y, artifacts = load_and_prepare_dataset(DATA_FILE)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

	model = RandomForestClassifier(max_depth=None, min_samples_leaf=1, min_samples_split=10, n_estimators=200, random_state=42)
	model.fit(X_train, y_train)

	pred = model.predict(X_test)
	acc = accuracy_score(y_test, pred)
	print(f"Accuracy: {acc:.4f}")
	print(classification_report(y_test, pred))

	# Save artifacts
	joblib.dump(model, os.path.join(ARTIFACT_DIR, 'model.joblib'))
	joblib.dump(artifacts['scaler'], os.path.join(ARTIFACT_DIR, 'scaler.joblib'))
	joblib.dump(artifacts['label_encoders'], os.path.join(ARTIFACT_DIR, 'label_encoders.joblib'))
	joblib.dump(artifacts['feature_cols'], os.path.join(ARTIFACT_DIR, 'feature_cols.joblib'))
	print(f"Saved artifacts to {ARTIFACT_DIR}")


if __name__ == "__main__":
	train_and_save()


