import pandas as pd
import numpy as np
import random
import os

def generate_data(num_records=1000):
    np.random.seed(42)
    random.seed(42)
    suppliers = [f"SUPP_{i:03d}" for i in range(1, 51)]
    categories = ["Electronics", "Raw Materials", "Packaging", "Machinery", "Textiles"]
    weather = ["Clear", "Rain", "Storm", "Snow"]
    carriers = ["Road", "Air", "Sea", "Rail"]
    
    data = []
    for _ in range(num_records):
        supp = random.choice(suppliers)
        cat = random.choice(categories)
        order_value = np.round(np.random.uniform(50_000, 10_000_000), 2)  # INR
        defect_rate = np.round(np.random.uniform(0.1, 15.0), 2)
        delay_rate = np.round(np.random.uniform(1.0, 30.0), 2)
        lead_time = np.random.randint(2, 60)
        wth = random.choice(weather)
        crr = random.choice(carriers)
        
        # Calculate risk score based on synthetic rules
        risk_score = 0
        if wth in ["Storm", "Snow"]: risk_score += 30
        elif wth == "Rain": risk_score += 10
        if defect_rate > 10: risk_score += 25
        elif defect_rate > 5: risk_score += 10
        if delay_rate > 20: risk_score += 25
        elif delay_rate > 10: risk_score += 10
        if lead_time > 40: risk_score += 15
        
        if crr == "Sea": risk_score += 10
        elif crr == "Road": risk_score += 5
        
        # Noise
        risk_score += np.random.randint(-10, 15)
        risk_score = max(0, min(100, risk_score))
        
        if risk_score > 65:
            risk_level = "High"
        elif risk_score > 35:
            risk_level = "Medium"
        else:
            risk_level = "Low"
            
        data.append({
            "Supplier_ID": supp,
            "Category": cat,
            "Order_Value_INR": order_value,
            "Defect_Rate_Pct": defect_rate,
            "Delay_Rate_Pct": delay_rate,
            "Lead_Time_Days": lead_time,
            "Weather_Condition": wth,
            "Carrier_Type": crr,
            "Risk_Score": risk_score,
            "Risk_Level": risk_level
        })
        
    df = pd.DataFrame(data)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/supply_chain_data.csv', index=False)
    print("Data generated successfully at data/supply_chain_data.csv!")
    return df

if __name__ == "__main__":
    generate_data(2000)
