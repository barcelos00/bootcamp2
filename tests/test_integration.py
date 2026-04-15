from src.app import EstudoOrganizer

def test_obter_conselho_api_sucesso():
    """Teste de integração que valida a comunicação com a API Advice Slip."""
    organizador = EstudoOrganizer()
    conselho = organizador.obter_conselho_motivacional()
    
    # Verifica se o retorno é uma string e não está vazio
    assert isinstance(conselho, str)
    assert len(conselho) > 0
    assert conselho != ""

def test_fluxo_conclusao_com_api():
    """Valida se o fluxo de conclusão de tarefa integra corretamente com a chamada da API."""
    organizador = EstudoOrganizer()
    organizador.adicionar_tarefa("Python", 2)
    
    # Ao concluir, a lógica deve funcionar sem erros, mesmo chamando a API internamente
    resultado = organizador.concluir_tarefa(0)
    assert resultado is True
    assert organizador.listar_tarefas()[0]["concluida"] is True
