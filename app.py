import streamlit as st

st.set_page_config(page_title="AI Agent Dashboard", layout="wide")

st.title("🤖 AI Agent Dashboard")
st.write("Welcome! Use the sidebar to select a tool.")

st.markdown("""
### Available Tools:
- 📄 **PDF Analysis** — Chat with your PDFs.
- 📊 **CSV Analysis** — Explore and query your CSV data.
- 📝 **Task Planner** — Plan and track your daily tasks.
""")

st.sidebar.title("Select a Tool")
st.sidebar.button("PDF Analysis", on_click=lambda: st.switch_page("pages\pdf_ui.py"))

st.sidebar.button("CSV Analysis", on_click=lambda: st.switch_page("pages\csv_ui.py"))

st.sidebar.button("Task Planner", on_click=lambda: st.switch_page("pages\planner_ui.py"))