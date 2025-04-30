from setuptools import setup, find_packages

setup(
    name='autoview',
    version='0.1',
    description='One-line Python EDA assistant',
    author='Abhi Betha',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
        'tabulate',
        "missingno",
        'scikit-learn'
    ],
    python_requires='>=3.6',
)