from setuptools import find_packages, setup

REQUIREMENTS_PATH = 'requirements.txt'


def get_requirements(path):
    with open(path, 'r') as fd:
        requirements = fd.read().splitlines()
    return requirements


setup(
    name="ml_project",
    packages=find_packages(),
    version="0.1.1",
    author="stepdan23",
    install_requires=get_requirements(REQUIREMENTS_PATH),
    license="MIT",
)
