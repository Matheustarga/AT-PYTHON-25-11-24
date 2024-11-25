num_positivos = []

while True :
  number = int(input("Informe o número que deseja colocar na lista(para sair digite um número negativo): "))
  if number >= 0:
    num_positivos.append(number) 
  else:
    break
print(f"Lista dos números digitados {num_positivos}")

buscar = int(input("Informe o número que deseja verificar se está na lista: "))
if buscar in num_positivos:
  print(f"O número {buscar} está na lista!!!")
else:
  print(f"O número {buscar} não está na lista!!!")
  #primeira atividade