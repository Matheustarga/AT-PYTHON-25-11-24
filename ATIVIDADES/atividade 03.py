atletas = {}

while True:
 nome = input("informe o nome do atleta(para sair digite 'sair'): ").upper()
 if nome == "SAIR":
  break
 primeiro = float(input("Informe o valor do 1 salto: "))
 segundo = float(input("Informe o valor do 2 salto: "))
 terceiro = float(input("Informe o valor do 3 salto: "))
 quarto = float(input("Informe o valor do 4 salto: "))
 quinto = float(input("Informe o valor do 5 salto: "))

 media = (primeiro+segundo+terceiro+quarto+quinto)/5

 atletas[nome] = f"[1-S = {primeiro}  2-S = {segundo}  3-S = {terceiro}  4-S = {quarto}  5-S = {quinto} A MÉDIA DOS SALTOS FOI: {media}]"

print(f"{atletas}")