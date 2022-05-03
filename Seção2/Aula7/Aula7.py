nome = "Guilherme"
altura= 1.70
idade = 28
e_maior=idade>18
peso= 83
imc = peso/(altura*altura)

print("Nome:", nome)
print("Altura:", altura)
print("idade:", idade)
print("Maior:", e_maior)
print("Peso:", peso)

print()
print(f"{nome} tem {idade}, anos e seu IMC é de: {imc:.2f}") #f strings, variavel:.2f é usado pra arredondar ponto flutuante
print("{} tem {} anos e seu imc e {}".format(nome, idade,imc))

