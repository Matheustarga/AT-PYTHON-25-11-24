colaborador = {}
abono_total = 0 
colab_min = 0
maior_abono = []

while True:
 nome_colab = input("Digite o nome do colaborador(digite sair para finalizar): ").upper()
 if nome_colab == "SAIR":
  break
 salario = float(input("Digite o salario do colaborador"))


 abono = salario * 0.2
 maior_abono.append(abono)

 if abono < 100:
  total_S_A = salario + 100
  abono_total +=100
  colab_min += 1

 else:
  total_S_A = salario + abono
  abono_total += abono
 colaborador[nome_colab] = f"salário R$ {salario}, salário com abono R$ {total_S_A}"
print(f"{colaborador}")
print(f"TOTAL DE COLABORADORES{len(colaborador)}")
print(f"VALOR TOTAL A SER GASTO COM ABONO: R$ {abono_total}")
print(f"NÚMERO DE COLABORADORES QUE VÃO RECEBER O ABONO MIN. {colab_min}")
print(f"MAIOR ABONO PAGO R$ {max(maior_abono)}")