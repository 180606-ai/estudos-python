nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"\nUsuário: {nome}")

if idade >= 18:
    print("Acesso permitido")
else:
    print("Acesso negado")