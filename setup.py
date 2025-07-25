from setuptools import setup, find_packages

setup(
    name='nextskills-core',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # Aquí irían dependencias externas si las hubiera
    description='Librería base de funciones del asistente NextSkill',
    author='Álvaro Humberto',
    author_email='tucorreo@ejemplo.com',
    url='https://github.com/TUUSUARIO/nextskills-core',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

