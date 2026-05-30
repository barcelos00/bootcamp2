import pytest
from unittest.mock import MagicMock
from src.app import EstudoOrganizer

@pytest.fixture
def organizador_mock(monkeypatch):
    # Injeta variáveis de ambiente falsas para o teste passar na validação do __init__
    monkeypatch.setenv("SUPABASE_URL", "http://mock-url.com")
    monkeypatch.setenv("SUPABASE_KEY", "mock-key")
    
    # Cria a instância e substitui o cliente supabase por um mock
    organizador = EstudoOrganizer()
    organizador.supabase = MagicMock()
    return organizador

def test_adicionar_tarefa_sucesso(organizador_mock):
    # Simula o retorno do Supabase
    organizador_mock.supabase.table().insert().execute.return_value = MagicMock(data=[])
    
    resultado = organizador_mock.adicionar_tarefa("Matemática", 2.0)
    assert "OK" in resultado
    organizador_mock.supabase.table().insert.assert_called()

def test_listar_tarefas(organizador_mock):
    # Simula dados retornados pelo Supabase
    mock_data = [{"id": 1, "materia": "História", "horas": 1.0, "concluida": False}]
    organizador_mock.supabase.table().select().order().execute.return_value = MagicMock(data=mock_data)
    
    tarefas = organizador_mock.listar_tarefas()
    assert len(tarefas) == 1
    assert tarefas[0]["materia"] == "História"

def test_concluir_tarefa(organizador_mock):
    # Simula sucesso na atualização
    organizador_mock.supabase.table().update().eq().execute.return_value = MagicMock(data=[{"id": 1}])
    
    resultado = organizador_mock.concluir_tarefa(1)
    assert resultado is True