# nextskills_core/habilidades.py

HABILIDADES = {
    "Python": "Programación",
    "SQL": "Bases de Datos",
    "Excel": "Herramientas",
    "Machine Learning": "Inteligencia Artificial",
    "Power BI": "Visualización de Datos"
}

COMPLEMENTARIAS = {
    "Data Science": ["Python", "SQL", "Machine Learning"],
    "Marketing Digital": ["SEO", "Google Ads", "Analytics"],
    "Business Intelligence": ["Power BI", "Excel", "SQL"]
}

def clasificar_habilidad(habilidad):
    return HABILIDADES.get(habilidad, "Otras")

def sugerir_habilidades(area):
    return COMPLEMENTARIAS.get(area, [])

def normalizar_habilidad(habilidad):
    return habilidad.strip().lower().replace("-", " ").title()