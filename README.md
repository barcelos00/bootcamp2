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
```
Para resolver isso da forma mais rápida e com menos dor de cabeça futura, eu recomendo fortemente que você siga o caminho de **fazer o downgrade do Python**.

Como o Python 3.14 é extremamente recente, várias bibliotecas (como essa `pyiceberg`) ainda não têm versões prontas e "mastigadas" para ele no Windows. Se você continuar no 3.14, esse erro de compilação em C++ vai continuar assombrando você em outros projetos.

Aqui está exatamente o que você deve fazer agora:

### 1. Desinstale o Python 3.14

* Vá nas Configurações do Windows > **Aplicativos** > **Aplicativos Instalados**.
* Procure por "Python 3.14" (e o "Python Launcher", se houver) e clique em **Desinstalar**.

### 2. Baixe e Instale o Python 3.12

O Python 3.12 é super estável e compatível com praticamente tudo.

* Acesse o site oficial: [python.org/downloads](https://www.python.org/downloads/) e baixe o instalador do Python 3.12 (ou 3.13, se for a versão estável mais em destaque).
* **⚠️ ATENÇÃO AQUI:** Na primeiríssima tela do instalador, antes de clicar em instalar, marque a caixinha lá embaixo que diz **"Add Python.exe to PATH"**. Só depois clique em "Install Now".

### 3. Limpe e recrie sua "venv"

Como você trocou a versão do Python "base" do computador, o ambiente virtual que estava na pasta `bootcamp2` quebrou. Precisamos fazer um novo.

* Feche o terminal que você estava usando e abra um novo no VS Code (ou PowerShell).
* Exclua a pasta `venv` (ou `.venv`, se for esse o nome) que está dentro da pasta `bootcamp2`. Pode excluir pelo próprio Windows Explorer.
* No terminal, crie uma venv nova do zero:
```powershell
python -m venv venv

```


* Ative essa venv nova:
```powershell
.\venv\Scripts\Activate

```


*(Lembre-se de confirmar se o `(venv)` apareceu verdinho no começo da linha).*

### 4. Instale os requisitos e rode o app!

Agora, com a casa arrumada e na versão certa do Python, o seu computador vai baixar as bibliotecas já prontas, sem precisar compilar nada.

* Rode a instalação em lote:
```powershell
python -m pip install -r requirements.txt

```


* Quando terminar, inicie o aplicativo:
```powershell
python -m streamlit run src/web_app.py

```



Pronto! Isso deve passar reto pelo erro do `pyiceberg` e abrir o seu site no navegador.

## 👥 Integrantes do Grupo
| Nome | Matrícula |
| Victor Barcelos | 22504504 |
| Gabriel Henrique | 22508587|
| Lucas Vieira Werneck| 22508352|

## 🔗 Links
* **Repositório:** https://github.com/barcelos00/bootcamp2