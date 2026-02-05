from fastapi import APIRouter
from backend.services.predict_service import predict_potability

router = APIRouter()


@router.post("/predict")
def predict(data: dict):
    result = predict_potability(data)
    return {"potability": result}
