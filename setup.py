from setuptools import setup

setup(
    name="ProtMIMO",
    version="1.0",
    description="MIMO for protein function prediction.",
    packages=["ProtMIMO"],  # same as name
    install_requires=[
        "matplotlib==3.5.1",
        "matplotlib-inline==0.1.3",
        "numpy==1.22.0",
        "pandas==1.3.5",
        "scikit-learn==1.0.2",
        "scipy==1.8.0",
        "seaborn==0.11.2",
        "sklearn==0.0",
        "tape-proteins==0.5",
        "tensorboard==2.10.1",
    ],  # external packages as dependencies
)
