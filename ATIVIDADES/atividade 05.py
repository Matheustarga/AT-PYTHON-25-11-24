carros = ["FUSCA","GOL","VECTRA","MOBI","COROLLA"]
consumo = [11.5,13.3,10.8,14,9.3]
ind = 0
calculo_custo = {}

economico = max(consumo)
for i in range(len(carros)):
 if economico != consumo[i]:
  ind += 1
 else:
  break

print(f"O carro mais econômico é {carros[ind]} - KM/L {economico}")

for i in range(len(carros)):
 custo_1000 = (1000/consumo[i])*6.25
 calculo_custo[carros[i]] = f"O consumo para 1000km é R$ {custo_1000:.2f}"


for i in range(len(calculo_custo)):
 print(f"{carros[i]}--{calculo_custo[carros[i]]}")
