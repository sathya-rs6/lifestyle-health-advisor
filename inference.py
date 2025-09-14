import os
import joblib
import numpy as np


ARTIFACT_DIR = os.path.join(os.path.dirname(__file__), "artifacts")


class ModelBundle:
	def __init__(self):
		self.model = joblib.load(os.path.join(ARTIFACT_DIR, 'model.joblib'))
		self.scaler = joblib.load(os.path.join(ARTIFACT_DIR, 'scaler.joblib'))
		self.label_encoders = joblib.load(os.path.join(ARTIFACT_DIR, 'label_encoders.joblib'))
		self.feature_cols = joblib.load(os.path.join(ARTIFACT_DIR, 'feature_cols.joblib'))

	def transform_row(self, payload: dict) -> np.ndarray:
		gender = self.label_encoders['Gender'].transform([payload['gender']])[0]
		bmi = self.label_encoders['BMI Category'].transform([payload['bmi_category']])[0]
		occ = self.label_encoders['Occupation'].transform([payload['occupation']])[0]
		sleep_disorder = 0  # not used as feature; target in training

		row = [
			gender,
			payload['age'],
			occ,
			payload['sleep_duration'],
			payload['quality_of_sleep'],
			payload['physical_activity_level'],
			payload['stress_level'],
			bmi,
			payload['heart_rate'],
			payload['daily_steps'],
			payload['systolic'],
			payload['diastolic'],
		]
		row = np.asarray([row])
		row_scaled = self.scaler.transform(row)
		return row_scaled

	def predict(self, payload: dict) -> dict:
		row = self.transform_row(payload)
		pred = self.model.predict(row)[0]
		inv_map = {v: k for k, v in enumerate(['None', 'Sleep Apnea', 'Insomnia'])}
		# Our label mapping in training: ['None','Sleep Apnea','Insomnia'] -> 0,1,2 via label encoder
		# Return human-readable label via inverse of encoder
		label_encoder = self.label_encoders['Sleep Disorder']
		label = label_encoder.inverse_transform([pred])[0]
		proba = None
		if hasattr(self.model, 'predict_proba'):
			proba = self.model.predict_proba(row).max()
		return {"prediction": label, "confidence": float(proba) if proba is not None else None}


