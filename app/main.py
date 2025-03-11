import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from backend.data_loader import load_data
from backend.anonymization import anonymize_data
from backend.risk_analyzer import detect_sensitive_data, classify_data

st.set_page_config(page_title="data-anonymizer", layout="wide")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Choose a page", ["Upload data", "Detection & Classification", "Anonymization", "Results"])

if page == "Upload data":
    st.title("📂 Upload data")
    
    uploaded_file = st.file_uploader("Please uplaod a file", type=["csv, json, xml"])
    
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.session_state["df"] = df
        st.write("File successfully loaded:")
        st.dataframe(df.head())

elif page == "Detection & Classification":
    st.title("🔍 Detection & Classification")

    if "df" in st.session_state:
        df = st.session_state["df"]
        
        sensitive_info = detect_sensitive_data(df)
        st.write("🚨 Detected sensitive information:")
        st.json(sensitive_info)

        classified_data = classify_data(df)
        st.write("📌 Classified data:")
        st.json(classified_data)
    else:
        st.warning("Please upload a file first")

elif page == "Anonymization":
    st.title("🛡️ Anonymization")
    
    if "df" in st.session_state:
        df = st.session_state["df"]
        
        method = st.selectbox("Please select the wished anonymization model", ["K-Anonymity", "L-Diversity", "Differential Privacy"])
        k_value = st.slider("Please select the k-value", 2, 10, 3) if method == "K-Anonymity" else None
        
        anonymized_df = anonymize_data(df, method, k_value)
        st.session_state["anonymized_df"] = anonymized_df

        st.write("✅ Anonymized data:")
        st.dataframe(anonymized_df.head())

    else:
        st.warning("Please upload a file first")

elif page == "Results":
    st.title("📊 Results")

    if "anonymized_df" in st.session_state:
        st.write("📌 Original data:")
        st.dataframe(st.session_state["df"].head())

        st.write("🛡️ Anonymized data:")
        st.dataframe(st.session_state["anonymized_df"].head())
    else:
       st.warning("Please upload a file first")
