from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from .inference import ModelBundle


class SuggestRequest(BaseModel):
	age: int = Field(..., ge=0, le=120)
	physical_activity_level: float = Field(..., ge=0, le=10)
	stress_level: float = Field(..., ge=0, le=10)
	gender: str
	heart_rate: Optional[float] = None
	blood_pressure: Optional[float] = None
	sleep_disorder: Optional[str] = None


app = FastAPI(title="Lifestyle Recommendation API")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


def suggest_health(req: SuggestRequest) -> list[str]:
	suggestions: list[str] = []

	if req.age <= 12 and req.physical_activity_level <= 2:
		suggestions.append(
			"For children below 12 years with low physical activity, encourage outdoor play and limit screen time."
		)

	if req.stress_level >= 7:
		suggestions.append(
			"High stress can impact health. Practice relaxation like meditation or yoga."
		)

	if (req.sleep_disorder or "").lower() == "insomnia":
		suggestions.append(
			"For insomnia, limit caffeine, include tryptophan-rich foods, and avoid heavy meals near bedtime."
		)

	if req.heart_rate is not None and req.heart_rate > 100:
		suggestions.append(
			"Elevated heart rate observed. Consider consulting a healthcare professional if persistent."
		)
	if req.blood_pressure is not None and req.blood_pressure > 120:
		suggestions.append(
			"Elevated blood pressure observed. Monitor regularly and consult a professional if needed."
		)

	if req.age > 12 and req.stress_level < 7 and (req.blood_pressure is None or req.blood_pressure <= 120):
		suggestions.append(
			"Age, stress, and blood pressure are within normal ranges. Keep up the good work!"
		)

	if not suggestions:
		suggestions.append("Provide more details or adjust inputs to receive tailored suggestions.")

	return suggestions


@app.post("/suggest")
def suggest(req: SuggestRequest):
	return {"suggestions": suggest_health(req)}


@app.get("/")
def root():
	return {"status": "ok"}



class PredictRequest(BaseModel):
	age: int
	gender: str
	occupation: str
	sleep_duration: float
	quality_of_sleep: float
	physical_activity_level: float
	stress_level: float
	bmi_category: str
	heart_rate: float
	daily_steps: float
	systolic: int
	diastolic: int


_MODEL: ModelBundle | None = None


def _get_model() -> ModelBundle:
	global _MODEL
	if _MODEL is None:
		_MODEL = ModelBundle()
	return _MODEL


@app.post("/predict")
def predict(req: PredictRequest):
	model = _get_model()
	return model.predict(req.dict())