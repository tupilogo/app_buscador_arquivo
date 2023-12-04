import tkinter as tk
from tkinter import scrolledtext, messagebox
import os


def buscar_arquivo():
    caminho = entry_caminho.get()
    extensao = entry_extensao.get()

    # Adiciona a mensagem ao widget Text
    output_text.insert(tk.END, "Tenha pasciência, estou entrando no limbo...\n\n")
    output_text.update_idletasks()
    
    # Buscar arquivos .pst no diretório e subdiretórios
    arquivos_encontrados = __buscador_de_arquivos(diretorio=caminho, extencao=extensao)

    # Mostrar os arquivos encontrados
    if arquivos_encontrados:
        messagebox.showinfo("Informativo", f"Achei, pae!")
        
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
    
    output_text.insert(tk.END, "\nOh o tanto que eu achei ai oh! Busca finalizada.\n")
    output_text.update_idletasks()


def limpar_tela():
    output_text.configure(state='normal')
    output_text.delete('1.0', tk.END)
    output_text.configure(state='disabled')


def __buscador_de_arquivos(diretorio, extencao):
    arquivos_pst = []
    for pasta_raiz, sub_pastas, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(extencao):
                arquivos_pst.append(os.path.join(pasta_raiz, arquivo))
    return arquivos_pst


root = tk.Tk()
root.title("Busca o Arquivo no Inferno")
root.geometry("500x400")

# Criando rótulos
label_caminho = tk.Label(root, text="Caminho do arquivo que deseja buscar:")
label_caminho.pack()

# Entrada para o caminho do arquivo
entry_caminho = tk.Entry(root)
entry_caminho.pack()

label_extensao = tk.Label(root, text="Extensão do arquivo:")
label_extensao.pack()

# Entrada para a extensão do arquivo
entry_extensao = tk.Entry(root)
entry_extensao.pack()

# Mostrar o status do sistema
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=200, height=15)
output_text.pack(padx=10, pady=10)

# Botão para iniciar a busca
botao_buscar = tk.Button(root, text="Buscar Arquivo", command=buscar_arquivo)
botao_buscar.pack()

# Botão para limpar a tela de busca
botao_limpar = tk.Button(root, text="Limpar tela de saída", command=limpar_tela)
botao_limpar.pack()

root.mainloop()