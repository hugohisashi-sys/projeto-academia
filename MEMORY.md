# MEMORY — Memória de trabalho e contexto arquitetural

## Objetivo
Controlar a ocupação de 12 aparelhos de uma academia durante um expediente.

## Estrutura central
`matriz_ocupacao` é uma matriz 3x4:
- linha 0: Musculação
- linha 1: Cardio
- linha 2: Funcional
- 0: livre
- 1: ocupado

## Contador
`total_utilizacoes` começa em 0 e aumenta somente quando um aparelho passa de 0 para 1. A liberação de 1 para 0 não reduz o acumulado.

## Interface
A interface usa Tkinter e ttk, com botões associados às posições da matriz. O estado é mostrado diretamente nos botões e o total é mostrado em um contador.

## Paradigma
O projeto é procedural. Não utiliza classes personalizadas.

## Fluxo
1. Inicializar matriz.
2. Criar interface.
3. Receber clique.
4. Alternar estado.
5. Incrementar contador quando houver nova ocupação.
6. Atualizar interface.
7. Encerrar e mostrar total.

## Restrições pedagógicas
Seguir o `ia/Prompt Python.md` fornecido pelo professor, incluindo comentários pedagógicos sobre funções e métodos de alto nível utilizados.
