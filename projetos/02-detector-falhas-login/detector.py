arquivo = open("servidor.log")

contador = 0

for linha in arquivo:
    if "LOGIN_FAILED" in linha:
        contador += 1

print("=== DETECTOR DE FALHAS DE LOGIN ===")
print(f"Total de falhas: {contador}")

arquivo.close()