import requests
import os
from dotenv import load_dotenv
from supabase import create_client

# Carrega as variáveis de ambiente
load_dotenv()

class EstudoOrganizer:
    def __init__(self):
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        if not url or not key:
            raise Exception("SUPABASE_URL e SUPABASE_KEY são necessários.")
        self.supabase = create_client(url, key)

    def adicionar_tarefa(self, materia, horas):
        if horas <= 0:
            raise ValueError("O tempo de estudo deve ser maior que zero.")
        
        data = {"materia": materia, "horas": horas, "concluida": False}
        self.supabase.table("tarefas").insert(data).execute()
        return f"OK: Tarefa de {materia} adicionada com sucesso!"

    def listar_tarefas(self):
        # Busca no Supabase ordenando pelo ID
        response = self.supabase.table("tarefas").select("*").order("id").execute()
        return response.data

    def concluir_tarefa(self, tarefa_id):
        response = self.supabase.table("tarefas").update({"concluida": True}).eq("id", tarefa_id).execute()
        return len(response.data) > 0

    def remover_tarefas_concluidas(self):
        response = self.supabase.table("tarefas").delete().eq("concluida", True).execute()
        return len(response.data)

    def obter_conselho_motivacional(self):
        try:
            response = requests.get("https://api.adviceslip.com/advice", timeout=5)
            if response.status_code == 200:
                return response.json()["slip"]["advice"]
            return "Continue focado nos seus estudos!"
        except Exception:
            return "O sucesso e a soma de pequenos esforcos repetidos dia apos dia."