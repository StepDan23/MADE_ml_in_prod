from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SplittingParams:
    val_size: float = 0.2
    random_state: int = 42


@dataclass
class TrainingParams:
    params: dict
    model_type: str = "LogisticRegression"


@dataclass
class FeatureParams:
    cat_features: List[str]
    num_features: List[str]
    features_to_drop: Optional[List[str]]
    target_col: Optional[str]


@dataclass
class Config:
    logger_config_path: str
    input_data_path: str
    test_data_path: str
    predict_path: str
    output_model_path: str
    metric_path: str
    split_params: SplittingParams
    train_params: TrainingParams
    feature_params: FeatureParams
