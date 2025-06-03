import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.svm import SVC
from data.data_loader import load_disease_symptoms_training_data, unique_disease_training_data
from input import collect_unique_disease_inputs
import time

models = [
    GaussianNB(),
    LogisticRegression(max_iter=5000),
    DecisionTreeClassifier(random_state=42),
    RandomForestClassifier(random_state=42, n_estimators=100),
    SVC(random_state=42),
]

def predict_disease_model(input_symptoms):
    x_train, x_test, y_train, y_test, mlb = load_disease_symptoms_training_data()
    model = GaussianNB()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    cleaned_symptoms = [str(sym).strip() for sym in input_symptoms]
    user_input = pd.DataFrame(mlb.transform([cleaned_symptoms]), columns=mlb.classes_)
    user_pred_result = model.predict(user_input)    
    
    return user_pred_result, accuracy

def analyse_unique_disease_model(disease_name):
    x_train, x_test, y_train, y_test, mlb = unique_disease_training_data(disease_name.lower().replace(" ", "_"))
    input_array = collect_unique_disease_inputs(disease_name.lower().replace(" ", "_"))
    print("\nGenerating output...\n")
    results = []
    best_result = {
        "name": "",
        "accuracy": 0.0,
        "prediction": None
    }
    user_input = None
    
    if disease_name == "Diabetes":
        gender_val, smoke_val = [[str(val).strip()] for val in input_array[-2:]]
        gender_transformed = pd.DataFrame(mlb[0].transform([gender_val]), columns=mlb[0].classes_)
        smoke_transformed = pd.DataFrame(mlb[1].transform([smoke_val]), columns=mlb[1].classes_)
        user_input = pd.DataFrame([input_array[:6]], columns=x_train.columns[:6])
        user_input = pd.concat([user_input, gender_transformed, smoke_transformed], axis=1)
    elif disease_name == "liver":
        gender_val = [[str(val).strip()] for val in input_array[-1:]]
        gender_transformed = pd.DataFrame(mlb[0].transform(gender_val), columns=mlb[0].classes_)
        user_input = pd.DataFrame([input_array[:-1]], columns=x_train.columns[:-2])
        user_input = pd.concat([user_input, gender_transformed], axis=1)
    else:
        user_input = pd.DataFrame([input_array], columns=x_train.columns)
                    
    for model in models:
        start_time = time.time()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        model_name = model.__class__.__name__
        user_pred_result = model.predict(user_input)
        end_time = time.time()
        user_pred_final_result = ""
        if disease_name == "Diabetes" or disease_name == "liver":
            user_pred_final_result = "positive" if str(user_pred_result[0]) == "1" else "negative"
        else:
            user_pred_final_result = str(user_pred_result[0])
        val = {
            "name": model_name,
            "accuracy": accuracy * 100,
            "prediction": user_pred_final_result,
            "time_taken": end_time - start_time
        }
        results.append(val)
        if val["accuracy"] > best_result["accuracy"]:
            best_result = val
    
    print("########################################")
    print(f"Prediction for the disease {disease_name}: {best_result['prediction']}")
    print(f"Best model used: {best_result['name']}")
    print(f"Model Accuracy: {best_result['accuracy']:.2f}%")
    print("########################################")
    print("\nAll Model Results:")
    for result in results:
        print(f"Model: {result['name']}, Accuracy: {result['accuracy']:.2f}%, Prediction: {result['prediction']}, Time Taken: {result['time_taken']:.4f} seconds")
    
    # plotting confusion matrix for the best model
    best_model = next((model for model in models if model.__class__.__name__ == best_result['name']), None)
    if best_model:
        y_pred_best = best_model.predict(x_test)
        cm = confusion_matrix(y_test, y_pred_best)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Negative", "Positive"])
        disp.plot(cmap=plt.cm.Blues)
        plt.title(f'Confusion Matrix for {best_result["name"]}')
        plt.tight_layout()
        
    
    # plotting accuracy vs model
    plt.figure(figsize=(10, 5))
    sns.barplot(x=[result['name'] for result in results], y=[result['accuracy'] for result in results])
    plt.title(f'Accuracy of models for {disease_name} prediction')
    plt.xlabel('Model')
    plt.ylabel('Accuracy (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # plotting Time taken vs model
    plt.figure(figsize=(10, 5))
    sns.barplot(x=[result['name'] for result in results], y=[result['time_taken'] for result in results])
    plt.title(f'Time taken by models for {disease_name} prediction')
    plt.xlabel('Model')
    plt.ylabel('Time Taken (seconds)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return 0