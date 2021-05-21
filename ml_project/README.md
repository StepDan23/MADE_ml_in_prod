# ML Project: Heart Disease UCI

## Dataset
Download dataset from [Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci) to `data` folder

## Enviroment
* `pip3 install virtualenv`
* `virtualenv ml_project_venv` 
* `source ml_project_venv/bin/activate`
* `pip install .`

## EDA in jupyter notebook
```bash
jupyter notebook notebooks/heart_eda.ipynb
```

## Training

```bash
python ml_project/train.py --config-name ./configs/model_1.yml
python ml_project/train.py --config-name ./configs/model_2.yml
```

## Prediction

```bash
python ml_project/predict.py --config-name ./configs/model_1.yml
python ml_project/predict.py --config-name ./configs/model_2.yml
```

## Local project testing
```bash
pytest -v .
```

## Check code style with pylint
```bash
pylint ml_project --disable=C0114,C0115,C0116 --fail-under=7.0
```
