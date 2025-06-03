from data.data_loader import load_symptoms_dataset
from models import predict_disease_model, analyse_unique_disease_model

print("\n###################\t\t#####################\n")
print("\tWelcome to Disease Prediction ML Model")
print("\n###################\t\t#####################\n")

# Load the symptoms dataset
diseases, symptoms = load_symptoms_dataset()

print("\nAvailable Diseases in the Model:")
for disease in diseases:
    print(f"- {disease}")

print("\nAvailable Symptoms in the Model:\n")
symptoms_collection = [s for s in symptoms]
for i in range(0, len(symptoms_collection), 4):
    for j in range(i, min(i + 4, len(symptoms_collection))):
        print(f"{j+1}. {symptoms_collection[j]}", end="\t")
    print("\n")

print("\nPlease enter the symptom number that you are experiencing from the above list. Make sure to enter atleast 3 symptoms for better result,\ne.g. 1, 5, 7\n")

input_symptoms = input().strip().split(',')
print("\nLoading the entered symptoms....\n")
valid_check = True
if(len(input_symptoms) < 3):
    print("Please enter at least 3 symptoms for better prediction.")
    valid_check = False
    
if valid_check:
    for i in input_symptoms:
        try:
            symptom_index = int(i.strip()) - 1
            if 0 <= symptom_index < len(symptoms_collection):
                print(f"- {symptoms_collection[symptom_index]}")
            else:
                print(f"Invalid symptom index: {i.strip()}")
                valid_check = False
        except ValueError:
            print(f"Invalid input: {i.strip()}. Please enter numbers only.")
            valid_check = False

if valid_check:
    print("\nSymptoms recorded, Loading the model..\n")
    input_symptoms = [symptoms_collection[int(i.strip()) - 1].lower().replace(" ","_") for i in input_symptoms]
    disease_value, accuracy = predict_disease_model(input_symptoms)
    
    predicted_disease = str(disease_value[0]).strip()
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print(f"Model Used: Gaussian Naive Bayes Classifier")
    if("epatitis" in predicted_disease):
        print(f"\nIt looks like: Liver Disease: {predicted_disease.title()}")
    else:
        print(f"\nIt looks like: {predicted_disease.title()}")
    print("For more correct prediction, please provide more information:\n")
    analyse_unique_disease_model("epatitis" in predicted_disease and "liver" or predicted_disease.strip())
        
    print("\n########## Model exited #########")
else:
    print("\n########## Model exited #########")
    exit(0)


