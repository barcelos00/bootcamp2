# Estudo Organizer

## Descricao do Problema

Este projeto foi desenvolvido para solucionar a dificuldade de organizacao e manutencao de rotinas de estudo enfrentada por diversos estudantes. A falta de um planejamento claro e de um acompanhamento de progresso muitas vezes resulta em procrastinacao e baixa produtividade academica.

## Proposta da Solucao

O Estudo Organizer e uma aplicacao de interface de linha de comando (CLI) que permite ao usuario gerenciar suas atividades de estudo de forma estruturada. A solucao foca na simplicidade e na eficacia, permitindo o registro de materias, definicao de carga horaria e controle de conclusao de tarefas.

## Publico-Alvo

Estudantes de diversos niveis de ensino, pesquisadores e profissionais em constante aprendizado que necessitam de uma ferramenta leve e direta para organizar suas demandas diarias de estudo.

## Funcionalidades Principais

*   Adicao de tarefas de estudo com especificacao de materia e horas estimadas.
*   Listagem completa de todas as tarefas cadastradas e seus respectivos status.
*   Marcacao de tarefas como concluidas para acompanhamento de progresso.
*   Validacao de dados para garantir que o tempo de estudo seja sempre positivo.

## Tecnologias Utilizadas

*   Linguagem de Programacao: Python 3.11+
*   Framework de Testes: Pytest
*   Analise Estatica (Linting): Ruff
*   Integracao Continua (CI): GitHub Actions

## Instrucoes de Instalacao

1.  Realize o clone do repositorio:
    ```bash
    git clone https://github.com/barcelos00/bootcamp2.git
    cd bootcamp2
    ```
2.  Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```
3.  Instale as dependencias necessarias:
    ```bash
    pip install -r requirements.txt
    ```

## Instrucoes de Execucao

Para iniciar a aplicacao interativa, utilize o comando:

```bash
python src/app.py
```

## Instrucoes para Rodar os Testes

Para executar a suite de testes automatizados, utilize o comando:

```bash
python -m pytest
```

## Instrucoes para Rodar o Lint

Para executar a analise estatica de codigo e verificar a qualidade do mesmo, utilize o comando:

```bash
ruff check src/ tests/
```

## Versao Atual

1.0.0

## Autor

Victor Santos Barcelos

## Link do Repositorio Publico

https://github.com/barcelos00/bootcamp2
