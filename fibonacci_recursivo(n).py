def fibonacci_recursivo(n):
    # Casos base: F(0) = 0 y F(1) = 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Caso recursivo: F(n) = F(n-1) + F(n-2)
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Permitir que el usuario ingrese el valor
try:
    entrada = input("Ingresa la posición (n) del término de Fibonacci que deseas calcular: ")
    n = int(entrada)
    
    if n < 0:
        print("Por favor, ingresa un número entero positivo o cero.")
    else:
        # Calcular el término n
        resultado = fibonacci_recursivo(n)
        print(f"El término en la posición {n} es: {resultado}")
        
        # Opcional: Generar y mostrar toda la secuencia hasta esa posición
        secuencia = [fibonacci_recursivo(i) for i in range(n + 1)]
        print(f"Secuencia completa hasta la posición {n}: {secuencia}")
        
except ValueError:
    print("Por favor, ingresa un número entero válido.")