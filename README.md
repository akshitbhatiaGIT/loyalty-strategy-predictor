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
git clone https://github.com/KHUSH241/AIML-PROJECT.git
cd AIML-PROJECT
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
## Example
## 📸 Screenshots
## 🤖 How It Works
## 📊 Dataset Format
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
pwswip
tkinter
```
Install via: `pip install -r requirements.txt`

## 👤 Author
**Author:** Akshit Bhatia
