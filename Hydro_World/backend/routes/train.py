from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.ml_service import train_models

router = APIRouter()


class TrainRequest(BaseModel):
    device: str = "cpu"

    # SVM hyperparameters
    svm_C: float = 1.0
    svm_kernel: str = "rbf"
    svm_gamma: str = "scale"

    # GB hyperparameters
    gb_n_estimators: int = 400
    gb_learning_rate: float = 0.03
    gb_max_depth: int = 4
    gb_subsample: float = 0.85

    # Combined weights
    combined_svm_weight: float = 0.5
    combined_gb_weight: float = 0.5


@router.post("/train")
def train_model(request: TrainRequest):
    svm_params = {
        "C": request.svm_C,
        "kernel": request.svm_kernel,
        "gamma": request.svm_gamma
    }

    gb_params = {
        "n_estimators": request.gb_n_estimators,
        "learning_rate": request.gb_learning_rate,
        "max_depth": request.gb_max_depth,
        "subsample": request.gb_subsample
    }

    combined_weights = (request.combined_svm_weight, request.combined_gb_weight)

    return train_models(
        device=request.device,
        svm_params=svm_params,
        gb_params=gb_params,
        combined_weights=combined_weights
    )
