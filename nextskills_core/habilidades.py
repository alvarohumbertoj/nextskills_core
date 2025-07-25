import re

def clasificar_habilidad(habilidad):
    habilidad = habilidad.lower().strip()

    if re.search(r'py|python|r\b|sql|scala', habilidad):
        return 'Programación'
    elif re.search(r'ia|inteligencia artificial|machine learning|deep learning', habilidad):
        return 'Inteligencia Artificial'
    elif re.search(r'power\s*bi|excel|tableau|looker|dashboards?', habilidad):
        return 'Herramientas BI'
    elif re.search(r'nube|azure|aws|gcp|cloud', habilidad):
        return 'Cloud Computing'
    elif re.search(r'gestion|scrum|kanban|jira', habilidad):
        return 'Gestión de proyectos'
    else:
        return 'Otra'
