import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle
import os

def train():
    if not os.path.exists('data/supply_chain_data.csv'):
        print("Data not found. Please run data_generator.py first.")
        return
        
    df = pd.read_csv('data/supply_chain_data.csv')
    
    # Preprocessing
    categorical_cols = ["Category", "Weather_Condition", "Carrier_Type"]
    
    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
        
    features = ["Order_Value_INR", "Defect_Rate_Pct", "Delay_Rate_Pct", "Lead_Time_Days", "Category", "Weather_Condition", "Carrier_Type"]
    X = df[features]
    y = df["Risk_Level"]  # Target variable
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    # Initialize and train Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    print(f"Model trained with accuracy: {accuracy:.2f}")
    
    # Save the model and preprocessors for the Streamlit web app to use
    os.makedirs('models', exist_ok=True)
    with open('models/risk_model.pkl', 'wb') as f:
        pickle.dump(model, f)
        
    with open('models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
        
    with open('models/encoders.pkl', 'wb') as f:
        pickle.dump(encoders, f)
        
    print("Model and preprocessors saved to models/ directory successfully!")

if __name__ == "__main__":
    train()
