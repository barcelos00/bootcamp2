class EstudoOrganizer:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, materia, horas):
        if horas <= 0:
            raise ValueError("O tempo de estudo deve ser maior que zero.")
        tarefa = {"materia": materia, "horas": horas, "concluida": False}
        self.tarefas.append(tarefa)
        return f"✅ Tarefa de {materia} adicionada com sucesso!"

    def listar_tarefas(self):
        return self.tarefas

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["concluida"] = True
            return True
        return False

def menu():
    organizador = EstudoOrganizer()
    
    while True:
        print("\n ORGANIZADOR DE ESTUDOS ")
        print("1. Adicionar Matéria")
        print("2. Listar Meus Estudos")
        print("3. Concluir Matéria")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            materia = input("Qual matéria você vai estudar? ")
            try:
                horas = float(input("Quantas horas pretende dedicar? "))
                print(organizador.adicionar_tarefa(materia, horas))
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            tarefas = organizador.listar_tarefas()
            if not tarefas:
                print("📭 Nenhuma tarefa agendada.")
            for i, t in enumerate(tarefas):
                status = "✅" if t["concluida"] else "⏳"
                print(f"{i}. [{status}] {t['materia']} - {t['horas']}h")

        elif opcao == "3":
            indice = int(input("Digite o número da tarefa para concluir: "))
            if organizador.concluir_tarefa(indice):
                print("🎉 Parabéns por concluir mais um estudo!")
            else:
                print("❌ Tarefa não encontrada.")

        elif opcao == "4":
            print("Até logo! Bons estudos! 📖")
            break

if __name__ == "__main__":
    menu()
