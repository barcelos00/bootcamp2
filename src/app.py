import requests
import sys
import sqlite3

if sys.platform == "win32":
    import os
    os.system("chcp 65001 > nul")

class EstudoOrganizer:
    def __init__(self, db_path="estudos.db", conn=None):
        self.db_path = db_path
        self._external_conn = conn # Store external connection for testing
        self._init_db()

    def _get_db_connection(self):
        if self._external_conn:
            return self._external_conn
        return sqlite3.connect(self.db_path)

    def _close_db_connection(self, conn):
        if not self._external_conn:
            conn.close()

    def _init_db(self):
        conn = self._get_db_connection()
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;") # Enable foreign key support
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                materia TEXT NOT NULL,
                horas REAL NOT NULL,
                concluida INTEGER NOT NULL DEFAULT 0
            )
        """)
        conn.commit()
        self._close_db_connection(conn)

    def adicionar_tarefa(self, materia, horas):
        if horas <= 0:
            raise ValueError("O tempo de estudo deve ser maior que zero.")
        conn = self._get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarefas (materia, horas, concluida) VALUES (?, ?, ?)", (materia, horas, 0))
        conn.commit()
        self._close_db_connection(conn)
        return f"OK: Tarefa de {materia} adicionada com sucesso!"

    def listar_tarefas(self):
        conn = self._get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, materia, horas, concluida FROM tarefas")
        tarefas_db = cursor.fetchall()
        self._close_db_connection(conn)
        # Convertendo para o formato original para compatibilidade
        tarefas = []
        for id, materia, horas, concluida in tarefas_db:
            tarefas.append({"id": id, "materia": materia, "horas": horas, "concluida": bool(concluida)})
        return tarefas

    def concluir_tarefa(self, tarefa_id):
        conn = self._get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (tarefa_id,))
        conn.commit()
        rows_affected = cursor.rowcount
        self._close_db_connection(conn)
        return rows_affected > 0

    def remover_tarefas_concluidas(self):
        conn = self._get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE concluida = 1")
        conn.commit()
        rows_affected = cursor.rowcount
        self._close_db_connection(conn)
        return rows_affected

    def obter_conselho_motivacional(self):
        """Consome a API pública Advice Slip para retornar um conselho."""
        try:
            response = requests.get("https://api.adviceslip.com/advice", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return data["slip"]["advice"]
            return "Continue focado nos seus estudos!"
        except Exception:
            return "O sucesso e a soma de pequenos esforcos repetidos dia apos dia."

def menu():
    organizador = EstudoOrganizer()
    
    while True:
        print("\n=== ORGANIZADOR DE ESTUDOS ===")
        print("1. Adicionar Materia")
        print("2. Listar Meus Estudos")
        print("3. Concluir Materia")
        print("4. Remover Materias Concluidas")
        print("5. Obter Frase Motivacional (API)")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
            materia = input("Qual materia voce vai estudar? ")
            try:
                horas = float(input("Quantas horas pretende dedicar? "))
                print(organizador.adicionar_tarefa(materia, horas))
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            tarefas = organizador.listar_tarefas()
            if not tarefas:
                print("Nenhuma tarefa agendada.")
            for t in tarefas:
                status = "[CONCLUIDO]" if t["concluida"] else "[ESTUDANDO]"
                print(f"{status} {t['materia']} - {t['horas']}h (ID: {t['id']})")

        elif opcao == "3":
            try:
                entrada = input("Digite o ID da tarefa para concluir: ")
                tarefa_id = int(entrada)
                if organizador.concluir_tarefa(tarefa_id):
                    print("Parabens por concluir mais um estudo!")
                    print(f"Dica do dia (API): {organizador.obter_conselho_motivacional()}")
                else:
                    print("Tarefa nao encontrada.")
            except ValueError:
                print("Por favor, digite um numero valido.")

        elif opcao == "4":
            removidas = organizador.remover_tarefas_concluidas()
            print(f"Sucesso: {removidas} tarefas concluidas foram removidas!")

        elif opcao == "5":
            print(f"\nConselho para voce: {organizador.obter_conselho_motivacional()}")

        elif opcao == "6":
            print("Ate logo! Bons estudos!")
            break

if __name__ == "__main__":
    menu()