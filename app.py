import tkinter as tk
from tkinter import ttk, messagebox
import os
from pyswip import Prolog 

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Import the core logic function
from classifier_module import load_and_predict_churn, load_data_and_train

# --- 0. Initial Setup ---
if not os.path.exists(os.path.join(SCRIPT_DIR, 'churn_classifier.pkl')):
    print("Initial run detected. Training the Classification Model...")
    # Attempt to train the model on startup if the pkl file is missing
    load_data_and_train()

try:
    # Initialize Prolog engine and load rules
    prolog = Prolog()
    prolog.consult(os.path.join(SCRIPT_DIR, "rules.pl"))
    PROLOG_READY = True
except Exception as e:
    PROLOG_READY = False
    print(f"Prolog Initialization Error. Ensure SWI-Prolog is installed correctly. Error: {e}")


def run_analysis():
    """Handles input, ML prediction, and Prolog inference for strategy."""
    if not PROLOG_READY:
        messagebox.showerror("Setup Error", "Prolog engine failed to start. Ensure SWI-Prolog is installed correctly.")
        return
        
    try:
        # Inputs
        contract = float(contract_entry.get())
        usage = float(usage_entry.get())
        tickets = float(tickets_entry.get())
        customer_type = customer_var.get().lower()
        logins=float(login_entry.get())
        days_since=float(days_entry.get())

        if contract <= 0 or usage <= 0 or tickets < 0 or logins < 0 or days_since < 0 or customer_type not in ['new', 'existing']:
            messagebox.showerror("Input Error", "Please enter valid, non-zero numbers and select a customer type.")
            return

        # ----------------------------------------------------------------
        # --- Module 1: ML Classification (Churn Risk) 
        # ----------------------------------------------------------------
        churn_risk_category = load_and_predict_churn(contract, usage, tickets,logins,days_since)
        
        churn_risk_category = str(churn_risk_category).strip()
        churn_text.set(f"ML CHURN RISK: {churn_risk_category.upper()}")
        
        # Define colors for risk
        if churn_risk_category.lower() == 'high':
            churn_label.config(foreground="#FF6B6B")  # Red
        elif churn_risk_category.lower() == 'medium':
            churn_label.config(foreground="#FFB84D")  # Orange
        else:
            churn_label.config(foreground="#51CF66")  # Green

        # ----------------------------------------------------------------
        # --- Module 2: Prolog Strategy
        # ----------------------------------------------------------------
        
        # 1. Retract previous facts using simple string-based retractall
        prolog.retractall("churn_risk(_)")
        prolog.retractall("customer_type(_)")
        
        # 2. Assert new facts based on Python inputs
        # Convert to lowercase for Prolog atoms
        churn_risk_lower = churn_risk_category.lower()
        prolog.assertz(f"churn_risk({churn_risk_lower})")
        prolog.assertz(f"customer_type({customer_type})")

        # 3. Query the Prolog knowledge base for the strategy
        query = prolog.query("get_strategy(S, R)")
        result = list(query)
        query.close()

        if result:
            try:
                # Extract Prolog query results
                strategy_val = result[0]['S']
                recommendation_val = result[0]['R']
                
                # Safely convert to string using atom_string if available, otherwise str()
                if hasattr(strategy_val, 'value'):
                    strategy = strategy_val.value
                else:
                    strategy = str(strategy_val)
                
                if hasattr(recommendation_val, 'value'):
                    recommendation = recommendation_val.value
                else:
                    recommendation = str(recommendation_val)
                
                # Formatting
                strategy = strategy.strip("'\"").replace('_', ' ').title()
                recommendation = recommendation.strip("'\"")
                
                strategy_text.set(f"Strategy: {strategy}")
                recommendation_text.set(recommendation)
            except Exception as e:
                strategy_text.set("Strategy: ERROR")
                recommendation_text.set(f"Error processing Prolog result: {e}")
                print(f"Prolog result processing error: {e}")
                import traceback
                traceback.print_exc()
        else:
            strategy_text.set("Strategy: UNKNOWN")
            recommendation_text.set("Prolog rules could not determine a loyalty strategy.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except Exception as e:
        messagebox.showerror("System Error", f"An unexpected error occurred: {e}")


# ----------------------------------------------------
# --- Tkinter GUI 
# ----------------------------------------------------

root = tk.Tk()
root.title("RetainIQ - AI Loyalty Strategy Expert System")
root.geometry("1200x1000")
root.resizable(False, False)
BG_PRIMARY = "#0F1419"    
BG_SECONDARY = "#1A1F2E"  
FG_TEXT = "#E8EAED"       
ACCENT_PRIMARY = "#00D4FF"  
ACCENT_BUTTON = "#12E5B2"  
ACCENT_HOVER = "#FF6B6B"    
ACCENT_WARNING = "#FFB84D"  
ACCENT_SUCCESS = "#51CF66"  

root.config(bg=BG_PRIMARY)

style = ttk.Style()
style.theme_create("ModernTheme", parent="alt", settings={
    "TFrame": {"configure": {"background": BG_PRIMARY}},
    "TLabel": {"configure": {"background": BG_PRIMARY, "foreground": FG_TEXT}},
    "TEntry": {"configure": {"fieldbackground": BG_SECONDARY, "foreground": FG_TEXT, "padding": 5}},
    "TMenubutton": {"configure": {"background": BG_SECONDARY, "foreground": FG_TEXT}},
    "TButton": {
        "configure": {
            "background": ACCENT_BUTTON,
            "foreground": BG_PRIMARY,
            "font": ('Segoe UI', 12, 'bold'),
            "padding": 12,
            "relief": "flat",
            "borderwidth": 0
        },
        "map": {
            "background": [("active", "#0DA88E"), ("!disabled", ACCENT_BUTTON)],
        }
    }
})
style.theme_use("ModernTheme")

# Main container
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=20, pady=20)
header_frame = ttk.Frame(main_frame)
header_frame.pack(fill='x', pady=(0, 20))

ttk.Label(header_frame, text="🤖 RetainIQ - AI Loyalty Advisor", 
          font=('Segoe UI', 24, 'bold'), foreground=ACCENT_PRIMARY).pack(anchor='w')
ttk.Label(header_frame, text="Intelligent Customer Retention Strategy",
          font=('Segoe UI', 12), foreground="#888").pack(anchor='w', pady=(2, 0))

# Input Section
input_label = ttk.Label(main_frame, text="📊 Customer Information",
                        font=('Segoe UI', 13, 'bold'), foreground=ACCENT_PRIMARY)
input_label.pack(anchor='w', pady=(15, 10))

input_frame = tk.Frame(main_frame, bg=BG_SECONDARY, highlightthickness=1, highlightbackground="#333")
input_frame.pack(fill='x', pady=(0, 20))

fields = [
    ("Contract Duration (Months):", "6", contract_entry := ttk.Entry(input_frame, width=28, font=('Arial', 11))),
    ("Monthly Usage (GB):", "150", usage_entry := ttk.Entry(input_frame, width=28, font=('Arial', 11))),
    ("Support Tickets (Past 3M):", "3", tickets_entry := ttk.Entry(input_frame, width=28, font=('Arial', 11))),
    ("Customer", "12", login_entry := ttk.Entry(input_frame, width=28, font=('Arial', 11))),
    ("Days Since Last Login:", "10", days_entry := ttk.Entry(input_frame, width=28, font=('Arial', 11))),
]

for idx, (label_text, default_val, entry_widget) in enumerate(fields):
    label = ttk.Label(input_frame, text=label_text, font=('Segoe UI', 11), background=BG_SECONDARY)
    label.grid(row=idx, column=0, sticky='w', padx=15, pady=10)
    entry_widget.insert(0, default_val)
    entry_widget.grid(row=idx, column=1, sticky='ew', padx=15, pady=10)

# Customer Type
ttk.Label(input_frame, text="Customer Type:", font=('Segoe UI', 11), background=BG_SECONDARY).grid(
    row=3, column=0, sticky='w', padx=15, pady=10)
customer_var = tk.StringVar(root)
customer_var.set("Existing")
customer_dropdown = ttk.OptionMenu(input_frame, customer_var, "Existing", "New", "Existing")
customer_dropdown.grid(row=3, column=1, sticky='ew', padx=15, pady=10)

input_frame.grid_columnconfigure(1, weight=1)

# Analyze Button
analyze_button = tk.Button(main_frame, text="🚀 Generate Loyalty Strategy", 
                           command=run_analysis, font=('Segoe UI', 12, 'bold'),
                           bg=ACCENT_BUTTON, fg=BG_PRIMARY, 
                           relief='flat', bd=0, padx=20, pady=12, cursor='hand2',
                           activebackground="#0DA88E")
analyze_button.pack(fill='x', pady=(15, 25))

# Results Section with Frame
result_label = ttk.Label(main_frame, text="📈 Analysis Results",
                        font=('Segoe UI', 13, 'bold'), foreground=ACCENT_PRIMARY)
result_label.pack(anchor='w', pady=(15, 10))

result_frame = tk.Frame(main_frame, bg=BG_SECONDARY, highlightthickness=1, highlightbackground="#333")
result_frame.pack(fill='both', expand=True)

# ML Churn Risk
churn_header = tk.Label(result_frame, text="📊 ML Churn Risk Assessment", 
                       font=('Segoe UI', 11, 'bold'), bg=BG_SECONDARY, fg=ACCENT_PRIMARY)
churn_header.pack(anchor='w', padx=15, pady=(12, 5))

churn_text = tk.StringVar(value="[Awaiting Input]")
churn_label = tk.Label(result_frame, textvariable=churn_text, 
                       font=('Segoe UI', 13, 'bold'), bg=BG_SECONDARY, fg=ACCENT_WARNING)
churn_label.pack(anchor='w', padx=15, pady=(0, 12))

# Recommended Strategy
strategy_header = tk.Label(result_frame, text="💡 Recommended Strategy",
                          font=('Segoe UI', 11, 'bold'), bg=BG_SECONDARY, fg=ACCENT_PRIMARY)
strategy_header.pack(anchor='w', padx=15, pady=(12, 5))

strategy_text = tk.StringVar(value="[Awaiting Input]")
strategy_label = tk.Label(result_frame, textvariable=strategy_text,
                         font=('Segoe UI', 12, 'bold'), bg=BG_SECONDARY, fg=ACCENT_SUCCESS)
strategy_label.pack(anchor='w', padx=15, pady=(0, 12))

# Action Plan
action_header = tk.Label(result_frame, text="✅ Action Plan",
                        font=('Segoe UI', 11, 'bold'), bg=BG_SECONDARY, fg=ACCENT_PRIMARY)
action_header.pack(anchor='w', padx=15, pady=(12, 5))

recommendation_text = tk.StringVar(value="The specific recommendation from the expert system will appear here.")
recommendation_label = tk.Label(result_frame, textvariable=recommendation_text, 
                               wraplength=600, justify='left', font=('Segoe UI', 10),
                               bg=BG_SECONDARY, fg=FG_TEXT)
recommendation_label.pack(anchor='w', padx=15, pady=(0, 15))

root.mainloop()
