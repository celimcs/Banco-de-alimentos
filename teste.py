from tkinter import *
from tkinter import messagebox

# Listas para armazenar os dados
doadores = []
instituicoes = []
entradas_estoque = []
saidas_estoque = []

# Função para cadastrar um doador
def cadastrar_doador():
    janela_cadastro = Toplevel(janela)
    janela_cadastro.title("Cadastrar Doador")
    janela_cadastro.geometry("300x250")

    Label(janela_cadastro, text="Nome do Doador:").pack(pady=5)
    nome_entry = Entry(janela_cadastro, width=30)
    nome_entry.pack(pady=5)

    Label(janela_cadastro, text="Contato do Doador:").pack(pady=5)
    contato_entry = Entry(janela_cadastro, width=30)
    contato_entry.pack(pady=5)

    Label(janela_cadastro, text="Endereço do Doador:").pack(pady=5)
    endereco_entry = Entry(janela_cadastro, width=30)
    endereco_entry.pack(pady=5)

    def salvar_doador():
        nome = nome_entry.get()
        contato = contato_entry.get()
        endereco = endereco_entry.get()
        if nome and contato and endereco:
            doadores.append({"Nome": nome, "Contato": contato, "Endereço": endereco})
            messagebox.showinfo("Cadastro", "Doador cadastrado com sucesso!")
            janela_cadastro.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    Button(janela_cadastro, text="Salvar", command=salvar_doador).pack(pady=20)

# Função para cadastrar uma instituição beneficiária
def cadastrar_instituicao():
    janela_instituicao = Toplevel(janela)
    janela_instituicao.title("Cadastrar Instituição")
    janela_instituicao.geometry("300x250")

    Label(janela_instituicao, text="Nome da Instituição:").pack(pady=5)
    nome_entry = Entry(janela_instituicao, width=30)
    nome_entry.pack(pady=5)

    Label(janela_instituicao, text="Contato da Instituição:").pack(pady=5)
    contato_entry = Entry(janela_instituicao, width=30)
    contato_entry.pack(pady=5)

    Label(janela_instituicao, text="Endereço da Instituição:").pack(pady=5)
    endereco_entry = Entry(janela_instituicao, width=30)
    endereco_entry.pack(pady=5)

    def salvar_instituicao():
        nome = nome_entry.get()
        contato = contato_entry.get()
        endereco = endereco_entry.get()
        if nome and contato and endereco:
            instituicoes.append({"Nome": nome, "Contato": contato, "Endereço": endereco})
            messagebox.showinfo("Cadastro", "Instituição cadastrada com sucesso!")
            janela_instituicao.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    Button(janela_instituicao, text="Salvar", command=salvar_instituicao).pack(pady=20)

# Função para registrar a entrada de uma doação no estoque
def registrar_entrada():
    janela_entrada = Toplevel(janela)
    janela_entrada.title("Registrar Entrada de Doação")
    janela_entrada.geometry("300x200")

    Label(janela_entrada, text="Nome do Item:").pack(pady=5)
    item_entry = Entry(janela_entrada, width=30)
    item_entry.pack(pady=5)

    Label(janela_entrada, text="Quantidade:").pack(pady=5)
    quantidade_entry = Entry(janela_entrada, width=30)
    quantidade_entry.pack(pady=5)

    def salvar_entrada():
        item = item_entry.get()
        quantidade = quantidade_entry.get()
        if item and quantidade.isdigit():
            entradas_estoque.append({"Item": item, "Quantidade": int(quantidade)})
            messagebox.showinfo("Cadastro", "Entrada registrada com sucesso!")
            janela_entrada.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos corretamente.")

    Button(janela_entrada, text="Salvar", command=salvar_entrada).pack(pady=5)

# Função para registrar a saída de um item do estoque
def registrar_saida():
    janela_saida = Toplevel(janela)
    janela_saida.title("Registrar Saída de Estoque")
    janela_saida.geometry("300x200")

    Label(janela_saida, text="Nome do Item:").pack(pady=5)
    item_entry = Entry(janela_saida, width=30)
    item_entry.pack(pady=5)

    Label(janela_saida, text="Quantidade:").pack(pady=5)
    quantidade_entry = Entry(janela_saida, width=30)
    quantidade_entry.pack(pady=5)

    def salvar_saida():
        item = item_entry.get()
        quantidade = quantidade_entry.get()
        if item and quantidade.isdigit():
            saidas_estoque.append({"Item": item, "Quantidade": int(quantidade)})
            messagebox.showinfo("Cadastro", "Saída registrada com sucesso!")
            janela_saida.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos corretamente.")

    Button(janela_saida, text="Salvar", command=salvar_saida).pack(pady=5)

# Função para mostrar todos os dados dos doadores
def mostrar_doador():
    janela_doador = Toplevel(janela)
    janela_doador.title("Lista de Doadores")
    janela_doador.geometry("400x300")

    if not doadores:
        Label(janela_doador, text="Nenhum doador cadastrado.").pack(pady=10)
    else:
        doador_texto = "\n".join(
            f"Nome: {doador['Nome']}, Contato: {doador['Contato']}, Endereço: {doador['Endereço']}"
            for doador in doadores
        )
        Label(janela_doador, text=f"Total de Doadores: {len(doadores)}\n\n{doador_texto}", justify=LEFT).pack(pady=10)

# Função para mostrar todos os dados das instituições
def mostrar_instituicoes():
    janela_instituicao = Toplevel(janela)
    janela_instituicao.title("Lista de Instituições")
    janela_instituicao.geometry("400x300")

    if not instituicoes:
        Label(janela_instituicao, text="Nenhuma instituição cadastrada.").pack(pady=10)
    else:
        instituicao_texto = "\n".join(
            f"Nome: {instituicao['Nome']}, Contato: {instituicao['Contato']}, Endereço: {instituicao['Endereço']}"
            for instituicao in instituicoes
        )
        Label(janela_instituicao, text=f"Total de Instituições: {len(instituicoes)}\n\n{instituicao_texto}", justify=LEFT).pack(pady=10)

# Função para mostrar o estoque
def mostrar_estoque():
    estoque = Toplevel(janela)
    estoque.title("Estoque")
    estoque.geometry("300x300")

    estoque_texto = "Entradas de Estoque:\n" + "\n".join(f"{item['Item']}: {item['Quantidade']}" for item in entradas_estoque)
    estoque_texto += "\n\nSaídas de Estoque:\n" + "\n".join(f"{item['Item']}: {item['Quantidade']}" for item in saidas_estoque)

    Label(estoque, text=estoque_texto, justify=LEFT).pack(pady=10)

# Função para sair do sistema
def sair():
    janela.destroy()

# Configuração da janela principal
janela = Tk()
janela.title("Banco de Alimentos")
janela.geometry("300x400")

# Mensagem de boas-vindas
Label(janela, text="Bem-vindo ao Banco de Alimentos!", font=("Arial", 12)).pack(pady=10)

# Botões principais
Button(janela, text="Cadastrar Doador", command=cadastrar_doador).pack(fill="x", padx=20, pady=5)
Button(janela, text="Cadastrar Instituição", command=cadastrar_instituicao).pack(fill="x", padx=20, pady=5)
Button(janela, text="Registrar Entrada de Doação", command=registrar_entrada).pack(fill="x", padx=20, pady=5)
Button(janela, text="Registrar Saída de Estoque", command=registrar_saida).pack(fill="x", padx=20, pady=5)
Button(janela, text="Mostrar Estoque", command=mostrar_estoque).pack(fill="x", padx=20, pady=5)
Button(janela, text="Mostrar Doadores", command=mostrar_doador).pack(fill="x", padx=20, pady=5)
Button(janela, text="Mostrar Instituições", command=mostrar_instituicoes).pack(fill="x", padx=20, pady=5)
Button(janela, text="Sair", command=sair).pack(fill="x", padx=20, pady=5)

# Iniciar o loop da interface gráfica
janela.mainloop()

