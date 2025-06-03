import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer

# Name Formattor
def format_name(name):
    name = name.strip()
    expanded_name = name.replace('_', ' ').title()
    return expanded_name

# Load Symptoms Dataset
def load_symptoms_dataset():
    try:
        dataset = pd.read_csv('./data/DiseaseSymptoms.csv')
        print("Diseases and Symptoms dataset loaded successfully.")
        disease_set = set()
        symptoms_set = set()
        for index, row in dataset.iterrows():
            for disease in row[0:1]:
                if not pd.isnull(disease) and disease != '':
                    name = format_name(disease)
                    disease_set.add(name)
            for symptom in row[1:]:
                if not pd.isnull(symptom) and symptom != '':
                    symptm_name = format_name(symptom)
                    symptoms_set.add(symptm_name)
        return disease_set, symptoms_set
    except FileNotFoundError:
        print("Symptoms dataset file not found.")
        return None
    
def load_disease_symptoms_training_data():
    try:
        dataset = pd.read_csv('./data/DiseaseSymptoms.csv')
        mlb = MultiLabelBinarizer()
        print("Disease Symptoms training data loaded successfully.")
        print("Dataset shape:", dataset.shape)
        
        x_cord = dataset.drop(columns=['Disease'])
        symptom_lists = x_cord.apply(lambda row: [str(symptom).strip() for symptom in row.dropna()], axis=1)
        encoded_x_cord = pd.DataFrame(mlb.fit_transform(symptom_lists), columns=mlb.classes_, index=x_cord.index)
        y_cord = dataset['Disease']
        x_train, x_test, y_train, y_test = train_test_split(encoded_x_cord, y_cord, test_size=0.2, random_state=42)
        return x_train, x_test, y_train, y_test, mlb
    except FileNotFoundError:
        print("Disease Symptoms training data file not found.")
        return None


def unique_disease_training_data(disease_name):
    try:
        url=""
        output=""
        if disease_name == "heart_attack":
            url = './data/HeartMedicaldataset.csv'
            output="Result"
        elif disease_name == "diabetes":
            url = './data/diabetes_prediction_dataset.csv'
            output="diabetes"
        elif disease_name == "liver":
            url = './data/indian_liver_patient.csv'
            output="Dataset"
        dataset = pd.read_csv(url)
        dataset = dataset.dropna()  # Drop rows with NaN values
        print(f"{disease_name} training data loaded successfully.")
        print("Dataset shape:", dataset.shape)
        
        x_cord = dataset.drop(columns=[output])
        y_cord = dataset[output]
        encoded_x_cord = x_cord
        
        # encoding categorical variables if necessary
        mlb_set = []
        if disease_name == "diabetes":
            mlb_gender = MultiLabelBinarizer()
            mlb_smoke = MultiLabelBinarizer()
            list_t1 = x_cord["gender"].apply(lambda x: [x.strip()])
            list_t2 = x_cord["smoking_history"].apply(lambda x: [x.strip()])
            x_cord_t1 = pd.DataFrame(mlb_gender.fit_transform(list_t1), columns=mlb_gender.classes_, index=x_cord.index)
            x_cord_t2 = pd.DataFrame(mlb_smoke.fit_transform(list_t2), columns=mlb_smoke.classes_, index=x_cord.index)
            encoded_x_cord = pd.concat([x_cord.drop(columns=['gender', 'smoking_history']), x_cord_t1, x_cord_t2], axis=1)
            mlb_set = [mlb_gender, mlb_smoke]
        elif disease_name == "liver":
            mlb_gender_livr = MultiLabelBinarizer()
            list_t = x_cord["Gender"].apply(lambda x: [x.strip()])
            x_cord_t = pd.DataFrame(mlb_gender_livr.fit_transform(list_t), columns=mlb_gender_livr.classes_, index=x_cord.index)
            encoded_x_cord = pd.concat([x_cord.drop(columns=["Gender"]), x_cord_t], axis=1)
            mlb_set = [mlb_gender_livr]
        x_train, x_test, y_train, y_test = train_test_split(encoded_x_cord, y_cord, test_size=0.2, random_state=42)
        return x_train, x_test, y_train, y_test, mlb_set
    except FileNotFoundError:
        print(f"{disease_name} training data file not found.")
        return None