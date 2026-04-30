# Estudo Organizer
![Version](https://img.shields.io/badge/version-2.0.3-blue )
[![CI - Estudo Organizer](https://github.com/barcelos00/bootcamp2/actions/workflows/ci.yml/badge.svg )](https://github.com/barcelos00/bootcamp2/actions/workflows/ci.yml )

> **Status do Projeto:** Etapa 2 - Evolução Concluída

## Descrição do Problema

Este projeto foi desenvolvido para solucionar a dificuldade de organização e manutenção de rotinas de estudo enfrentada por diversos estudantes. A falta de um planejamento claro e de um acompanhamento de progresso muitas vezes resulta em procrastinação e baixa produtividade acadêmica.

## Proposta da Solução (Etapa 2)

O Estudo Organizer evoluiu! Agora, além de gerenciar suas matérias, a aplicação se conecta à **Advice Slip API** para fornecer frases motivacionais em tempo real, incentivando o foco e a disciplina.

### Novidades da Etapa 2:
- **Integração com API:** Consumo de serviço externo para frases de incentivo.
- **Testes de Integração:** Validação da comunicação com a API.
- **Fluxo Profissional:** Uso de Issues e Branch `entrega-intermediaria`.
- **Deploy:** Aplicação disponível online.
- O projeto ainda é possivel de ser executado no terminal para caso nao abra na interface grafica.
- Executado tanto no terminal pra poder ser executavel sem o acesso a rede local criada.

## Tecnologias Utilizadas

*   **Linguagem:** Python 3.11+
*   **Bibliotecas:** `requests` (API), `pytest` (Testes), `ruff` (Linting)
*   **CI/CD:** GitHub Actions
*   **Deploy:** Streamlit Cloud / Render

## Instruções de Instalação (Windows)

1.  Realize o clone do repositório:
    ```powershell
    git clone https://github.com/barcelos00/bootcamp2.git
    cd bootcamp2
    ```
2.  Crie um ambiente virtual:
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  Instale as dependências:
    ```powershell
    pip install -r requirements.txt
    
    #caso não tenha streamlit pode baixar por fora peloseguinte codigo ou direto pelo requirements.
    pip install streamlit
    ```
4. Rode o codigo pra poder abrir a interface:
   ```powershell
   streamlit run src/web_app.py
    ```

## Instruções de Execução

Para iniciar a aplicação:
```powershell
python src/app.py #rodar no terminal

streamlit run src/web_app.py  #rodar na interface grafica
```

## Testes e Qualidade

Para rodar os testes unitários e de integração:
```powershell
python -m pytest
```

## Versão Atual

2.0.3 (MAJOR: Evolução com API e Testes de Integração)

## Autor

Victor Santos Barcelos

## Link do Repositório Público

[https://github.com/barcelos00/bootcamp2](https://github.com/barcelos00/bootcamp2)

## Link da Aplicação Web

https://bootcamp2-u8xbkegk9svbnhdgjurzqt.streamlit.app/
