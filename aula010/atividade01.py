#iniciar com saldo de 1000, qual valor sacar
#apos sacar, informar o resultado da operacao e finalize o programa
# utilize a estrutura de tratamento de erros

print ("Saldo Inicial 1000")

try:
    saldo = float(1000)
    saque = float(input("Informe o valor de saque: "))

    saldo_total = saldo - saque
    if saldo_total < 0:
        print ("sem saldo disponivel, operacao nao realizada")
    else:
        print (f"Saldo total: {saldo_total}")

except Exception:
    print ("Valores nao validos")
finally:
    print ("Programa encerrado")
