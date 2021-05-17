# ML Project: Heart Disease UCI

## Dataset
Download artefacts from [google-disk](https://drive.google.com/file/d/1NQrmECZzrwe_00aRVLDg4v1dkL4Hku5m/view?usp=sharing) to `artefacts` folder
```bash
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1NQrmECZzrwe_00aRVLDg4v1dkL4Hku5m' -O artefacts.zip && unzip artefacts.zip
```

## Enviroment
* `pip3 install virtualenv`
* `virtualenv venv_online` 
* `source venv_online/bin/activate`
* `pip install .`

## Launch application

```bash
MODEL_PATH='artefacts/model.pkl' uvicorn online_inference.app:app
```

## Queries with a script

```bash
python online_inference/request.py --config-name='configs/request.yml'
```

## Local project testing
```bash
MODEL_PATH=artefacts/model.pkl pytest -v .
```

## Check code style with pylint
```bash
pylint online_inference --disable=C0114,C0115,C0116 --fail-under=7.0
```
