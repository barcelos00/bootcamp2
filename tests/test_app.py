import pytest
from src.app import EstudoOrganizer

def test_adicionar_tarefa_sucesso():
    organizador = EstudoOrganizer()
    resultado = organizador.adicionar_tarefa("Matemática", 2)
    assert len(organizador.listar_tarefas()) == 1
    assert "sucesso" in resultado

def test_adicionar_tarefa_erro_horas_negativas():
    organizador = EstudoOrganizer()
    with pytest.raises(ValueError):
        organizador.adicionar_tarefa("História", -1)
