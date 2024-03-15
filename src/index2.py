def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas
    nivel = ""

    if vitorias < 10:
        nivel = "Ferro"
    elif vitorias >= 10 and vitorias <= 20:
        nivel = "Bronze"
    elif vitorias >= 21 and vitorias <= 50:
        nivel = "Prata"
    elif vitorias >= 51 and vitorias <= 80:
        nivel = "Ouro"
    elif vitorias >= 81 and vitorias <= 90:
        nivel = "Diamante"
    elif vitorias >= 91 and vitorias <= 100:
        nivel = "Lendário"
    elif vitorias >= 101:
        nivel = "Imortal"

    return f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}"

vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))

print(calcular_nivel(vitorias, derrotas))
