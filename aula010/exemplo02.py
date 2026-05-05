# for i in range (5):
#     total_produzido = float(input("Digite o total produzido: "))
#     funcionarios = int(input("Digite o numero de funcionarios: "))

#     media_por_funcionarios = total_produzido / funcionarios
#     print (f'Media por funcionario {media_por_funcionarios:.2f}')

for i in range (5):

    try:
        total_produzido = float(input("Digite o total produzido: "))
        funcionarios = int(input("Digite o numero de funcionarios: "))

        media_por_funcionarios = total_produzido / funcionarios
        print (f'Media por funcionario {media_por_funcionarios:.2f}')
    except ValueError:
        print ("Informe um numero")
    except ZeroDivisionError:
        print ("Funcionarios nao pode ser zero")