def detect_sensitive_data(df):

    # for test purposes, we assume that the following keywords indicate sensitive data
    # later with the help of NER (Named Entity Recognition) and different regex patterns, we can improve the detection

    sensitive_keywords = ["name", "email", "phone", "address", "iban", "credit", "ssn","sex", "age", "salary", "bank"]
    detected = {col: "sensitive" for col in df.columns if any(word in col.lower() for word in sensitive_keywords)}
    return detected

def classify_data(df):

    # for test purposes, we assume that the following keywords indicate the type of data

    classifications = {}
    
    for col in df.columns:
        if any(keyword in col.lower() for keyword in ["name", "email", "phone", "ssn"]):
            classifications[col] = "Identifying"
        elif any(keyword in col.lower() for keyword in ["iban", "credit", "salary", "bank"]):
            classifications[col] = "Financial"
        elif df[col].dtype == 'object':
            classifications[col] = "Textual Data"
        elif df[col].dtype in ['int64', 'float64']:
            classifications[col] = "Numerical Data"
        else:
            classifications[col] = "General Data"
    
    return classifications