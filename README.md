# 🧠 RetainIQ - AI Driven Loyalty Strategy Predictor
An intelligent hybrid AI system that predicts customer churn risk and recommends personalized retention strategies using Machine Learning and Rule-Based Expert Systems.

## 📌 Key Features
✅ Predicts customer churn risk using ML  
✅ Uses Prolog rules for explainable decision-making  
✅ Hybrid AI system (ML + Expert System)  
✅ User-friendly Tkinter GUI  
✅ Real-time strategy recommendation  
✅ Color-coded risk visualization

## 🏗️ Project Structure
``` bash 
loyalty-strategy-predictor/
│
├── app.py                   # PRIMARY — GUI application (run this)
├── classifier_module.py     # ML model training and prediction
├── rules.pl                 # Prolog knowledge base (diagnosis + treatment rules)
├── churn_classifier.pkl     # Trained model (auto-generated on first run)
├── customer_churn_data.csv  # Training dataset (65 rows)
├── requirements.txt         # Python dependencies
└── README.md
```

## 🔧 Setup & Installation
### Prerequisites
* Python 3.8 or higher
* SWI-Prolog installed on your system

### Step 1 — Install SWI-Prolog

| OS | Command |
| :--- | :--- |
| Ubuntu/Debian | `sudo apt install swi-prolog` |
| macOS | `brew install swi-prolog` |
| Windows | Download from [swi-prolog.org/download](https://www.swi-prolog.org/download) |

### Step 2 — Clone the Repository
```bash
git clone https://github.com/akshitbhatiaGIT/loyalty-strategy-predictor.git
cd loyalty-strategy-predictor
```

### Step 3 — Install Python Dependencies
```bash
pip install -r requirements.txt\
```

## 🚀 How to Run ( GUI )
``` bash
python app.py
```

## 🖥️ Input Features
The system uses 5 key features:

* Contract Duration (Months)
* Monthly Usage (GB)
* Support Tickets
* Login Frequency
* Days Since Last Login

## 🔄 Workflow
* User enters customer details via GUI
* Input validation is performed
* ML model predicts churn risk
* Risk + customer type sent to Prolog
* Prolog infers best strategy
* Results displayed to user  

## 📋 How to Use (Step by Step)
1. Run `python app.py` in your terminal
2. Enter Customer Details
   * Contract Duration (Months)
   * Monthly Usage (GB)
   * Support Tickets
   * Customer Type (New/Existing)
   * Days Since Login
3. Generate Loyalty Strategy using its button
4. View Application Results
   * Churn Risk Level
   * Recommended Strategy
   * Action Plan
5. Modify inputs and enter new details for different scenarios.

## ✨ Example
| Churn Risk | Strategy | Recommendation |
| :--- | :--- | :--- |
| HIGH 🔴 | Service Recovery | Conduct detailed service audit and provide personalized resolution plan. |

## 📸 Screenshots
### 🏠 HomePage
<img width="1489" height="1035" alt="homepage" src="https://github.com/user-attachments/assets/6fe23d5c-9ac4-4e2f-89e7-71fc16640da6" />

### 🔴 High Risk
<img width="1469" height="1040" alt="high_risk" src="https://github.com/user-attachments/assets/22dda9ba-5892-492e-83cd-aab6af5ae928" />

### 🟡 Medium Risk
<img width="1476" height="1035" alt="medium_risk" src="https://github.com/user-attachments/assets/0a5a1750-be91-4108-ad0c-ef98cb72b591" />

### 🟢 Low Risk
<img width="1469" height="1044" alt="low_risk" src="https://github.com/user-attachments/assets/cbb621b2-099f-4447-b639-1fa63da37cb8" />

## 🤖 How It Works
### 1. Application (app.py – GUI)
* A Tkinter-based graphical interface allows user interaction.
* Users input customer details through form fields.
* On clicking the analysis button:
  Inputs are validated, the ML model predicts churn risk, prolog infers strategy
* The system displays results:
  Churn Risk Level (color-coded), Recommended Strategy, Detailed Action Plan

### 2. Machine Learning (classifier_module.py)
* A Random Forest Classifier is trained on labelled customer data to predict churn risk.
* The model uses the following features:
  Contract Duration (Months), Monthly Usage (GB), Support Tickets, Login Frequency, Days Since Last Login
* It classifies customers into three categories:
  Low Risk, Medium Risk, High Risk
The trained model is serialized and stored as churn_classifier.pkl for reuse.

### 3. Prolog System (rules.pl)
* The churn risk predicted by the ML model, along with customer type (New / Existing), is converted into Prolog facts:
  churn_risk/1, customer_type/1
* Inference rules derive one of six predefined strategies:
  aggressive_retention, service_recovery, proactive_engagement, value_reinforcement, maintain_status_quo, review_manually
* Each strategy is mapped to a detailed action plan.
* Facts are retracted and re-asserted per query (fully stateless)

## 📊 Dataset Format
```bash
Contract Duration (Months),Monthly Usage (GB),Support Tickets,Login Frequency,Days Since Last Login,Churn Score
12,50,0,25.7,1,Low
6,120,2,9.4,11,Medium
1,300,5,1.6,47,High
```
65 rows covering the full range.

## 💡 What Makes This Unique
This system combines two AI paradigms rarely seen together in student projects:
* ML handles probabilistic, data-driven risk prediction
* Prolog handles transparent, logical, rule-based diagnosis

This mirrors how real clinical decision support systems are designed — not relying on a single AI approach, but combining the strengths of both.

## 🔮 Future Improvements
* Add more features (adoption rates, payment delay score)
* Deploy as web app (Flask / Steamlit)
* Introduce fourth risk level (Critical)
* Integrate database for dashbord analysis and better prediction

## 📦 Requirements
```bash
pandas
scikit-learn
pyswip
tkinter
```
Install via: `pip install -r requirements.txt`

## 👤 Author
**Author:** Akshit Bhatia
