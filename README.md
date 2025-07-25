﻿# nextskills-core

> Librería modular en Python para **clasificación, normalización** y **análisis de habilidades** y **riesgo de automatización**.  
> Diseñada como núcleo funcional del asistente inteligente **NextSkill**.

---

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/tuusuario/nextskills-core.git
cd nextskills-core

# 2. Instala la librería localmente
pip install .
```

---

## Funcionalidades principales

### `habilidades.py`

| Función                  | Descripción                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `clasificar_habilidad()` | Clasifica una habilidad en su categoría (Programación, IA, Herramientas...) |
| `sugerir_habilidades()`  | Sugiere habilidades complementarias por área (Data Science, BI, etc.)       |
| `normalizar_habilidad()` | Limpia y estandariza nombres de habilidades                                |

---

### `riesgo.py`

| Función             | Descripción                                             |
|---------------------|---------------------------------------------------------|
| `calcular_riesgo()` | Evalúa el riesgo de automatización (Bajo, Medio, Alto) |

---

## Cómo ejecutar los tests

```bash
pytest
```

También puedes probar la librería ejecutando el archivo de ejemplo:

```bash
python main.py
```

---

## Estructura del proyecto

```
nextskills-core/
│
├── nextskills_core/
│   ├── habilidades.py
│   ├── riesgo.py
│   └── __init__.py
│
├── tests/
│   ├── test_habilidades.py
│   └── test_riesgo.py
│
├── main.py
├── setup.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Ejemplo de uso

```python
from nextskills_core.habilidades import clasificar_habilidad, normalizar_habilidad
from nextskills_core.riesgo import calcular_riesgo

print(clasificar_habilidad("Python"))         # → Programación
print(normalizar_habilidad(" power-bi "))     # → Power Bi
print(calcular_riesgo(0.7))                   # → Alto
```

---

## Autor

**Álvaro Humberto**  
[alvarohumbertojf@gmail.com](mailto:alvarohumbertojf@gmail.com)  


