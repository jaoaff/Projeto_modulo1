# Projeto_modulo1
 Este projeto que contém calculadora em python e shell script para linux que executa automaticamente a calculadora no terminal
 
Para isso a ferramenta git deve estar instalada no seu computador caso não esteja basta usar o comando:

"sudo apt-get install git"

Depois basta clonar o projeto usando o comando:

"git clone https://github.com/jaoaff/Projeto_modulo1"

Com isso será possivel rodar essa automação no seu linux basta entrar na pasta do projeto fazendo as devidas alterações de usuario no comando abaixo:

"cd /home/usuario/Projeto_modulo1"

Na sequencia é necessário alterar a premissão do do nosso script shell:

"chmod 755 calc_exe.sh"

Por fim basta exeutar o script:

"./calc_exe,sh"

## Programa python "calculadora.py"

Este programa funciona coletanto 3 informações a nota da primeira e segunda prova e a nota de tabaho, esse inputs estão amarrados em um loop e uma condição, para que a nota possa ser calculada todos os campos devem estar preechidos, sendo assim o laço de repetição vai verificar se tudo foi preenchido e caso isso seja verdadeiro a média pode ser calculada.

verifica_campo = True                                                                                                                                                                      

while verifica_campo == True:
 p1 = input("digite a nota da primeira prova de 0 a 10: ")
 p2 = input("digite a nota da primeira prova de 0 a 10: ")
 trab = input("digite a nota de trbalho de 0 a 10: ")
 if p1 == "" or p2 == "" or trab == "":
 print("Um dos tópicos ficou vazio, preencha novamente")
 continue                                                      

Dada a condição anterior, caso a condição seja falsa sera calculada a média entre as provas e será convertida para peso 7, tepois a nota de trabalho sera convertido para peso 3, depois sera feita a soma e o numero de casas apos a virgula sera limitada para 2, por fim será feita a apresetnação do resultado ao usuário e o loop será interrompido.
 
 else:
  media_convertida = (((float(p1) + float(p2)) / 2) * 7) / 10
  trab_convertido = (float(trab) * 3) / 10
  nota_final = media_convertida + trab_convertido
  nota_final = round(nota_final, 2)
  print("Sua nota final é:", nota_final)
  break 
