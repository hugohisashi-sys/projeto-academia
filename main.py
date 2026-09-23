import tkinter as tk
from tkinter import ttk, messagebox

# Matriz 3x4: 0 = livre, 1 = ocupado.
matriz_ocupacao = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Acumulado de utilizações: só aumenta quando 0 passa para 1.
total_utilizacoes = 0

setores = ["Musculação", "Cardio", "Funcional"]

# Matriz visual que guarda os botões correspondentes aos aparelhos.
botoes_aparelhos = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None]
]

janela = None
texto_contador = None
botao_encerrar = None


def atualizar_contador():
    """Atualiza o contador mostrado na interface."""
    # config() altera a propriedade text do widget já criado.
    texto_contador.config(text=f"Total de utilizações: {total_utilizacoes}")


def atualizar_aparencia_botao(linha, coluna):
    """Atualiza o texto do botão conforme 0 (livre) ou 1 (ocupado)."""
    valor = matriz_ocupacao[linha][coluna]

    # Seleção: escolhe a mensagem visual de acordo com o estado.
    if valor == 0:
        texto = f"Aparelho {coluna + 1}\nLIVRE"
    else:
        texto = f"Aparelho {coluna + 1}\nOCUPADO"

    # config() atualiza o texto do botão.
    botoes_aparelhos[linha][coluna].config(text=texto)


def alternar_aparelho(linha, coluna):
    """Alterna um aparelho entre livre e ocupado."""
    global total_utilizacoes

    estado_atual = matriz_ocupacao[linha][coluna]

    # Seleção: 0 -> 1 significa nova ocupação; 1 -> 0 significa liberação.
    if estado_atual == 0:
        matriz_ocupacao[linha][coluna] = 1
        total_utilizacoes = total_utilizacoes + 1
    else:
        matriz_ocupacao[linha][coluna] = 0

    atualizar_aparencia_botao(linha, coluna)
    atualizar_contador()


def encerrar_expediente():
    """Apresenta o total e desabilita os controles."""
    # messagebox.showinfo() apresenta uma mensagem em uma janela gráfica.
    messagebox.showinfo(
        "Expediente encerrado",
        f"Total de utilizações registradas: {total_utilizacoes}"
    )

    # config(state=...) desabilita o botão depois do encerramento.
    botao_encerrar.config(state="disabled")

    # Repetição: percorre as três linhas da matriz.
    for linha in range(3):
        # Repetição interna: percorre os quatro aparelhos.
        for coluna in range(4):
            botoes_aparelhos[linha][coluna].config(state="disabled")


def criar_interface():
    """Cria a interface gráfica."""
    global janela, texto_contador, botao_encerrar

    janela = tk.Tk()

    # title() define o título da janela.
    janela.title("Controle de Ocupação - Academia")

    # geometry() define o tamanho inicial.
    janela.geometry("760x600")

    # resizable() permite redimensionar a janela.
    janela.resizable(True, True)

    # Style() cria a configuração visual do ttk.
    estilo = ttk.Style()

    # theme_use() seleciona o tema nativo disponível.
    try:
        estilo.theme_use("vista")
    except tk.TclError:
        pass

    # configure() define características visuais dos estilos.
    estilo.configure("Aparelho.TButton", font=("Segoe UI", 11), padding=10)
    estilo.configure("Titulo.TLabel", font=("Segoe UI", 18, "bold"))
    estilo.configure("Contador.TLabel", font=("Segoe UI", 12, "bold"))

    quadro_principal = ttk.Frame(janela, padding=20)

    # grid() posiciona o quadro na janela.
    quadro_principal.grid(row=0, column=0, sticky="nsew")

    # rowconfigure() permite expansão vertical do quadro.
    janela.rowconfigure(0, weight=1)

    # columnconfigure() permite expansão horizontal do quadro.
    janela.columnconfigure(0, weight=1)

    titulo = ttk.Label(
        quadro_principal,
        text="Controle de Ocupação de Aparelhos",
        style="Titulo.TLabel"
    )

    titulo.grid(row=0, column=0, pady=(0, 10))

    instrucoes = ttk.Label(
        quadro_principal,
        text="Clique em um aparelho para alternar entre LIVRE e OCUPADO."
    )

    instrucoes.grid(row=1, column=0, pady=(0, 15))

    texto_contador = ttk.Label(
        quadro_principal,
        text="Total de utilizações: 0",
        style="Contador.TLabel"
    )

    texto_contador.grid(row=2, column=0, pady=(0, 15))

    quadro_matriz = ttk.Frame(quadro_principal)
    quadro_matriz.grid(row=3, column=0, sticky="nsew")

    # Repetição: configura as três linhas da matriz.
    for linha in range(3):
        # rowconfigure() permite que a linha se expanda.
        quadro_matriz.rowconfigure(linha, weight=1)

    # Repetição: configura as quatro colunas da matriz.
    for coluna in range(4):
        # columnconfigure() permite que a coluna se expanda.
        quadro_matriz.columnconfigure(coluna, weight=1)

    # Repetição externa: percorre os três setores.
    for linha in range(3):
        etiqueta_setor = ttk.Label(
            quadro_matriz,
            text=setores[linha],
            anchor="center",
            font=("Segoe UI", 10, "bold")
        )

        etiqueta_setor.grid(
            row=linha * 2,
            column=0,
            columnspan=4,
            sticky="ew",
            pady=(5, 2)
        )

        # Repetição interna: percorre os quatro aparelhos do setor.
        for coluna in range(4):
            # lambda cria uma função curta para preservar os índices
            # e chamar alternar_aparelho no momento do clique.
            comando = lambda l=linha, c=coluna: alternar_aparelho(l, c)

            botao = ttk.Button(
                quadro_matriz,
                text=f"Aparelho {coluna + 1}\nLIVRE",
                style="Aparelho.TButton",
                command=comando
            )

            botao.grid(
                row=linha * 2 + 1,
                column=coluna,
                sticky="nsew",
                padx=4,
                pady=4
            )

            botoes_aparelhos[linha][coluna] = botao

    botao_encerrar = ttk.Button(
        quadro_principal,
        text="Encerrar expediente",
        command=encerrar_expediente
    )

    botao_encerrar.grid(row=4, column=0, pady=20)

    # mainloop() mantém a janela aberta e processa os cliques.
    janela.mainloop()


# SEQUÊNCIA: inicia a interface.
criar_interface()
