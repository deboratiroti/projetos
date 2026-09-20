tipo_de_imovel = input("Informe o seu tipo de imovel (comercial, casa, apartamento): ")
consumo_mensal = float(input("Informe o consumo mensal de agua em m³: "))
if tipo_de_imovel == "comercial":
    print("Tarifa comercial aplicada - consulte o plano corporativo")
elif tipo_de_imovel == "apartamento" and consumo_mensal < 10:
    print("Consumo economico - excelente controle de agua!")
elif tipo_de_imovel == "apartamento" or (tipo_de_imovel == "casa" and consumo_mensal <= 25):
    print("Consumo moderado - dentro do padrao residencial")
else:
    print("Consumo excessivo - adote medidas de economia e verifique vazamentos") 
    