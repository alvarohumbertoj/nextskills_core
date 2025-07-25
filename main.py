# main.py

from nextskills_core.habilidades import clasificar_habilidad, sugerir_habilidades, normalizar_habilidad
from nextskills_core.riesgo import calcular_riesgo

print("📚 Clasificación de habilidades:")
print("Python →", clasificar_habilidad("Python"))
print("Excel →", clasificar_habilidad("Excel"))
print("Blockchain →", clasificar_habilidad("Blockchain"))

print("\n🔁 Sugerencias de habilidades:")
print("Data Science →", sugerir_habilidades("Data Science"))
print("Marketing Digital →", sugerir_habilidades("Marketing Digital"))

print("\n🧹 Normalización de habilidades:")
print("'machine-learning' →", normalizar_habilidad("machine-learning"))
print("' Power-bi ' →", normalizar_habilidad(" Power-bi "))

print("\n🤖 Cálculo de riesgo de automatización:")
print("0.25 →", calcular_riesgo(0.25))
print("0.65 →", calcular_riesgo(0.65))
print("0.9 →", calcular_riesgo(0.9))

