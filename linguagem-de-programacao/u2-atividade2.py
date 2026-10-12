# Atividade Unidade 2 - Linguagem de Programação
# Sistema de Gerenciamento de Livros // Thainara Kerdy

import matplotlib.pyplot as plt

class livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

biblioteca = []

def cadrastar_livros():
    print("\n¨¨¨¨¨¨¨¨Cadastro de novos livros¨¨¨¨¨¨¨¨")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor(a) do livro: ")
    genero = input("Digite o genero do livro: ")

    try:
        quantidade = int(input("Digite a quantidade disponivel: "))
        livro_novo = livro(titulo, autor, genero, quantidade)
        biblioteca.append(livro_novo)
        print("Livro cadastrado com sucesso!")
    except ValueError:
        print("Erro 402: Quantidade não valida")

def listar_livros():
    print("\n¨¨¨¨¨¨¨¨Lista de livros na Biblioteca¨¨¨¨¨¨¨¨")
    if not biblioteca:
        print("Erro 404: Nenhum livro cadastrado")
        return
    for i, livro in enumerate(biblioteca, 1):
        print(f"{i}. Titulo: {livro.titulo} | Autor: {livro.autor} | Genero: {livro.genero}")

def buscar_livro():
    print("\n¨¨¨¨¨¨¨¨Buscar livro na Biblioteca¨¨¨¨¨¨¨¨")
    termo = input("Digite o titulo, ou, parte do nome do livro que deseja buscar: ").lower()
    encontrados = [l for l in biblioteca if termo in l.titulo.lower()]

    if not encontrados:
        print("Nenhum livro com esse titulo")
    else:
        print("\nLivros encontrados: ")
        for livro in encontrados:
            print(f"- Titulo: {livro.titulo} | Autor: {livro.autor} | Genero: {livro.genero}")

def gerar_grafico_generos():
    if not biblioteca:
        print("\nAinda nao ha livros cadastrados")
        return

    contagem_generos = {}
    for livro in biblioteca:
        if livro.genero in contagem_generos:
            contagem_generos[livro.genero] += livro.quantidade
        else:
            contagem_generos[livro.genero] = livro.quantidade

    generos = list(contagem_generos.keys())
    quantidades = list(contagem_generos.values())

    plt.figure(figsize=(8, 5))
    plt.bar(generos, quantidades, color='darkblue')
    plt.xlabel('Gêneros')
    plt.ylabel('Quantidade de Livros')
    plt.title('Quantidade de Livros por Gênero')
    plt.xticks(rotation=45)
    plt.tight_layout()

    print("\nGerando grafico...")
    plt.show()

def main():
    while True:
        print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print(" SISTEMA DE BIBLIOTECA - MENU ")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("1. Cadastrar novo livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por titulo")
        print("4. Gerar grafico por genero")
        print("5. Sair")

        opcao = input("Escolha uma opcao: ")
    
        if opcao == '1':
            cadrastar_livros()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro()
        elif opcao == '4':
            gerar_grafico_generos()
        elif opcao == '5':
            print("Finalizando o sistema, tchau!")
            break
        else:
            print("Opcao invalida! Escolha de 1 ao 5.")

if __name__ == "__main__":
    main()