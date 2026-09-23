# Sistema de Controle de Ocupação de Aparelhos em uma Academia

Sistema em Python para registrar o uso de 12 aparelhos organizados em três setores: Musculação, Cardio e Funcional.

## Regra central

A aplicação usa uma matriz 3x4:
- `0` = aparelho livre;
- `1` = aparelho ocupado.

Ao clicar em um aparelho livre, ele passa para ocupado e o acumulado de utilizações aumenta em 1. Ao clicar novamente, ele volta a livre sem diminuir o acumulado.

## Tecnologias
- Python 3
- Tkinter
- tkinter.ttk

## Estrutura

```text
projeto-academia/
├── MEMORY.md
├── ROADMAP.md
├── README.md
├── main.py
└── ia/
    └── Prompt Python.md
```

## Execução

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

## Paradigma

O código segue programação procedural, sem classes personalizadas, e demonstra sequência, seleção e repetição.

## Integrantes

- 261120362 - Hugo Hisashi    
- 261120244 – Arthur Souza
- 261120245 – Samuel Knupp
