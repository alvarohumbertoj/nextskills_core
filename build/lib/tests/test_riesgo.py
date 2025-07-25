from nextskills_core.riesgo import calcular_riesgo

def test_calcular_riesgo():
    assert calcular_riesgo(0.3) == "Bajo"
    assert calcular_riesgo(0.5) == "Medio"
    assert calcular_riesgo(0.8) == "Alto"
