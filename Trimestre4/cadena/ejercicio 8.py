# Determinar en que tiempo esta conjugado un verbo
from pattern.es import conjugate

verbo =  "hablar"
conjugacion = conjugate(verbo, tense="present", person=3, mood="indicative")

if conjugacion is not None:
    print(f"El verbo '{verbo}' está conjugado en '{conjugacion}'.")
else:
    print(f"El verbo '{verbo}' no está conjugado.")


#pip install pattern para instalar libreria 