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
    '<h1 class="float-title">Biology Edexcel</h1>',
    unsafe_allow_html=True
)

st.write("Welcome! This page contains all the resources for your success in Edexcel GCSE Biology. All the resources uploaded are free to access and use. I hope you found it helpful!")

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
    if st.button("Paper 1 (Foundation) 1BI0/1F", width=110000):
        pdf_url = "https://drive.google.com/file/d/1GMZ4GsS-9zdo2Wmsk-hJ_FA-jmp30lqf/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 1 (Higher) 1BI0/1H", width=110000):
        pdf_url = "https://drive.google.com/file/d/1wtQCgDpAQ0PrMNq_qKIEDIkyoW9Fl2X7/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("June 2024 Paper 1 (Foundation) 1BI0/1F", width=110000):
        pdf_url = "https://drive.google.com/file/d/11OJos_8-wdz4o67exk0D6XXOJpMFsxQr/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("June 2024 Paper 1 (Higher) 1BI0/1H", width=110000):
        pdf_url = "https://drive.google.com/file/d/19gat0tA2yehmyoEyCuTRfl3cQ5gxvfa7/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("June 2024 Paper 2 (Foundation) 1BI0/2F", width=110000):
        pdf_url = "https://drive.google.com/file/d/12TwjdU8uZ2R8gf4BW9CY2T68gL-46h1N/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.session_state.selected_pdf:
        st.markdown(f'<iframe src="{st.session_state.selected_pdf}" width="100%" height="800"></iframe>', unsafe_allow_html=True)

if st.session_state.show_mark_schemes:
    st.markdown('<h2 class="float-title">Mark Schemes</h2>', unsafe_allow_html=True)
    if st.button("Paper 1 (Foundation) 1BI0/1F", width=110000):
        pdf_url = "https://drive.google.com/file/d/1M9Tbb6Z7CHd9hFN4CO2jnr3KhDInvfRF/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("Paper 1 (Higher) 1BI0/1H", width=110000):
        pdf_url = "https://drive.google.com/file/d/1ciE6EzBywVQbrhoSt3M10Ngpkb3HBksA/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("June 2024 Paper 1 (Foundation) 1BI0/1F", width=110000):
        pdf_url = "https://drive.google.com/file/d/1VCnPBxzMS-ggJ3JPwNNsAVDrP0aSFveu/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("June 2024 Paper 1 (Higher) 1BI0/1H", width=110000):
        pdf_url = "https://drive.google.com/file/d/1edjfUhYrNkB47X8XUuiqD887w3CEZn8o/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.button("June 2024 Paper 2 (Foundation) 1BI0/2F", width=110000):
        pdf_url = "https://drive.google.com/file/d/1SrcqDknvQTTUaIeHcRb1zIUHr_vjjt53/preview"
        st.session_state.selected_pdf = None if st.session_state.selected_pdf == pdf_url else pdf_url
    if st.session_state.selected_pdf:
        st.markdown(f'<iframe src="{st.session_state.selected_pdf}" width="100%" height="800"></iframe>', unsafe_allow_html=True)

if st.session_state.show_video:
    st.markdown('<h2 class="float-title">Helpful Video Course</h2>', unsafe_allow_html=True)
    
    video_url = "https://youtube.com/playlist?list=PLidqqIGKox7X5UFT-expKIuR-i-BN3Q1g&si=yooNAdvtT0d-6VxH"
    
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
            ">GCSE 9-1 Biology</button>
        </a>
        ''',
        unsafe_allow_html=True
    )