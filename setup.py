from setuptools import setup, find_packages # type: ignore

setup(
    name='CaloryPrediction',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'xgboost',
        'seaborn',
        'matplotlib'
    ],
    author='Debashis Mondal',
    author_email='debashis.deep205@gmail.com',
    description='This project is for predicting calory count after workout',
    url='https://github.com/debash1sM/E-2-E-Calory-count-prediction-using-XGboost',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)