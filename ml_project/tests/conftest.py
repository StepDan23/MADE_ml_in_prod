import pytest
import yaml


@pytest.fixture()
def faker_seed():
    return 42


@pytest.fixture
def fake_dataset(faker):
    faker.set_arguments("num", {"min_value": 1, "max_value": 3_000})
    faker.set_arguments("cat", {"min_value": 0, "max_value": 4})
    faker.set_arguments("target", {"min_value": 0, "max_value": 1})
    data = faker.csv(
        header=("num", "cat", "bin", "target"),
        data_columns=(
            "{{pyfloat:num}}",
            "{{pyint:cat}}",
            "{{pyint:target}}",
        ),
        num_rows=300,
        include_row_ids=False,
    ).replace("\r", "")

    return data


@pytest.fixture
def config_dict():
    config_str = """
        logger_config_path: "configs/logging.conf.yml"
        input_data_path: "data/heart.csv"
        test_data_path: "data/heart.csv"
        predict_path: "models/predicts.csv"
        output_model_path: "models/model.pkl"
        metric_path: "models/metrics.json"
        
        split_params:
            val_size: 0.1
            random_state: 23
        
        train_params:
            model_type: "LogisticRegression"
            params:
                random_state: 23
        
        feature_params:
            cat_features:
                - "cat"
            num_features:
                - "num"
            features_to_drop:
                - "drop"
            target_col: "target"
    """

    config_dict = yaml.safe_load(config_str)

    return config_dict


@pytest.fixture
def config_path(tmp_path, fake_dataset, config_dict):
    fake_input_data_path = str(tmp_path / "data.csv")
    with open(fake_input_data_path, "w") as f:
        f.write(fake_dataset)

    config_dict["input_data_path"] = fake_input_data_path
    config_dict["test_data_path"] = fake_input_data_path
    config_dict["predict_path"] = str(tmp_path / config_dict["predict_path"])
    config_dict["output_model_path"] = str(tmp_path / config_dict["output_model_path"])
    config_dict["metric_path"] = str(tmp_path / config_dict["metric_path"])

    config_path = tmp_path / "config.yml"
    with open(config_path, "w") as fd:
        yaml.dump(config_dict, fd)

    return config_path
