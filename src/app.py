import requests
import sys

if sys.platform == "win32":
    import os
    os.system('chcp 65001 > nul')

class EstudoOrganizer:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, materia, horas):
        if horas <= 0:
            raise ValueError("O tempo de estudo deve ser maior que zero.")
        tarefa = {"materia": materia, "horas": horas, "concluida": False}
        self.tarefas.append(tarefa)
        return f"OK: Tarefa de {materia} adicionada com sucesso!"

    def listar_tarefas(self):
        return self.tarefas

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["concluida"] = True
            return True
        return False

    def obter_conselho_motivacional(self):
        """Consome a API pública Advice Slip para retornar um conselho."""
        try:
            response = requests.get("https://api.adviceslip.com/advice", timeout=5 )
            if response.status_code == 200:
                data = response.json()
                return data['slip']['advice']
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
        print("4. Obter Frase Motivacional (API)")
        print("5. Sair")
        
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
            for i, t in enumerate(tarefas):
                status = "[CONCLUIDO]" if t["concluida"] else "[ESTUDANDO]"
                print(f"{i}. {status} {t['materia']} - {t['horas']}h")

        elif opcao == "3":
            try:
                entrada = input("Digite o numero da tarefa para concluir: ")
                indice = int(entrada)
                if organizador.concluir_tarefa(indice):
                    print("Parabens por concluir mais um estudo!")
                    print(f"Dica do dia (API): {organizador.obter_conselho_motivacional()}")
                else:
                    print("Tarefa nao encontrada.")
            except ValueError:
                print("Por favor, digite um numero valido.")

        elif opcao == "4":
            print(f"\nConselho para voce: {organizador.obter_conselho_motivacional()}")

        elif opcao == "5":
            print("Ate logo! Bons estudos!")
            break

if __name__ == "__main__":
    menu()
