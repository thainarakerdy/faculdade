# Atividade unidade 1/ Faculdade
# Sistema de notas // Thainara Kerdy

def cadastrar_notas():
    notas = []
    print("¨¨¨¨Cadastro de Notas¨¨¨¨¨")

    while True:
        entrada = input("Digite a nota do aluno, ou 'pronto' para encerrar: ")
        if entrada.lower() == "pronto":
            break

        try:
            valor_nota = float(entrada)
            if 0 <= valor_nota <= 10:
                notas.append(valor_nota)
            else: 
                print("Digite uma nota válida entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número ou 'pronto'.")

    return notas

def calcular_media(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def aprovado_ou_nao(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"

def relatorio(notas, media, situacao):
    print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
    print("        RELATÓRIO FINAL          ")
    print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
    print(f"Notas cadastradas : {notas}")
    print(f"Média do aluno    : {media:.2f}")
    print(f"Situação Final    : {situacao}")
    print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n")

def principal():
    lista_notas = cadastrar_notas()

    if lista_notas:
        media_aluno = calcular_media(lista_notas) 
        situacao_aluno = aprovado_ou_nao(media_aluno)
        relatorio(lista_notas, media_aluno, situacao_aluno)
    else: 
        print("Nenhuma nota cadastrada.")

if __name__ == "__main__":
    principal()
