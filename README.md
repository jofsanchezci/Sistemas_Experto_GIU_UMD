
# Sistema Experto para Decisiones Financieras

Este proyecto es una implementación básica de un sistema experto para ayudar a tomar decisiones en el sector financiero. Utiliza reglas simples del tipo "si-entonces" para evaluar situaciones financieras y proporcionar recomendaciones. También incluye una interfaz gráfica de usuario utilizando `tkinter`.

## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos:

1. `KnowledgeBase.py` - Implementa la base de conocimientos.
2. `Rule.py` - Define las reglas con condiciones y acciones.
3. `ConditionsAndActions.py` - Contiene ejemplos de condiciones y acciones específicas para el dominio financiero.
4. `InferenceEngine.py` - Implementa el motor de inferencia.
5. `Main.py` - Aplicación principal que configura y ejecuta el sistema experto con una interfaz gráfica de usuario.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/sistema-experto-finanzas.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd sistema-experto-finanzas
    ```
3. Asegúrate de tener Python instalado en tu sistema. Este proyecto utiliza `tkinter` para la interfaz gráfica, que viene incluido con Python.

## Uso

### 1. Base de Conocimientos (KnowledgeBase.py)
```python
class KnowledgeBase:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, key, value):
        self.facts[key] = value

    def add_rule(self, rule):
        self.rules.append(rule)

    def evaluate(self):
        results = []
        for rule in self.rules:
            result = rule.evaluate(self.facts)
            if result:
                results.append(result)
        return results
```

### 2. Regla (Rule.py)
```python
class Rule:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def evaluate(self, facts):
        if self.condition(facts):
            return self.action(facts)
        return None
```

### 3. Condiciones y Acciones (ConditionsAndActions.py)
```python
# Ejemplo de condiciones
def condition_high_risk_investment(facts):
    return facts.get('market_volatility') == 'high' and facts.get('investment_type') == 'stocks'

def condition_low_interest_rate(facts):
    return facts.get('interest_rate') < 2.0

def condition_high_inflation(facts):
    return facts.get('inflation_rate') > 3.0

# Ejemplo de acciones
def action_recommend_bonds(facts):
    return "Recomendación: Considerar invertir en bonos debido a la alta volatilidad del mercado."

def action_recommend_real_estate(facts):
    return "Recomendación: Considerar invertir en bienes raíces debido a las bajas tasas de interés."

def action_recommend_gold(facts):
    return "Recomendación: Considerar invertir en oro debido a la alta inflación."
```

### 4. Motor de Inferencia (InferenceEngine.py)
```python
class InferenceEngine:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def run(self):
        return self.knowledge_base.evaluate()
```

### 5. Aplicación Principal con Interfaz Gráfica (Main.py)
```python
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
```

## Ejecución

Para ejecutar la aplicación, asegúrate de estar en el directorio del proyecto y ejecuta:

```bash
python Main.py
```

Esto abrirá una interfaz gráfica donde puedes ingresar los valores para los hechos y obtener recomendaciones basadas en las reglas definidas.

## Extensiones y Mejoras

- **Agregar más hechos y reglas:** Puedes extender la base de conocimientos añadiendo más hechos y reglas relevantes para el dominio financiero.
- **Interfaz de usuario:** Mejorar la interfaz gráfica para hacerla más intuitiva y amigable.
- **Subsistema de explicación:** Añadir un subsistema que explique cómo se llegó a una conclusión o recomendación.

## Contribuciones

Si deseas contribuir a este proyecto, por favor, realiza un fork del repositorio y envía un pull request con tus mejoras.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
