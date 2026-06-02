import streamlit as st

st.set_page_config(
    page_title="GCSE Study Resources",
    page_icon="📚",
)

PALETTE = {
    "bg": "#C9E4CA",
    "card": "#87BBA2",
    "primary": "#55828B",
    "accent": "#3B6064",
    "text": "#364958"
}

st.markdown(f"""
<style>
.stApp {{
    background-color: {PALETTE["bg"]};
    color: {PALETTE["text"]};
}}

h1 {{
    color: {PALETTE["accent"]};
}}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>
[data-testid="stSidebar"] {{
    background-color: {PALETTE["card"]};
    color: {PALETTE["text"]};
}}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>
[data-testid="stHeader"] {{
    background-color: {PALETTE["card"]};
}}


.block-container {{
    padding-top: 1rem;
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
button {
    background-color: #55828B !important;  
    color: #C9E4CA !important;             
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes floatUp {
    from {
        transform: translateY(20px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.float-title {
    animation: floatUp 1.0s ease-out;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<h1 class="float-title"> GCSE Study Resources</h1>',
    unsafe_allow_html=True
)
st.write("Welcome to the GCSE Study Resources! This website is designed to provide you with comprehensive resources for all your GCSE subjects. Whether you're looking for mark schemes, practice questions, or video tutorials, we've got you covered. Just select a subject from the sidebar to get started!")
st.set_page_config(page_title="GCSE Study Resource")
st.markdown("""
        <style>
            [data-testid="stSidebarNav"] {
                display: none;
            }
        </style>
""", unsafe_allow_html=True)
st.sidebar.title("**Subjects**")
st.sidebar.write("This contains all the subjects available! Just click to find all the resources")
if st.sidebar.button("Religious Studies", width=100000):
    st.switch_page("pages/Religious_Studies.py")
if st.sidebar.button("Biology", width=100000):
    st.switch_page("pages/Biology.py")
if st.sidebar.button("Chemistry", width=100000):
    st.switch_page("pages/Chemistry.py")
if st.sidebar.button("Physics", width=100000):
    st.switch_page("pages/Physics.py")
if st.sidebar.button("Economics", width=100000):
    st.switch_page("pages/Economics.py")
if st.sidebar.button("Maths", width=100000):
    st.switch_page("pages/Maths.py")
if st.sidebar.button("English", width=100000):
    st.switch_page("pages/English.py")
if st.sidebar.button("Further Maths", width=100000):
    st.switch_page("pages/Further_Maths.py")
st.set_page_config(layout="wide")

if st.button("Religious Studies", width=100000):
    st.switch_page("pages/Religious_Studies.py")
if st.button("Biology", width=100000):
    st.switch_page("pages/Biology.py")
if st.button("Chemistry", width=100000):
    st.switch_page("pages/Chemistry.py")
if st.button("Physics", width=100000):
    st.switch_page("pages/Physics.py")
if st.button("Economics", width=100000):
    st.switch_page("pages/Economics.py")
if st.button("Maths", width=100000):
    st.switch_page("pages/Maths.py")
if st.button("English", width=100000):
    st.switch_page("pages/English.py")
if st.button("Further Maths", width=100000):
    st.switch_page("pages/Further_Maths.py")