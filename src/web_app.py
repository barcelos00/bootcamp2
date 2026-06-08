import streamlit as st
from app import EstudoOrganizer

st.set_page_config(page_title="Estudo Organizer", page_icon="📚")

if 'organizador' not in st.session_state:
    st.session_state.organizador = EstudoOrganizer()

st.title("Estudo Organizer 📚")
st.subheader("Organize seus estudos com o Supabase!")

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
            except Exception as e:
                st.error(f"Erro ao salvar no banco: {e}")
        else:
            st.error("Digite o nome da matéria!")

# Busca tarefas
tarefas = st.session_state.organizador.listar_tarefas()

# --- MÉTRICAS ---
total = len(tarefas)
concluidas = len([t for t in tarefas if t["concluida"]])
pendentes = total - concluidas
total_horas = sum(t["horas"] for t in tarefas)

col1, col2, col3, col4 = st.columns(4)
col1.metric("📋 Total", total)
col2.metric("✅ Concluídas", concluidas)
col3.metric("📖 Pendentes", pendentes)
col4.metric("⏱️ Total de Horas", f"{total_horas}h")

st.divider()

# --- FILTROS ---
st.header("Meus Estudos")
filtro = st.radio("Filtrar por:", ["Todas", "Pendentes", "Concluídas"], horizontal=True)

if filtro == "Pendentes":
    tarefas_filtradas = [t for t in tarefas if not t["concluida"]]
elif filtro == "Concluídas":
    tarefas_filtradas = [t for t in tarefas if t["concluida"]]
else:
    tarefas_filtradas = tarefas

if not tarefas_filtradas:
    st.info("Nenhuma tarefa encontrada.")
else:
    for t in tarefas_filtradas:
        col1, col2 = st.columns([3, 1])
        status = "✅" if t["concluida"] else "📖"
        col1.write(f"{status} **{t['materia']}** - {t['horas']}h")

        if not t["concluida"]:
            if col2.button("Concluir", key=f"btn_{t['id']}"):
                st.session_state.organizador.concluir_tarefa(t["id"])
                st.balloons()
                st.rerun()

st.divider()

if st.button("💡 Obter Conselho Rápido"):
    st.success(f"**Dica de hoje:** {st.session_state.organizador.obter_conselho_motivacional()}")

if st.button("🗑️ Remover Concluídas"):
    removidas = st.session_state.organizador.remover_tarefas_concluidas()
    if removidas > 0:
        st.success(f"✅ {removidas} tarefas concluídas foram removidas!")
        st.rerun()
    else:
        st.info("Nenhuma tarefa concluída para remover.")