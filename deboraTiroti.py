excelente = 0 
ruim = 0 
for i in range(10):
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    print("Opiniao sobre o atendimento: ")
    print("1 - EXCELENTE", "2 - BOM" , "3 - RUIM") 
    opiniao = int(input("Digite a opçao: "))
    if opiniao == 1:
        excelente += 1 
    elif opiniao == 3:
        ruim += 1
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")






