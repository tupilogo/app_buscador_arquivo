import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
from tkinter.filedialog import askdirectory
import re


def buscar_arquivo():
    caminho = input_caminho.get()
    extensao = input_extencao.get()
    nome_arquivo = input_nome_arquivo.get()
    

    # Adiciona a mensagem ao widget Text
    output_text.insert(tk.END, "Tenha pasciência, estou entrando no limbo...\n\n")
    output_text.update_idletasks()
    
    # Buscar arquivos .pst no diretório e subdiretórios
    arquivos_encontrados = __buscador_de_arquivos(nome_arquivo=nome_arquivo, diretorio=caminho, extencao=extensao)

    # Mostrar os arquivos encontrados
    if arquivos_encontrados:
        messagebox.showinfo("Informativo", f"Achei!")
        
        # Habilitar o input das informações
        output_text.configure(state='normal')
        
        # Adiciona a mensagem de sucesso ao widget Text
        output_text.insert(tk.END, "\nOh o tanto que eu achei ai oh! Busca finalizada.\n")
        output_text.update_idletasks()
        
        for n, arquivo in enumerate(arquivos_encontrados):
            # Adiciona a mensagem de sucesso ao widget Text
            output_text.insert(tk.END, f"{n+1} - {arquivo}\n\n")
            output_text.update_idletasks()
    else:
        # Janela de erro
        messagebox.showerror("Erro", f"Só perda de tempo!")
    
    output_text.insert(tk.END, "\nBusca finalizada.\n")
    output_text.update_idletasks()


def limpar_tela():
    output_text.configure(state='normal')
    output_text.delete('1.0', tk.END)
    output_text.configure(state='disabled')


def __buscador_de_arquivos(nome_arquivo:str, diretorio, extencao:str):
    arquivos_pst = []
    extencao = extencao.lower()

    for pasta_raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.lower().endswith(extencao) and nome_arquivo in arquivo:
                arquivos_pst.append(os.path.join(pasta_raiz, arquivo))
    return arquivos_pst


def selecionar_caminho_pasta(elemento: tk.Entry) -> str:
    '''
    ## Selecionar Caminho Pasta
    ---
    Seleciona caminho da pasta para criar um novo novo projeto
    ### Atribuições
    ---
    parâmetros:
        elemento : tkinter.Entry

    return pasta_selecionada : str
    '''
    try:
        pasta_selecionada = askdirectory()
        elemento.delete(0, tk.END)  # Limpa o conteúdo atual do Entry
        elemento.insert(0, pasta_selecionada)  # Insere o novo caminho no Entry
    except FileExistsError as e:
        messagebox.showerror("Erro", "Erro ao encontrar pasta!")
        print("Erro", "Erro ao encontrar pasta!", e)
    return pasta_selecionada


root = tk.Tk()
frame_buscar_arquivo = tk.Frame(root)
frame_extencao_arquivo = tk.Frame(root)
frame_nome_do_arquivo = tk.Frame(root)
frame_envio_requisicao = tk.Frame(root)

frame_buscar_arquivo.pack(side=tk.TOP, padx=10, pady=10)
frame_nome_do_arquivo.pack(side=tk.TOP, padx=10, pady=10)
frame_extencao_arquivo.pack(side=tk.TOP, padx=10, pady=10)
frame_envio_requisicao.pack(side=tk.BOTTOM, padx=10, pady=10)

root.title("Buscador de Arquivo")

# Rótulo do input do caminho do arquivo
label_caminho = tk.Label(frame_buscar_arquivo, text="Caminho do arquivo:")
label_caminho.pack(side=tk.LEFT)
# Entrada para o caminho do arquivo
input_caminho = tk.Entry(frame_buscar_arquivo, width=50)
input_caminho.pack(side=tk.LEFT)
# Busca a pasta e retorna o caminho do arquivo
botao_buscar_pasta = tk.Button(frame_buscar_arquivo, text="Buscar Pasta...", command=lambda: selecionar_caminho_pasta(elemento=input_caminho))
botao_buscar_pasta.pack(side=tk.LEFT, padx=5)

# Rótulo do input do nome do nome do arquivo
label_nome_arquivo = tk.Label(frame_nome_do_arquivo, text="Nome do arquivo:")
label_nome_arquivo.pack(side=tk.LEFT)
# Entrada para o nome do arquivo
input_nome_arquivo = tk.Entry(frame_nome_do_arquivo, width=20)
input_nome_arquivo.pack(side=tk.LEFT)

# Rótulo do input da extenção do arquivo
label_extencao = tk.Label(frame_extencao_arquivo, text="Extensão do arquivo:")
label_extencao.pack(side=tk.LEFT)
# Entrada para a extensão do arquivo
input_extencao = tk.Entry(frame_extencao_arquivo, width=5)
input_extencao.pack(side=tk.LEFT)


# Mostrar o status do sistema
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
output_text.pack(padx=10, pady=10)

# Botão para iniciar a busca
botao_buscar = tk.Button(frame_envio_requisicao, text="Buscar Arquivo", command=buscar_arquivo, width=20, height=2)
botao_buscar.pack(side=tk.LEFT, padx=10, pady=10)

# Botão para limpar a tela de busca
botao_limpar = tk.Button(frame_envio_requisicao, text="Limpar tela de saída", command=limpar_tela, width=20, height=2)
botao_limpar.pack(side=tk.LEFT)

root.mainloop()