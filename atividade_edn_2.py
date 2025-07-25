#=================================
# ATIVIDADE PRÁTICA 02 - EDN
#=================================


# 1) Conversor de Moeda
print("\n" + "="*60 + "\n")
print("ATIVIDADE 01: Conversor de Moedas" + "\n")

reais = 100
tx_dolar = 5.20
tx_euro = 6.15
dolares = reais/tx_dolar
euros = reais/tx_euro

print(f"Valor em reais: R$ {reais:.2f}")
print(f"R$ {reais}.00 equivalem à US$ {dolares:.2f}")
print(f"R$ {reais}.00 equivalem à € {euros:.2f} ")
print("\n" + "="*60 + "\n")

# 2) Calculadora de Desconto
print("ATIVIDADE 02: Calculadora de Desconto" + "\n")

nome_produto = "Camiseta"
preco_original = 50
desconto_percentual = 20
valor_desconto = preco_original*(desconto_percentual/100)
preco_final = preco_original - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}% = R$ {valor_desconto:.2f}")
print(f"Preço com desconto: R$ {preco_final:.2f}")
print("\n" + "="*60 + "\n")


# 3) Calculadora de Média Escolar

print("ATIVIDADE 03: Calculadora de Média Escolar" + "\n")

nota1 = 7.5
nota2 = 8
nota3 = 6.5
media = (nota1 + nota2 + nota3)/3

print(f"Nota 1: {nota1:.1f}")
print(f"Nota 2: {nota2:.1f}")
print(f"Nota 3: {nota3:.1f}")
print(f"Média: {media:.2f}")
print("\n" + "="*60 + "\n")

# 4) Calculadora de Consumo de Combustível
print("ATIVIDADE 04: Calculadora de Consumo de Combustível" + "\n")

distancia_percorrida = 300
gasto_combustivel = 25 
consumo_medio = distancia_percorrida / gasto_combustivel


print("-> Dados da viagem" + "\n")
print(f"Distância percorrida: {distancia_percorrida} Km")
print(f"Combustível gasto: {gasto_combustivel} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
print("\n" + "="*60 + "\n")

