import streamlit as st
from app import EstudoOrganizer

st.set_page_config(page_title="Estudo Organizer", page_icon="📚")

# Inicializa o organizador com o banco de dados persistente
if 'organizador' not in st.session_state:
    st.session_state.organizador = EstudoOrganizer()

st.title("Estudo Organizer")
st.subheader("Organize seus estudos com motivação!")

with st.sidebar:
    st.header("Adicionar Nova Matéria")
    materia = st.text_input("Nome da Matéria")
    horas = st.number_input("Horas de Dedicação", min_value=0.5, step=0.5)
    if st.button("Adicionar"):
        if materia:
            try:
                msg = st.session_state.organizador.adicionar_tarefa(materia, horas)
                st.success(msg)
                st.rerun()
            except ValueError as e:
                st.error(f"Erro: {e}")
        else:
            st.error("Digite o nome da matéria!")

st.header("Meus Estudos")
tarefas = st.session_state.organizador.listar_tarefas()

if not tarefas:
    st.info("Nenhuma tarefa agendada. Use a barra lateral para adicionar!")
else:
    for t in tarefas:
        col1, col2 = st.columns([3, 1])
        status = "✅" if t["concluida"] else "📖"
        col1.write(f"{status} **{t['materia']}** - {t['horas']}h")
        
        if not t["concluida"]:
            if col2.button("Concluir", key=f"btn_{t['id']}"):
                st.session_state.organizador.concluir_tarefa(t["id"])
                st.balloons()
                conselho = st.session_state.organizador.obter_conselho_motivacional()
                st.info(f"🎉 Parabéns! Dica do dia: {conselho}")
                st.rerun()

# Botão para Frase Motivacional avulsa
st.divider()
if st.button("💡 Obter Conselho Rápido"):
    conselho = st.session_state.organizador.obter_conselho_motivacional()
    st.success(f"**Dica de hoje:** {conselho}")