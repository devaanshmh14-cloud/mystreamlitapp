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
/* Top header bar */
[data-testid="stHeader"] {{
    background-color: {PALETTE["card"]};
}}

/* Remove white gap above the app */
.block-container {{
    padding-top: 1rem;
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
button {
    background-color: #55828B !important;  /* your desired color */
    color: #C9E4CA !important;             /* text color */
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
st.write("Welcome! You have found the website with all the GCSE revision resources for most subjects. Here you will find not only notes but also past papers and key examiner reports you can make full use of. This website is full designed in order for any student to achieve a grade 9. The website contains all trusted materials which will be of use to every student. It also contains the grade boundaries of any past papers that you may have completed so that you can check where you stand. Overall I hope you find this as helpful as I do and use it to full extent. Enjoy!")
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
if st.sidebar.button("Geography", width=100000):
    st.switch_page("pages/Geography.py")
if st.sidebar.button("German", width=100000):
    st.switch_page("pages/German.py")
if st.sidebar.button("Maths", width=100000):
    st.switch_page("pages/Maths.py")
if st.sidebar.button("English", width=100000):
    st.switch_page("pages/English.py")
if st.sidebar.button("Computer Science", width=100000):
    st.switch_page("pages/Computer_Science.py")
if st.sidebar.button("Further Maths", width=100000):
    st.switch_page("pages/Further_Maths.py")
st.set_page_config(layout="wide")