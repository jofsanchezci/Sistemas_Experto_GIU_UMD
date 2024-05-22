# Ejemplo de condiciones
def condition_high_risk_investment(facts):
    return facts.get('market_volatility') == 'high' and facts.get('investment_type') == 'stocks'

def condition_low_interest_rate(facts):
    return facts.get('interest_rate') < 2.0

def condition_high_inflation(facts):
    return facts.get('inflation_rate') > 3.0

# Ejemplo de acciones
def action_recommend_bonds(facts):
    print("Recomendación: Considerar invertir en bonos debido a la alta volatilidad del mercado.")

def action_recommend_real_estate(facts):
    print("Recomendación: Considerar invertir en bienes raíces debido a las bajas tasas de interés.")

def action_recommend_gold(facts):
    print("Recomendación: Considerar invertir en oro debido a la alta inflación.")
