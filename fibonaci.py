def fibonaci():
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Inicializamos la secuencia con los dos primeros términos
    secuencia = [0, 1]
    
    # Generamos los siguientes términos iterativamente
    for i in range(2, n):
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
        
    return secuencia

# Permitir que el usuario ingrese la cantidad de términos
try:
    entrada = input("¿Cuántos términos de la serie de Fibonacci deseas generar?: ")
    n = int(entrada)
    
    if n < 0:
        print("Por favor, ingresa un número entero positivo o cero.")
    else:
        resultado = fibonaci()
        print(f"Los primeros {n} términos de Fibonacci son: {resultado}")
        
except ValueError:
    print("Por favor, ingresa un número entero válido.")