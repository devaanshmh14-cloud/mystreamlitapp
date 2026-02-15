import streamlit as st
import base64

st.set_page_config(
    page_title="GCSE Study Resources",
    page_icon="https://emojis.wiki/books/",
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
    '<h1 class="float-title">Religious Studies</h1>',
    unsafe_allow_html=True
)
st.write("Welcome! Here you will find all the material needed to ace your religious studies exam. All  the resources uploaded has helped me get a grade 9 so you can fully rely on them. Thanks for trusting us with your revision and hopefully you benefit from these resources. This is for **AQA Religious Studies Short Course!**")
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
    st.switch_page("pages/Religious-Studies.py")
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
    st.switch_page("pages/Computer-Science.py")
if st.sidebar.button("Further Maths", width=100000):
    st.switch_page("pages/Further-Maths.py")
st.sidebar.title("Home Redirect")
st.sidebar.write("Press this button to go back to the home page. Thanks for visiting!")
if st.sidebar.button("Home", width=100000):
    st.switch_page("app.py")
st.set_page_config(layout="wide")
def display_pdf(file_path):
    """Display PDF in Streamlit"""
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
st.markdown(
    '<h2 class="float-title">2024 Past Papers</h2>',
    unsafe_allow_html=True
)
if 'selected_pdf' not in st.session_state:
    st.session_state.selected_pdf = None

if st.button("June 2024 Section 1: Buddhism", width=110000):
    st.session_state.selected_pdf = "pdfs/re.bub.pdf"
if st.button("June 2024 Section 2: Christianity", width=110000):
    st.session_state.selected_pdf = "pdfs/re.chri.pdf"
if st.button("June 2024 Section 5: Thematics", width=110000):
    st.session_state.selected_pdf = ("pdfs/re.the.pdf")

st.markdown(
    '<h2 class="float-title">2024 Mark Schemes</h2>',
    unsafe_allow_html=True
)

if st.button("June 2024 Mark Scheme: Buddhism", width=110000):
    st.session_state.selected_pdf = "pdfs/re.bms.pdf"
if st.button("June 2024 Mark Scheme: Christianity", width=110000):
    st.session_state.selected_pdf = "pdfs/re.chms.pdf"
if st.button("June 2024 Mark Scheme: Thematics", width=110000):
    st.session_state.selected_pdf = "pdfs/re.tms.pdf"

if st.session_state.selected_pdf:
    display_pdf(st.session_state.selected_pdf)

st.markdown(
    '<h2 class="float-title">Useful Youtube Videos</h2>',
    unsafe_allow_html=True
)

if 'selected_video' not in st.session_state:
    st.session_state.selected_video = None

if st.button("Religion 1: Christianity", width=110000):
    st.session_state.selected_video = "https://youtu.be/Fad9NuKcDdo?si=wpOOGWZEmrphXi5Q"

if st.button("Religion 2: Buddhism", width=110000):
    st.session_state.selected_video = "https://youtu.be/VBCH9q87_I4?si=8JyVqzeBYiUYSAc2"

if st.button("Theme: Family + Relationships", width=110000):
    st.session_state.selected_video = "https://youtu.be/Tu0wjvGUBdA?si=e8_2XS0jAdLE-xh1"

if st.button("Exam Practice: 12 Marker", width=110000):
    st.session_state.selected_video = "https://youtu.be/2rYfpLWrb0U?si=h0MSGWjFFt5_RcVp"

if st.button("Exam Practice: 6 Marker", width=110000):
    st.session_state.selected_video = "https://youtu.be/f2yKMtprdOY?si=3cz3PWSQf3lhASro"

if st.session_state.selected_video:
    st.video(st.session_state.selected_video)