def factorial_recursivo(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    # Caso base: 0! y 1! son iguales a 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    return n * factorial_recursivo(n - 1)

# Permitir que el usuario ingrese el número
try:
    entrada = input("Ingresa un número entero para calcular su factorial (versión recursiva): ")
    numero = int(entrada)
    
    resultado = factorial_recursivo(numero)
    print(f"El factorial de {numero} es: {resultado}")
    
except ValueError as e:
    print(f"Por favor, ingresa un número entero válido y no negativo. (Detalle: {e})")5