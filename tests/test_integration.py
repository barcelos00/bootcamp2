import pytest
import sqlite3
from src.app import EstudoOrganizer

# Fixture para criar um banco de dados temporário em memória para cada teste
@pytest.fixture
def organizador_db():
    conn = sqlite3.connect(":memory:")
    organizador = EstudoOrganizer(conn=conn)
    # _init_db is called in EstudoOrganizer.__init__
    yield organizador
    conn.close()

def test_obter_conselho_api_sucesso(organizador_db):
    """Teste de integração que valida a comunicação com a API Advice Slip."""
    conselho = organizador_db.obter_conselho_motivacional()
    
    # Verifica se o retorno é uma string e não está vazio
    assert isinstance(conselho, str)
    assert len(conselho) > 0
    assert conselho != ""

def test_adicionar_e_listar_tarefa(organizador_db):
    """Testa se a tarefa é adicionada e listada corretamente no banco de dados."""
    organizador_db.adicionar_tarefa("Matemática", 3.0)
    tarefas = organizador_db.listar_tarefas()
    assert len(tarefas) == 1
    assert tarefas[0]["materia"] == "Matemática"
    assert tarefas[0]["horas"] == 3.0
    assert not tarefas[0]["concluida"]

def test_concluir_tarefa(organizador_db):
    """Testa a conclusão de uma tarefa no banco de dados."""
    organizador_db.adicionar_tarefa("Física", 2.5)
    tarefas_antes = organizador_db.listar_tarefas()
    tarefa_id = tarefas_antes[0]["id"]

    resultado = organizador_db.concluir_tarefa(tarefa_id)
    assert resultado is True

    tarefas_depois = organizador_db.listar_tarefas()
    assert tarefas_depois[0]["concluida"]

def test_concluir_tarefa_inexistente(organizador_db):
    """Testa a tentativa de concluir uma tarefa com ID inexistente.""" 
    resultado = organizador_db.concluir_tarefa(999)
    assert resultado is False

def test_fluxo_conclusao_com_api(organizador_db):
    """Valida se o fluxo de conclusão de tarefa integra corretamente com a chamada da API."""
    organizador_db.adicionar_tarefa("Química", 1.0)
    tarefas_antes = organizador_db.listar_tarefas()
    tarefa_id = tarefas_antes[0]["id"]
    
    # Ao concluir, a lógica deve funcionar sem erros, mesmo chamando a API internamente
    resultado = organizador_db.concluir_tarefa(tarefa_id)
    assert resultado is True
    
    tarefas_depois = organizador_db.listar_tarefas()
    assert tarefas_depois[0]["concluida"] is True
    # A chamada da API é interna ao método, não precisamos testar o retorno aqui, apenas que não quebrou

def test_remover_tarefas_concluidas(organizador_db):
    """Testa a remoção de tarefas que foram marcadas como concluídas."""
    # Adiciona duas tarefas
    organizador_db.adicionar_tarefa("Tarefa 1", 1)
    organizador_db.adicionar_tarefa("Tarefa 2", 2)
    
    # Conclui a primeira
    tarefas = organizador_db.listar_tarefas()
    organizador_db.concluir_tarefa(tarefas[0]["id"])
    
    # Remove as concluídas
    removidas = organizador_db.remover_tarefas_concluidas()
    assert removidas == 1
    
    # Verifica se sobrou apenas a tarefa não concluída
    tarefas_restantes = organizador_db.listar_tarefas()
    assert len(tarefas_restantes) == 1
    assert tarefas_restantes[0]["materia"] == "Tarefa 2"