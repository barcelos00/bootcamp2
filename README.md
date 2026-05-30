# Estudo Organizer 📚

## 📖 Apresentação do Projeto
O Estudo Organizer é uma aplicação web interativa voltada para o gerenciamento de tarefas e acompanhamento de horas de estudo. O objetivo do projeto é ajudar o usuário a manter o foco, permitindo o registro de matérias, o controle do tempo dedicado a cada uma e a visualização clara do progresso, tudo isso com um toque extra de incentivo através de mensagens motivacionais.

## ⚙️ Como Funciona
A plataforma possui uma interface intuitiva dividida em duas áreas principais:
* **Barra Lateral:** Utilizada para o cadastro de novas matérias e a definição da carga horária pretendida.
* **Painel Principal:** Exibe a lista completa de estudos. Aqui, o usuário pode marcar as tarefas como concluídas, remover as finalizadas para limpar o painel e solicitar dicas motivacionais geradas em tempo real.
* Todos os dados inseridos são processados pelo backend em Python e salvos permanentemente em um banco de dados na nuvem, garantindo que o progresso não seja perdido ao fechar o navegador.

## 💻 Plataformas e Tecnologias Utilizadas
* **Python 3.11:** Linguagem base da aplicação.
* **Streamlit:** Framework utilizado para a construção da interface gráfica web.
* **Supabase:** Plataforma Backend-as-a-Service (BaaS) baseada em PostgreSQL, responsável pelo armazenamento de dados na nuvem.
* **Pytest:** Biblioteca utilizada para a execução dos testes de integração e validação do código com mocks.
* **Advice Slip API:** API pública consumida para gerar os conselhos motivacionais.

## 🚀 Como Iniciar

### 1. Pré-requisitos
Tenha o Python 3.11 ou superior instalado em sua máquina e uma conta ativa no [Supabase](https://supabase.com/). Configure uma tabela chamada `tarefas` no seu banco de dados com as colunas `id` (int8), `materia` (text), `horas` (float8) e `concluida` (boolean), desativando o RLS (Row Level Security).

### 2. Configuração das Variáveis de Ambiente
Crie um arquivo chamado `.env` na pasta raiz do projeto contendo as suas credenciais do Supabase, no seguinte formato:
SUPABASE_URL=sua_url_aqui
SUPABASE_KEY=sua_chave_aqui

### 3. Instalação das Dependências
Abra o terminal na pasta raiz do seu projeto e instale as bibliotecas necessárias com o comando:
```bash
python -m pip install -r requirements.txt