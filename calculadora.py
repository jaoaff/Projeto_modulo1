#-------------------calculadora--------------------------------------------

verifica_campo = True




while verifica_campo == True:

  #Entradas de dados:

  p1 = input("digite a nota da primeira prova de 0 a 10: ")
  p2 = input("digite a nota da primeira prova de 0 a 10: ")
  trab = input("digite a nota de trbalho de 0 a 10: ")


  #---------------------cálculos---------------------------------------------

  if p1 == "" or p2 == "" or trab == "":
    print("Um dos tópicos ficou vazio, preencha novamente")
    continue

  else:
    #calcula a média e já converte para peso 7

    media_convertida = (((float(p1) + float(p2)) / 2) * 7) / 10

    #converte a nota de trabalho para média final com peso 3

    trab_convertido = (float(trab) * 3) / 10


    nota_final = media_convertida + trab_convertido

    nota_final = round(nota_final, 2)



    #-------------------devolutiva---------------------------------------------

    print("Sua nota final é:", nota_final)

    break