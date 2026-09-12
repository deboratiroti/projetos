valor = float(input("Digite o valor total da compra: R$ "))
#if verifica a primeira condição
if valor < 200:
   desconto = 0.05
#elif verifica outra condição
elif valor < 300:
    desconto = 0.10
#else executa quando nenhuma condiçao anterior é verdadeira
else: 
    desconto = 0.15
valor_desconto = valor * desconto
valor_final = valor - valor_desconto
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")