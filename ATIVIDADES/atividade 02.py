vingadores = ["HOMEM DE FERRO","CAPITÃO AMÉTICA","THOR","HULK","VIÚVA NEGRA","GAVIÃO ARQUEIRO"]

incluir = input("Digite o herói que desja adicionar aos vingadores: ").upper()
vingadores.append(incluir)

cont_posicao = 0
while "THOR" != vingadores[cont_posicao]:
 cont_posicao += 1
print(f"A posição do THOR é {cont_posicao}")

print(f"LISTA DOS VINGADORES {vingadores}")

while True:
 remover= input("Informe o Herói que deseja remover(para sair digite sair): ").upper()
 if remover == "SAIR":
  break
 if remover in vingadores:                 
  vingadores.remove(remover)
 else:
  print("Informe um valor válido: ")

print(f"LISTA DOS VINGADORES {vingadores}")
