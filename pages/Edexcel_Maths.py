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
    '<h1 class="float-title">Maths</h1>',
    unsafe_allow_html=True
)

st.write("Welcome! Here you will find all the material needed for your maths exam. All  the resources uploaded are free to access and use. Just click on the buttons to find the resources you need! If you have any suggestions for resources to add, please let me know in the contact form on the home page. Thanks for visiting!")

st.markdown(
    '<h2 class="float-title">Resources</h2>',
    unsafe_allow_html=True
)

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
st.sidebar.title("Home Redirect")
st.sidebar.write("Press this button to go back to the home page. Thanks for visiting!")
if st.sidebar.button("Home", width=100000):
    st.switch_page("app.py")
st.set_page_config(layout="wide")

if 'show_past_papers' not in st.session_state:
    st.session_state.show_past_papers = False
if 'show_mark_schemes' not in st.session_state:
    st.session_state.show_mark_schemes = False
if 'show_video' not in st.session_state:
    st.session_state.show_video = False
if 'selected_pdf' not in st.session_state:
    st.session_state.selected_pdf = None
if 'selected_video' not in st.session_state:
    st.session_state.selected_video = None


if st.button("Past Papers", width=110000):
    st.session_state.show_past_papers = not st.session_state.show_past_papers
    st.session_state.show_mark_schemes = False
    st.session_state.show_video = False
    st.session_state.selected_pdf = None
    st.session_state.selected_video = None

if st.button("Mark Schemes", width=110000):
    st.session_state.show_mark_schemes = not st.session_state.show_mark_schemes
    st.session_state.show_past_papers = False
    st.session_state.show_video = False
    st.session_state.selected_pdf = None
    st.session_state.selected_video = None

if st.button("Helpful Video Course", width=110000):
    st.session_state.show_video = not st.session_state.show_video
    st.session_state.show_past_papers = False
    st.session_state.show_mark_schemes = False
    st.session_state.selected_pdf = None
    st.session_state.selected_video = None

if st.session_state.show_past_papers:
    st.markdown('<h2 class="float-title">Past Papers</h2>', unsafe_allow_html=True)
    if st.button("Paper 1: Non-Calculator (Foundation)", width=110000):
        pdf_url = "https://drive.google.com/file/d/1Fu_IgEqq2K0guSYqD7eNExLcaPzRAI4w/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 1: Non-Calculator (Higher)", width=110000):
        pdf_url = "https://drive.google.com/file/d/1uwJEKoGEIGera2EinHyFLZaMsRoVuSoF/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 2: Calculator (Foundation)", width=110000):
        pdf_url = "https://drive.google.com/file/d/1SGtNimji5q_t8XOpLoZ4MCGXZt_5wLbJ/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 2: Calculator (Higher)", width=110000):
        pdf_url = "https://drive.google.com/file/d/13GOMMJCi_Fthi0pWPW8EPtrq3d9IHsuT/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 3: Calculator (Foundation)", width=110000):
        pdf_url = "https://drive.google.com/file/d/1zXsefPw250uELQEtmCRCoyi6aXcRhgIN/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 3: Calculator (Higher)", width=110000):
        pdf_url = "https://drive.google.com/file/d/1uQxqCpzX79KZjfwwAhcQ9-3NY6PwoiaD/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.session_state.selected_pdf:
        st.markdown(f'<iframe src="{st.session_state.selected_pdf}" width="100%" height="800"></iframe>', unsafe_allow_html=True)

if st.session_state.show_mark_schemes:
    st.markdown('<h2 class="float-title">Mark Schemes</h2>', unsafe_allow_html=True)
    if st.button("Paper 1: Non-Calculator (Foundation)", width=110000):
        pdf_url = "https://drive.google.com/file/d/1nUJd17POQ64XlEfyS6z0Sk5TtYDd53--/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 1: Non-Calculator (Higher)", width=110000):
        pdf_url = "https://drive.google.com/file/d/13eQXFsXQRoJRNM__ye9Df-yR7NE3Itkt/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 2: Calculator (Foundation)", width=110000):
        pdf_url = "https://drive.google.com/file/d/12uuHRY2sJo5ahkF6rf__aWEBpIanKIH4/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 2: Calculator (Higher)", width=110000):
        pdf_url = "https://drive.google.com/file/d/1oVQQHJUAl3B2hVumCFFLrvseqla8n2BH/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 3: Calculator (Foundation)", width=110000):
        pdf_url = "https://drive.google.com/file/d/1B-gjkSTjEeyWWvBTfBKiRG5jBVWFVo_2/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 3: Calculator (Higher)", width=110000):
        pdf_url = "https://drive.google.com/file/d/1v-C24ctmEeuVukqWcD2Dh6idjDL7Y3F0/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.session_state.selected_pdf:
        st.markdown(f'<iframe src="{st.session_state.selected_pdf}" width="100%" height="800"></iframe>', unsafe_allow_html=True)
if st.session_state.show_video:
    st.markdown('<h2 class="float-title">Helpful Video Course</h2>', unsafe_allow_html=True)
    
    video_url = "https://youtube.com/playlist?list=PLidqqIGKox7XPh1QacLRiKto_UlnRIEVh&si=n7HWeu8K8KtftmOk"
    
    st.markdown(
        f'''
        <a href="{video_url}" target="_blank" style="text-decoration: none;">
            <button style="
                width: 100%; 
                padding: 0.5rem 1rem; 
                background-color: #55828B; 
                color: #C9E4CA; 
                border: none; 
                border-radius: 0.5rem; 
                cursor: pointer; 
                font-size: 1rem;
            ">9-1 Maths</button>
        </a>
        ''',
        unsafe_allow_html=True
    )