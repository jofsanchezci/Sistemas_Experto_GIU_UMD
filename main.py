import tkinter as tk
from tkinter import messagebox
from KnowledgeBase import KnowledgeBase
from Rule import Rule
from ConditionsAndActions import (
    condition_high_risk_investment,
    condition_low_interest_rate,
    condition_high_inflation,
    action_recommend_bonds,
    action_recommend_real_estate,
    action_recommend_gold
)
from InferenceEngine import InferenceEngine

class ExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto para Decisiones Financieras")
        
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)

        self.setup_ui()

    def setup_ui(self):
        # Labels and Entries for Facts
        self.fact_labels = {
            "market_volatility": tk.Label(self.root, text="Volatilidad del mercado (low/medium/high):"),
            "investment_type": tk.Label(self.root, text="Tipo de inversión (stocks/bonds/real_estate):"),
            "interest_rate": tk.Label(self.root, text="Tasa de interés:"),
            "inflation_rate": tk.Label(self.root, text="Tasa de inflación:")
        }
        self.fact_entries = {
            "market_volatility": tk.Entry(self.root),
            "investment_type": tk.Entry(self.root),
            "interest_rate": tk.Entry(self.root),
            "inflation_rate": tk.Entry(self.root)
        }

        row = 0
        for key, label in self.fact_labels.items():
            label.grid(row=row, column=0, sticky=tk.W, pady=2)
            self.fact_entries[key].grid(row=row, column=1, pady=2)
            row += 1

        # Button to Run Inference
        self.run_button = tk.Button(self.root, text="Obtener Recomendación", command=self.run_inference)
        self.run_button.grid(row=row, columnspan=2, pady=10)

        # Textbox for Results
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.grid(row=row+1, columnspan=2, pady=10)

    def run_inference(self):
        # Add facts from entries
        for key, entry in self.fact_entries.items():
            value = entry.get()
            try:
                value = float(value) if key in ["interest_rate", "inflation_rate"] else value
            except ValueError:
                messagebox.showerror("Error de entrada", f"Valor no válido para {key}")
                return
            self.kb.add_fact(key, value)

        # Add rules
        self.kb.add_rule(Rule(condition_high_risk_investment, action_recommend_bonds))
        self.kb.add_rule(Rule(condition_low_interest_rate, action_recommend_real_estate))
        self.kb.add_rule(Rule(condition_high_inflation, action_recommend_gold))

        # Run inference engine and display results
        results = self.engine.run()
        self.result_text.delete(1.0, tk.END)
        if results:
            for result in results:
                self.result_text.insert(tk.END, result + "\n")
        else:
            self.result_text.insert(tk.END, "No hay recomendaciones para los hechos proporcionados.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemApp(root)
    root.mainloop()
