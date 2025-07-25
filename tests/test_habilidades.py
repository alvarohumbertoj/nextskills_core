def test_clasificacion_robusta():
    assert clasificar_habilidad("PyThón") == "Programación"
    assert clasificar_habilidad("POWER bi") == "Herramientas BI"
    assert clasificar_habilidad("Scrum master") == "Gestión de proyectos"

