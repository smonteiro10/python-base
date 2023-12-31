#!/usr/bin/env python3
"""Hello Word Multi Linguas.

Dependendo da Lingua configurada no ambiente programa exibe a mensagem
correspondente.

como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""   
__version__ = "0.0.1"
__author__ = "Silas Monteiro"
__licence__ = "Unlicence"
 
import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"  

if current_language == "pt_BR":
    msg = "ola, Mundo!" 
elif current_language == "it_IT":
    msg = "Ciao, Mundo"
elif current_language == "es_SP":
    msg = "Hola, Mundo"
elif current_language ==  "fr_FR":
    msg = "Bonjour Monde"
                

print(msg)
