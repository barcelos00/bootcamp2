import pytest
import sqlite3
from src.app import EstudoOrganizer

@pytest.fixture
def organizador_app_db():
    conn = sqlite3.connect(":memory:")
    organizador = EstudoOrganizer(conn=conn)
    yield organizador
    conn.close()

def test_adicionar_tarefa_sucesso(organizador_app_db):
    """Testa se a tarefa é adicionada corretamente."""
    resultado = organizador_app_db.adicionar_tarefa("Matemática", 2)
    assert "OK: Tarefa de Matemática adicionada com sucesso!" in resultado
    assert len(organizador_app_db.listar_tarefas()) == 1

def test_adicionar_tarefa_erro_horas_negativas():
    """Testa se a adição de tarefa com horas negativas levanta ValueError."""
    organizador = EstudoOrganizer(db_path=":memory:") # Use in-memory for this test too
    with pytest.raises(ValueError, match="O tempo de estudo deve ser maior que zero."):
        organizador.adicionar_tarefa("História", -1)