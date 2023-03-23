from datetime import datetime, timedelta

def porcentagem_tempo(tempo, unidade):
    total_segundos_em_um_dia = 86400
    total_segundos_em_um_mes = 2629743
    total_segundos_em_um_ano = 31556952

    if unidade == "dias":
        tempo_em_segundos = tempo * total_segundos_em_um_dia
    elif unidade == "meses":
        tempo_em_segundos = tempo * total_segundos_em_um_mes
    elif unidade == "anos":
        tempo_em_segundos = tempo * total_segundos_em_um_ano
    else:
        raise ValueError("Unidade inválida. Por favor, informe 'dias', 'meses' ou 'anos'.")

    return tempo_em_segundos

def divisao_tempo(tempo_total, divisor):
    anos = int(tempo_total // 365)
    meses = int((tempo_total % 365) // 30)
    dias = int((tempo_total % 365) % 30)

    return f"{anos} anos, {meses} meses e {dias} dias"

def menu():
    print("Calculadora de Tempo")
    print("1. Calcular Data Final Resultante")
    print("2. Dividir Data por Número")
    print("3. Sair")
    opcao = int(input("Informe a opção desejada: "))
    return opcao

while True:
    print("Menu:")
    print("1. Calcular porcentagem de tempo em dias, meses e anos")
    print("2. Dividir quantidade de dias totais da data escolhida por um número escolhido")
    print("3. Sair")

    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        anos = int(input("Informe a quantidade de anos: "))
        meses = int(input("Informe a quantidade de meses: "))
        dias = int(input("Informe a quantidade de dias: "))

        dias_por_ano = 365

        dias_totais = dias_por_ano * anos + 30.44 * meses + dias
        porcentagem = (dias_totais / 365) * 100

        print("Resultado: {}% ({} dias)".format(porcentagem, dias_totais))

    elif opcao == 2:
        tempo = int(input("Informe a quantidade de tempo: "))
        unidade = input("Informe a unidade de tempo (dias, meses ou anos): ")
        
        divisor = float(input("Informe o número pelo qual deseja dividir: "))
        try:
            tempo_em_segundos = porcentagem_tempo(tempo, unidade)
        except ValueError as e:
            print("ERRO:", e)
            continue

        tempo_total = tempo_em_segundos / divisor
        print("Resultado da divisão:", divisao_tempo(tempo_total, divisor))

    elif opcao == 3:
        break

    else:
        print("Opção inválida. Por favor, informe uma opção válida.")

print("Programa encerrado.")

