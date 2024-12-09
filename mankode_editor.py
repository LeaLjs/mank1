import os
import tkinter as tk
from tkinter import filedialog, messagebox
import io
import contextlib

# Variável para armazenar o arquivo atual
arquivo_aberto = None

# Funções do editor de texto
def novo_arquivo():
    global arquivo_aberto
    texto.delete("1.0", tk.END)
    arquivo_aberto = None
    janela.title("Editor de Código - Sem título")

def abrir_arquivo():
    global arquivo_aberto
    caminho = filedialog.askopenfilename(defaultextension=".py",
                                         filetypes=[("Arquivos Python", "*.py"), 
                                                    ("Todos os Arquivos", "*.*")])
    if caminho:
        arquivo_aberto = caminho
        with open(caminho, "r", encoding="utf-8") as file:
            texto.delete("1.0", tk.END)
            texto.insert("1.0", file.read())
        janela.title(f"Editor de Código - {caminho}")

def salvar_arquivo():
    global arquivo_aberto
    if not arquivo_aberto:
        salvar_como()
    else:
        with open(arquivo_aberto, "w", encoding="utf-8") as file:
            file.write(texto.get("1.0", tk.END))
        messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")

def salvar_como():
    global arquivo_aberto
    caminho = filedialog.asksaveasfilename(defaultextension=".py",
                                           filetypes=[("Arquivos Python", "*.py"), 
                                                      ("Todos os Arquivos", "*.*")])
    if caminho:
        arquivo_aberto = caminho
        with open(caminho, "w", encoding="utf-8") as file:
            file.write(texto.get("1.0", tk.END))
        janela.title(f"Editor de Código - {caminho}")
        messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")

# Função para rodar o código Python simulado
def executar_codigo():
    global arquivo_aberto
    if not arquivo_aberto:
        messagebox.showerror("Erro", "Por favor, salve o arquivo antes de executar.")
        return

    # Simula a execução do código Python e redireciona a saída
    resultado = ""
    try:
        with open(arquivo_aberto, "r", encoding="utf-8") as file:
            codigo = file.read()
            with io.StringIO() as buffer, contextlib.redirect_stdout(buffer):
                exec_locals = {}
                exec(codigo, {}, exec_locals)  # Executa o código
                resultado = buffer.getvalue()  # Captura o que foi impresso
    except Exception as e:
        resultado = f"Erro ao executar o código:\n{e}"

    # Exibe o resultado no Mank Bash
    abrir_bash(resultado)

def abrir_bash(saida):
    """Abre uma janela simulando o Mank Bash."""
    bash = tk.Toplevel()
    bash.title("Mank Bash")
    bash.geometry("1200x2600")
    bash_texto = tk.Text(bash, wrap="word", bg="black", fg="white", font=("Courier", 12))
    bash_texto.pack(expand=True, fill="both")
    bash_texto.insert("1.0", saida)
    bash_texto.configure(state="disabled")

# Interface gráfica
janela = tk.Tk()
janela.title("Editor de Código - Sem título")
janela.geometry("1200x2600")

# Área de texto
texto = tk.Text(janela, wrap="word", undo=True, font=("Courier", 12))
texto.pack(expand=1, fill="both")

# Menu
menu = tk.Menu(janela)
janela.config(menu=menu)

# Menu "Arquivo"
menu_arquivo = tk.Menu(menu, tearoff=0)
menu_arquivo.add_command(label="Novo", command=novo_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
menu_arquivo.add_command(label="Salvar como...", command=salvar_como)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)
menu.add_cascade(label="Arquivo", menu=menu_arquivo)

# Menu "Executar"
menu_executar = tk.Menu(menu, tearoff=0)
menu_executar.add_command(label="Executar", command=executar_codigo)
menu.add_cascade(label="Executar", menu=menu_executar)

# Inicia a aplicação
janela.mainloop()
