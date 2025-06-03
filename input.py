def collect_unique_disease_inputs(disease_name):
    input_array = []
    
    if disease_name.lower() == "heart_attack":
        # [14.0, 1, 120.0, 135.0, 100.0, 130.0, 0.87, 1.3]
        gender = 1 if input("Enter Gender (Male/Female): ").strip().lower() == "male" else 0
        params = ["Age", "Heart rate", "Systolic blood pressure", "Diastolic blood pressure", "Blood sugar", "CK-MB Value", "Troponin Value"]
        for param in params:
            input_array.append(float(input(f"Enter {param}: ").strip()))
        
        input_array.insert(1, gender)
    elif disease_name.lower() == "liver":
        # [21.0, 0.8, 0.15, 191.0, 16.0, 18.0, 1.1, 1.2, 0.7, 'Male']
        input_array.append(float(input("Enter Age: ").strip()))
        gender_livr = input("Enter Gender (Male/Female): ").strip()

        params = ["Total Bilirubin", "Direct Bilirubin", "Alkaline Phosphotase"," Alamine Aminotransferase", "Aspartate Aminotransferase", "Total Proteins", "Albumin", "Albumin and Globulin Ratio"]
        for param in params:
            input_array.append(float(input(f"Enter {param}: ").strip()))
        
        input_array.append(gender_livr)
    elif disease_name.lower() == "diabetes":
        # [22.0, 0, 0, 22.0, 6.5, 84.0, 'Male', 'never']   
        gender_diab = input("Enter Gender (Male/Female/Other): ").strip()
        input_array.append(float(input("Enter Age: ").strip()))
        input_array.append(1 if input("Enter Hypertension (yes/no): ").strip().lower() == "yes" else 0)
        input_array.append(1 if input("Enter Heart Disease if any (yes/no): ").strip().lower() == "yes" else 0)
        smoking_history = input("Enter Smoking History (current, ever, former, never, No Info, not current): ").strip()
        
        params = ["BMI", "HbA1c Level", "Blood Glucose Level"]
        for param in params:
            input_array.append(float(input(f"Enter {param}: ").strip()))
            
        input_array.append(gender_diab)
        input_array.append(smoking_history)
    return input_array