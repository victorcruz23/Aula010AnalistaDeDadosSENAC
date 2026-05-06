#determinar a media de cada aluno e continuar rodando o codigo


contador = 1
while True:
    print (f"aluno: {contador}")
    aluno = input ("Nome do aluno")
    
    notas = []
    try:
        for i in range (4):
            nota = float(input("Informe a nota"))
            notas.append(nota)

    except ValueError:
        print ("Informe valores validos")
    else:
        notas.append(nota)




    opcao = input ("Quer calcular para outro aluno?").strip().upper()
    if opcao != "Sim":
        break
