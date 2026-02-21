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
    '<h1 class="float-title">Religious Studies AQA (Short Course)</h1>',
    unsafe_allow_html=True
)

st.write("Welcome! This page contains all the resources for your success in **AQA GCSE Religious Studies Short Course**. There are all things from past papers to notes. I hope you make good use of them to get a grade 9 in your exam. Enjoy!")

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

if st.button("Helpful Videos", width=110000):
    st.session_state.show_video = not st.session_state.show_video
    st.session_state.show_past_papers = False
    st.session_state.show_mark_schemes = False
    st.session_state.selected_pdf = None
    st.session_state.selected_video = None

if st.session_state.show_past_papers:
    st.markdown('<h2 class="float-title">Past Papers</h2>', unsafe_allow_html=True)
    if st.button("Specimen Section 1: Buddhism", width=110000):
        pdf_url = "https://drive.google.com/file/d/1-kutIMn3M9bsQHYt5shR29foo0_XOBy4/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Specimen Section 2: Christianity", width=110000):
        pdf_url = "https://drive.google.com/file/d/17Wpn-MTvcxyr9si_L4gxuWDGAcCDcGJt/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Specimen Section 3: Islam", width=110000):
        pdf_url = "https://drive.google.com/file/d/1R8fWZBNTWq49hzgcVHzjRtXh5T73_lg-/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Specimen Section 4: Judaism", width=110000):
        pdf_url = "https://drive.google.com/file/d/19RyJK9e5nJDsFZiKyVEMdPiOlc1MEYN/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Specimen Section 5: Thematics", width=110000):
        pdf_url = "https://drive.google.com/file/d/1GP38TMIZK4HAuY0YRJC1ii3P4dMHnzt3/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.session_state.selected_pdf:
        st.markdown(f'<iframe src="{st.session_state.selected_pdf}" width="100%" height="800"></iframe>', unsafe_allow_html=True)

if st.session_state.show_mark_schemes:
    st.markdown('<h2 class="float-title">Mark Schemes</h2>', unsafe_allow_html=True)
    if st.button("Specimen Mark Scheme: Buddhism", width=110000):
        pdf_url = "https://drive.google.com/file/d/1BMGHMznoV8La0-mvXa5AjktkXa40kb59/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Specimen Mark Scheme: Christianity", width=110000):
        pdf_url = "https://drive.google.com/file/d/1YnKsjoYVPHbZA2VDHrrKOpQefYYCarsE/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Specimen Mark Scheme: Islam", width=110000):
        pdf_url = "https://drive.google.com/file/d/1je4gEYiViESaJx1jYRCMr8UHrpgl5NB_/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Specimen Mark Scheme: Judaism", width=110000):
        pdf_url = "https://drive.google.com/file/d/1sEjTu4KwK7-_0YEPIVrVW-qtd3tBEROF/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Specimen Mark Scheme: Thematics", width=110000):
        pdf_url = "https://drive.google.com/file/d/1T5UR0o7mFYPf8LlzO3mRNiHHjoiaYq8n/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.session_state.selected_pdf:
        st.markdown(f'<iframe src="{st.session_state.selected_pdf}" width="100%" height="800"></iframe>', unsafe_allow_html=True)

if st.session_state.show_video:
    st.markdown('<h2 class="float-title">Helpful Videos</h2>', unsafe_allow_html=True)
    if st.button("Religion 1: Christianity", width=110000):
        video_url = "https://youtu.be/Fad9NuKcDdo?si=wpOOGWZEmrphXi5Q"
        st.session_state.selected_video = None if st.session_state.selected_video == video_url else video_url
    if st.button("Religion 2: Buddhism", width=110000):
        video_url = "https://youtu.be/VBCH9q87_I4?si=8JyVqzeBYiUYSAc2"
        st.session_state.selected_video = None if st.session_state.selected_video == video_url else video_url
    if st.button("Religion 3: Islam", width=110000):
        video_url = "https://youtu.be/xtWlil5BqcY?si=tP2ULlgAH2jlje_7"
        st.session_state.selected_video = None if st.session_state.selected_video == video_url else video_url
    if st.button("Theme 1: Family + Relationships", width=110000):
        video_url = "https://youtu.be/Tu0wjvGUBdA?si=e8_2XS0jAdLE-xh1"
        st.session_state.selected_video = None if st.session_state.selected_video == video_url else video_url
    if st.button("Theme 2: Peace + Conflict", width=110000):
        video_url = "https://youtu.be/zjXeVC-Vhbw?si=Mtv-48Of8_tmlhUQ"
        st.session_state.selected_video = None if st.session_state.selected_video == video_url else video_url
    if st.button("Exam Practice: 6 Marker", width=110000):
        video_url = "https://youtu.be/f2yKMtprdOY?si=3cz3PWSQf3lhASro"
        st.session_state.selected_video = None if st.session_state.selected_video == video_url else video_url
    if st.button("Exam Practice: 12 Marker", width=110000):
        video_url = "https://youtu.be/2rYfpLWrb0U?si=h0MSGWjFFt5_RcVp"
        st.session_state.selected_video = None if st.session_state.selected_video == video_url else video_url
    if st.session_state.selected_video:
        st.video(st.session_state.selected_video)