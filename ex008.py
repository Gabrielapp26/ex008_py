#Desafio 07
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
#sabendo que cada litro de tinta pinta uma área de 2 m²
print("Digite o tamanho da sua parede para saber quantos litros de tinta vai precisar")
l = float(input("Digite a largura: "))
h = float(input("Digite a altura: "))
a = l*h      # a de área
lt = a/2
print("A área da sua parede é {} m² e serão necessários {} litros de tinta para a pintura".format(a, lt))