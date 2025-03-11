def anonymize_data(df, method="K-Anonymity", k_value=3):
    df_anonymized = df.copy()

    if method == "K-Anonymity":
        df_anonymized = apply_k_anonymity(df_anonymized, k_value)

    elif method == "L-Diversity":
        df_anonymized = apply_l_diversity(df_anonymized)

    return df_anonymized

# very simple implementation of K-Anonymity
def apply_k_anonymity(df, k):
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        df[col] = df[col] // k * k
    return df

def apply_l_diversity(df):
    for col in df.select_dtypes(include=['object']).columns:
        unique_values = df[col].nunique()
        if unique_values > 5:
            df[col] = df[col].apply(lambda x: "Group " + str(hash(x) % 5))
    return df