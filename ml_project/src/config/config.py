import logging

import yaml

from src.config.config_classes import Config, SplittingParams, TrainingParams, FeatureParams

logger = logging.getLogger(__name__)


def build_config(config_path: str) -> Config:
    logger.info("building config from %s", config_path)

    with open(config_path) as fd:
        config_dict = yaml.safe_load(fd)

    config_dict['split_params'] = SplittingParams(**config_dict['split_params'])
    config_dict['train_params'] = TrainingParams(**config_dict['train_params'])
    config_dict['feature_params'] = FeatureParams(**config_dict['feature_params'])
    return Config(**config_dict)
