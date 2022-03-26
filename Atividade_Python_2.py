#variaveis lista e dicionario
celulares_lista = [('SAMSUNG S11', 1199.99,), ('MOTOROLA G8', 1350.50,), ('Iphone 12', 3299.99,)]
vendedor  = {'vt':0,'av':0 , 'co':0, '1v': 'Ayrton','co1':0, '2v': 'Emerson', 'co2':0, '3v': 'Nelson', 'co3':0, '4v': 'Rubens', 'co4':0, '5v': 'Felipe', 'co5':0, 's': 0, 'm':0, 'i':0 }

#inicio
print("=================================================")
print(" 	            ATIVIDADE 2	     	      	 ")
print("-------------------------------------------------")
print (" Nome do Aluno: André Goulart RA: 739712         ")
print (" Nome do Aluno: Bruno Kenzo   RA: 740525         ")
print (" Nome do Aluno: Gabriel Lima  RA: 740560         ")
print (" Nome do Aluno: Yuri Oliveira RA: 740707         ")
print("-------------------------------------------------")
marca = 0
#laço_while
while marca != 4:

    print("-------------------------------------------------")
    print ("          FECHAMENTO DO DIA - TELA INICIAL            ")
    print("-------------------------------------------------")
    print ("             1 - SAMSUNG S11                   ")
    print ("             2 - MOTOROLA G8                   ")
    print ("             3 - Iphone 12                     ")
    print ("             4 - Total do dia                  ")
    print("-------------------------------------------------")

    #cellfone
    marca = int(input(" Digite sua escolha ...................: "))
    if marca == 1:
        nomeC     = celulares_lista[0][0]
        precoBase = celulares_lista[0][1]
        qtdv      = vendedor['s'] + 1
        vendedor['s']  = qtdv
    elif marca == 2:
        nomeC     = celulares_lista[1][0]
        precoBase = celulares_lista[1][1]
        qtdv      = vendedor['m'] + 1
        vendedor['m']  = qtdv
    elif marca ==3:
        nomeC     = celulares_lista[2][0]
        precoBase = celulares_lista[2][1]
        qtdv      = vendedor['i'] + 1 
        vendedor['i']  = qtdv
    elif marca == 4:
        break

    #vendedor
    v = float(input(" Digite o código de vendedor...........: "))
    if v == 1:
        nome = vendedor['1v']
        comissao = vendedor['co1']
    elif v == 2:
        nome = vendedor['2v']
        comissao = vendedor['co2']
        vendedor['co2'] = comissao
    elif v == 3:
        nome = vendedor['3v']
        comissao = vendedor['co3']
        vendedor['co3'] = comissao
    elif v == 4:
        nome = vendedor['4v']
        comissao = vendedor['co4']
        vendedor['co4'] = comissao
    elif v == 5:
        nome = vendedor['5v']
        comissao = vendedor['co5']
        vendedor['co5'] = comissao
    else:
        print("=================================================")
        print('*****')
        print('*****       CÓDIGO DE VENDEDOR INCORRETO!  ******')
        print('*****           VENDA NÃO REGISTRADA!      ******')
        print('*****')
        print("=================================================")
        break
        
        
        

    #Escolha de pagamento
    forma = input (" Pagamento [V] à Vista ou [P] Parcelado: ").upper()
    print("-------------------------------------------------")
  
    #Condição de pagamento
    if forma ==  "V":
        descVista = int(input('Porcentagem do desconto à vista:  '))
        descVista = descVista / 100
        valorDesc = precoBase * descVista
        precoFinal = precoBase - valorDesc
        print("Preço base ...............: R$ {:.2f}".format(precoBase))
        print('Desconto .................: R${:.2f}'.format(valorDesc))
        print("Venda à vista ............: R${:.2f}" .format(precoFinal))  
        comissao = precoBase * 0.05
        vendedor['co'] = vendedor['co'] + comissao
        vendedor['vt'] = vendedor['vt'] + precoFinal
        vendedor['av'] = vendedor['av'] + precoFinal
        print("-------------------------------------------------")
        print('*****')
        print('*****  VENDA REGISTRADA #',vendedor['s']+ vendedor['m']+vendedor['i'], nomeC)
        print('*****  VENDEDOR', nome, '- COMISSÃO: R$ {:.2f}'.format(comissao)) 
        print('*****')
        print("=================================================")
    elif forma == "P":
        qtdParc = 6
        precoFinal = precoBase
        valorParc = precoFinal / qtdParc
        print ("6 parcelas de R${:.2f} totalizando R${:.2f}".format(valorParc, precoFinal))
        comissao = precoBase * 0.05
        vendedor['co'] = vendedor['co'] + comissao
        vendedor['vt'] = vendedor['vt'] + precoFinal
        print("-------------------------------------------------")
        print('*****')
        print('*****  VENDA REGISTRADA #',vendedor['s']+ vendedor['m']+vendedor['i'], nomeC)
        print('*****  VENDEDOR ', nome, '- COMISSÃO: R$ {:.2f}'.format(comissao))
        print('*****')
        print("=================================================")

   
print("-------------------------------------------------")
print ("               TOTALIZAÇÃO DO DIA                  ")
print("-------------------------------------------------")
print('Quantidade total de Smartphones vendidos: ',vendedor['s']+ vendedor['m']+vendedor['i'])
print('Quantidade vendida de SAMSUNG S11 ......: ', vendedor['s'])
print('Quantidade vendida de MOTOROLA G8 ......: ', vendedor['m'])
print('Quantidade vendida de IPHONE 12 ........: ', vendedor['i'])
print("-------------------------------------------------")
print('Soma total das vendas .....: R${:.2f}'.format(vendedor['vt']))
print('Soma das vendas à vista ...: R${:.2f}'.format(vendedor['av']))
print('Soma total paga de comissão: R${:.2f}'.format(vendedor['co']))
print("-------------------------------------------------")