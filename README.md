# 🧠 RetainIQ - AI Driven Loyalty Strategy Predictor
An intelligent hybrid AI system that predicts customer churn risk and recommends personalized retention strategies using Machine Learning and Rule-Based Expert Systems.

## 📌 Key Features
✅ Predicts customer churn risk using ML  
✅ Uses Prolog rules for explainable decision-making  
✅ Hybrid AI system (ML + Expert System)  
✅ User-friendly Tkinter GUI  
✅ Real-time strategy recommendation  
✅ Color-coded risk visualization
AIML-PROJECT/
│
├── app_cli.py          # PRIMARY — CLI application (run this)
├── app.py               # BONUS  — GUI version (optional)
├── classifier_model.py  # ML model training and prediction
├── rules.pl             # Prolog knowledge base (diagnosis + treatment rules)
├── risk_classifier.pkl  # Trained model (auto-generated on first run)
├── symptoms_data.csv    # Training dataset (190 rows)
├── requirements.txt     # Python dependencies
└── README.md

## 🏗️ Project Structure
loyalty-strategy-predictor/
│

├── app.py                   # PRIMARY — GUI application (run this)
├── classifier_module.py     # ML model training and prediction
├── rules.pl                 # Prolog knowledge base (diagnosis + treatment rules)
├── churn_classifier.pkl     # Trained model (auto-generated on first run)
├── customer_churn_data.csv  # Training dataset (65 rows)
├── requirements.txt         # Python dependencies
└── README.md

## 🔧 Setup & Installation
### Prerequisites
* Python 3.8 or higher
* SWI-Prolog installed on your system

### Step 1 — Install SWI-Prolog
OS	Command
Ubuntu/Debian	sudo apt install swi-prolog
macOS	brew install swi-prolog
Windows	Download from https://www.swi-prolog.org/download
Step 2 — Clone the Repository
git clone https://github.com/KHUSH241/AIML-PROJECT.git
cd AIML-PROJECT
Step 3 — Install Python Dependencies
pip install -r requirements.txt
