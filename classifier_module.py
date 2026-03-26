import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_FILENAME = os.path.join(SCRIPT_DIR, 'churn_classifier.pkl')
DATA_FILENAME = os.path.join(SCRIPT_DIR, 'customer_churn_data.csv')

def load_data_and_train():
    """Loads data, trains the ML model, and saves it."""
    try:
        df = pd.read_csv(DATA_FILENAME)
        
        # 1. Prepare Data: Features (X) and Target (y)
        X = df[['Contract Duration (Months)', 'Monthly Usage (GB)', 'Support Tickets','Login Frequency','Days Since Last Login']]
        y = df['Churn Score']
        
        # 2. Split Data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # 3. Train Model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # 4. Evaluate (Optional, but good practice)
        accuracy = model.score(X_test, y_test)
        print(f"ML Model Trained. Validation Accuracy: {accuracy:.2f}")
        
        # 5. Save the trained model
        with open(MODEL_FILENAME, 'wb') as file:
            pickle.dump(model, file)
        print(f"Model saved as {MODEL_FILENAME}.")
        return True

    except FileNotFoundError:
        print(f"Error: Training data file '{DATA_FILENAME}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred during training: {e}")
        return False

def load_and_predict_churn(contract_months, usage_gb, tickets,login_frequency,days_since_last_login):
    """Loads the model and predicts the churn risk category."""
    if not os.path.exists(MODEL_FILENAME):
        print("Model file not found. Training model now...")
        if not load_data_and_train():
            return "ERROR"
            
    try:
        # Load the model
        with open(MODEL_FILENAME, 'rb') as file:
            model = pickle.load(file)
            
        # Prepare the input for prediction (must be a 2D array/DataFrame row)
        input_data = pd.DataFrame([[contract_months, usage_gb, tickets,login_frequency,days_since_last_login]], 
                                  columns=['Contract Duration (Months)', 'Monthly Usage (GB)', 'Support Tickets','Login Frequency','Days Since Last Login'])
                                  
        # Predict the category (Low, Medium, or High)
        prediction = model.predict(input_data)
        
        # Convert numpy result to Python string
        return str(prediction[0])
        
    except Exception as e:
        print(f"Prediction Error: {e}")
        return "ERROR"

if __name__ == '__main__':
    load_data_and_train()
    test_result = load_and_predict_churn(3, 200, 4)
    print(f"\nTest Input (3 months, 200GB, 4 tickets) predicts Churn Risk: {test_result}")
