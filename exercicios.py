from typing import List

# 1. Calcular Média de Valores em uma Lista

def calcular_media(lista_numeros: List[float]) -> float:
    return sum(lista_numeros) / len(lista_numeros)

media = calcular_media([1.5, 2.9, 3.5, 4.2, 5.3, 6.5, 7.8, 8.9, 9.1, 10.48])

print(media)

# 2. Filtrar Dados Acima de um Limite 

def filtrar_dados_acima(dados: List[float], limite: float) -> list[float]:
    
    resultados = []

    for valor in dados:
        if valor > limite:
            resultados.append(valor)
            
    return resultados

resultado = filtrar_dados_acima([1.5, 2.9, 3.5, 4.2, 5.3, 6.5, 7.8, 8.9, 9.1, 10.48, 10.35, 100.35, 545.12, 99.13, 75.29], 40)
print(resultado)

# 3. Contar Valores Únicos em uma lista 

def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))

lista_numeros = contar_valores_unicos([1,2,3,4,4,4,5,5,6,7,8,9,10,11,11,11,12])

print(lista_numeros)

# 4. Converter Celsius para Farenheint em uma lista

def celsius_para_fahrenheit(temperatura_celsius: List[float]) -> float:
    return [1.8 * temp + 32 for temp in temperatura_celsius]

resultado = celsius_para_fahrenheit([35.6, 37.8, 85.4])
print(resultado)





