print("-------------------------------------------------")
print("|	            ATIVIDADE 1	     	      	|")
print("-------------------------------------------------")
print ("|Nome do Aluno: Yuri")
print ("|Nome do Aluno: Gabriel")
print ("|Nome do Aluno: Maik")
print ("|Nome do Aluno: André")
print("-------------------------------------------------")
print ("|Escolha um smartphone                          |")
print("-------------------------------------------------")
print ("|1 - SAMSUNG S11")
print ("|2 - MOTOROLA G8")
print ("|3 - Iphone 12")
print("-------------------------------------------------")
marca = float (input ("|Escolha a opção de smartphone:                 |"))
print("-------------------------------------------------")

if marca == 1:
    precoBase = 1199.99
    descVista = 0.05
    taxaJuros = 0.10
elif marca == 2:
        precoBase = 1350.50
        descVista = 0.07
        taxaJuros = 0.03
elif marca ==3:
        precoBase = 3299.99
        descVista = 0.10
        taxaJuros = 0.20
else:
    print ("Você escolheu digitar os dados!")
    precoBase  =  float(input ("o preço base do smartphone"))
    descVista  =  float(input ("a taxa de desconto à vista"))
    taxaJuros  =  float(input ("a taxa de juros"))
forma = input ("a forma de pagamento a vista ou parcelado (V ou P)")
print (precoBase)

if forma ==  "V":
    valorDesc = precoBase * descVista
    precoFinal = precoBase = valorDesc
    print (precoFinal, "a vista")
 
elif forma == "P":
        qtdParc = float (input ("a quantidade de parcelas"))

else qtdParc < 10:
    precoFinal = precoBase
    valorParc = precoFinal / qtdParc
    print (precoFinal, "parcelado sem juros")

if:
    valorJuros = precoBase * taxaJuros
    precoFinal = precoBase + valorJuros
    valorParc = precoFinal / qtdParc
    print (precoFinal, "parcelado com juros")

    print ("O Valor das parcelas serão", valorParc)

    print ("|| Nenhuma forma de pagamento foi selecionada! ||")

    print ("Fim da execução do programa!")
