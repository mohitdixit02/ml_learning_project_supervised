<h1>ML Learning Project - Supervised</h1>
<p>
    This project aim is to learn, understand and apply some basic supervised learning algorithms and comparing the models learning behaviour on different dataset.
</p>

### Table of Contents
- [Installation](#installation)
- [Project Workflow](#project-workflow)
- [Modules used](#modules-used)
- [References](#references)

## Installation

1. Clone the repo

```bash
git clone git@github.com:mohitdixit02/ml_learning_project_supervised.git
```

2. Setup a python (>=3.13) virtual environment (Snippet for Windows)

```bash
cd ml_learning_project_supervised
python -m venv venv
```

3. Activate the environment and install the dependencies

```bash
.\venv\Scripts\activate
pip install -r requirements.txt
```

4. Run the main script

```bash
python main.py
```

## Project workflow
<p>
    The project predicts the disease result (positive or negative) based on the symptoms and data provided by the user in two steps. workflow invloves:
    <ol>
    <li>Data selection and preprocessing: data selection, cleaning null values and preprocessing using services like MultiLabelBinarizer to encode multi-valued categorical columns.</li>
    <li>Model training: Data splitting and training the model using different supervised learning algorithms like Decision Tree, Random Forest, SVM, etc.</li>
    <li>Model evaluation: Evaluating the different model performances using metrics like accuracy and time for fitting</li>
    <li>Model prediction: Predicting the disease result based on the user input.</li>
    </ol>
</p>

![Project Workflow](data/workflow.png?raw=true "Project Workflow")

## Modules Used
<ol>
    <li>Pandas</li>
    <li>Matplotlib</li>
    <li>Scikit-learn</li>
    <li>Seaborn</li>
</ol>

## References
<p>Datasets are taken from Kaggle:</p>
<ol>
    <li><strong>Disease and Symptoms dataset</strong>- Choong Qian Zheng - <a href="https://www.kaggle.com/datasets/choongqianzheng/disease-and-symptoms-dataset">source</a></li>
    <li><strong>Diabetes prediction dataset</strong>- Mohammed Mustafa - <a href="https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset">source</a></li>
    <li><strong>Heart Attack Dataset</strong>- Fatemeh Mohammadinia - <a href="https://www.kaggle.com/datasets/fatemehmohammadinia/heart-attack-dataset-tarik-a-rashid">source</a></li>
    <li><strong>Indian Liver Patient Records</strong>- UCI Machine Learning - <a href="https://www.kaggle.com/datasets/uciml/indian-liver-patient-records">source</a></li>
</ol>

<h4>- Thanks -</h4>
For any query, email at: mohit.vsht@gmail.com - Mohit Sharma
