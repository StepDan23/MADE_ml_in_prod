# ML Project: Heart Disease UCI

## Dataset
Download dataset from [Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci) to `data` folder

## Enviroment
* `pip3 install virtualenv`
* `virtualenv ml_project_venv` 
* `source ml_project_venv/bin/activate`
* `pip install -r requirements.txt`

## EDA in jupyter notebook
```bash
jupyter notebook notebooks/heart_eda.ipynb
```

## Training

```bash
python -m train --config-name ./configs/model_1.yml
python -m train --config-name ./configs/model_2.yml
```

## Prediction

```bash
python -m predict --config-name ./configs/model_1.yml
python -m predict --config-name ./configs/model_2.yml
```