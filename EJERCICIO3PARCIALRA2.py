texto = input("INGRESE UNA CADENA DE TEXTO:")
textoMayus = texto.upper()

longitud = len(texto)

tienepython = "Python" in texto

print(f"texto en mayusculas: {textoMayus}")
print(f"Número de caracteres: {longitud}")
print(f"Si esta la palabra PYTHON: {tienepython}")

