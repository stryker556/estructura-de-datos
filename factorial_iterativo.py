def factorial_iterativo(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Permitir que el usuario ingrese el número
try:
    entrada = input("Ingresa un número entero para calcular su factorial: ")
    numero = int(entrada)  # Convertimos el texto ingresado a un número entero
    
    resultado = factorial_iterativo(numero)
    print(f"El factorial de {numero} es: {resultado}")
    
except ValueError:
    print("Por favor, ingresa un número entero válido (sin decimales ni letras).")