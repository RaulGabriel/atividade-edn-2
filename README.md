# Atividade Prática - 02
Esta atividade reúne quatro scripts simples desenvolvidos em Python, como parte das propostas práticas do curso da Escola da Nuvem (EDN). O objetivo é exercitar fundamentos básicos da programação de forma prática e direta.

---
# 1. Conversor de Moeda

**Objetivo:** Criar um programa que converte um valor em reais para dólares e euros.

```python
reais = 100
tx_dolar = 5.20
tx_euro = 6.15
dolares = reais/tx_dolar
euros = reais/tx_euro

print(f"Valor em reais: R$ {reais:.2f}")
print(f"R$ {reais}.00 equivalem à US$ {dolares:.2f}")
print(f"R$ {reais}.00 equivalem à € {euros:.2f} ")
```
# 2. Calculadora de Desconto

**Objetivo:** Desenvolver um programa que calcula o desconto em uma loja.
```python
nome_produto = "Camiseta"
preco_original = 50
desconto_percentual = 20
valor_desconto = preco_original*(desconto_percentual/100)
preco_final = preco_original - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}% = R$ {valor_desconto:.2f}")
print(f"Preço com desconto: R$ {preco_final:.2f}")
```
# 3. Calculadora de Média Escolar
**Objetivo:** Criar um programa que calcula a média escolar de um aluno.
```python
nota1 = 7.5
nota2 = 8
nota3 = 6.5
media = (nota1 + nota2 + nota3)/3

print(f"Nota 1: {nota1:.1f}")
print(f"Nota 2: {nota2:.1f}")
print(f"Nota 3: {nota3:.1f}")
print(f"Média: {media:.2f}")
```

# 4. Calculadora de Consumo de Combustível
**Objetivo:** Desenvolver um programa que calcula o consumo médio de combustível de um veículo.
```python
distancia_percorrida = 300
gasto_combustivel = 25 
consumo_medio = distancia_percorrida / gasto_combustivel

print(f"Distância percorrida: {distancia_percorrida} Km")
print(f"Combustível gasto: {gasto_combustivel} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
```
