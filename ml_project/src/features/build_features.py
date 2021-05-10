import logging
from typing import List

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.config.config_classes import FeatureTransformer
import src.features.transformers as T

logger = logging.getLogger(__name__)


def build_transformer(transform_params: List[FeatureTransformer]) -> ColumnTransformer:

    transformers = []
    for param in transform_params:
        logger.info("creating  '%s' column transformers", param.trans_name)
        pipeline = Pipeline([(param.trans_class, getattr(T, param.trans_class)(**param.params)), ])
        transformers.append((param.trans_name, pipeline, param.column_names))
    return ColumnTransformer(transformers)


def make_features(transformer: ColumnTransformer, df: pd.DataFrame) -> pd.DataFrame:
    logger.info("create features for dataset with shape %s", df.shape)

    features = transformer.transform(df)
    features_df = pd.DataFrame(features)
    logger.info("created %s new features", features.shape[1])

    return features_df
