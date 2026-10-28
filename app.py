from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SignChord Piano", page_icon="🎹", layout="wide")

# Kurangi ruang kosong bawaan Streamlit supaya aplikasi tampil lebih luas
st.markdown(
    """
    <style>
      header[data-testid="stHeader"] { display: none; }
      .stApp { background: #e8ebf1; }
      .block-container { padding: 0 !important; max-width: 100%; }
      iframe { border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"

if not html_path.exists():
    st.error("File index.html tidak ditemukan. Letakkan index.html di folder yang sama dengan app.py.")
    st.stop()

html = html_path.read_text(encoding="utf-8")

# Ubah angka height bila tampilan terpotong atau terlalu panjang
components.html(html, height=1500, scrolling=True)
