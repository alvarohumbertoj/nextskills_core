# nextskills_core/riesgo.py

def calcular_riesgo(valor):
    if valor < 0.4:
        return "Bajo"
    elif valor < 0.7:
        return "Medio"
    else:
        return "Alto"