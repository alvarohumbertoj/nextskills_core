from nextskills_core.habilidades import clasificar_habilidad, sugerir_habilidades, normalizar_habilidad

def test_clasificar_habilidad():
    assert clasificar_habilidad("Python") == "Programación"
    assert clasificar_habilidad("Power BI") == "Visualización de Datos"
    assert clasificar_habilidad("Otra") == "Otras"

def test_sugerir_habilidades():
    assert sugerir_habilidades("Data Science") == ["Python", "SQL", "Machine Learning"]
    assert sugerir_habilidades("No existe") == []

def test_normalizar_habilidad():
    assert normalizar_habilidad(" machine-learning ") == "Machine Learning"
    assert normalizar_habilidad("Power-bi") == "Power Bi"
