import math

def calcular_area_circulo(raio):
    return math.pi * raio**2

def calcular_area_quadrado(lado):
    return lado * lado

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

raio = 9
lado_quadrado = 10
base_triangulo = 4
altura_triangulo = 8

area_circulo = calcular_area_circulo(raio)
area_quadrado = calcular_area_quadrado(lado_quadrado)
area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)

print(f"Área do círculo com raio {raio}: {area_circulo}")
print(f"Área do quadrado com lado {lado_quadrado}: {area_quadrado}")
print(f"Área do triângulo com base {base_triangulo} e altura {altura_triangulo}: {area_triangulo}")
