import streamlit as st
import base64
import os

# THIS MUST BE FIRST - ONLY ONCE
st.set_page_config(
    page_title="Religious Studies - GCSE Study Resources",
    page_icon="📚",
    layout="wide"
)

# DEBUG CODE
st.title("🔍 DEBUG INFO")
st.write("**Current directory:**", os.getcwd())
st.write("**Files in root:**", os.listdir("."))

if os.path.exists("pdfs_religious_studies"):
    st.write("**✅ pdfs_religious_studies folder EXISTS**")
    st.write("**Files inside:**", os.listdir("pdfs_religious_studies"))
else:
    st.write("**❌ pdfs_religious_studies folder NOT FOUND**")

# Check for any PDF folders
all_items = os.listdir(".")
pdf_folders = [item for item in all_items if 'pdf' in item.lower()]
st.write("**Folders with 'pdf' in name:**", pdf_folders)

st.markdown("---")

# Your styling
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
button {{
    background-color: #55828B !important;
    color: #C9E4CA !important;
}}
@keyframes floatUp {{
    from {{
        transform: translateY(20px);
        opacity: 0;
    }}
    to {{
        transform: translateY(0);
        opacity: 1;
    }}
}}
.float-title {{
    animation: floatUp 1.0s ease-out;
}}
[data-testid="stSidebar"] {{
    background-color: {PALETTE["card"]};
    color: {PALETTE["text"]};
}}
[data-testid="stHeader"] {{
    background-color: {PALETTE["card"]};
}}
.block-container {{
    padding-top: 1rem;
}}
[data-testid="stSidebarNav"] {{
    display: none;
}}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="float-title">Religious Studies</h1>', unsafe_allow_html=True)
st.write("Welcome! Here you will find all the material needed to ace your religious studies exam. All the resources uploaded has helped me get a grade 9 so you can fully rely on them. Thanks for trusting us with your revision and hopefully you benefit from these resources. This is for **AQA Religious Studies Short Course!**")

# Sidebar
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

# PDF display function
def display_pdf(file_path):
    """Display PDF in Streamlit"""
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Initialize session state
if 'selected_pdf' not in st.session_state:
    st.session_state.selected_pdf = None

# 2024 Past Papers
st.markdown('<h2 class="float-title">2025 Past Papers</h2>', unsafe_allow_html=True)

if st.button("June 2024 Section 1: Buddhism", width=110000):
    st.session_state.selected_pdf = "pdfs_religious_studies/re.bub.pdf"  # FIXED PATH
if st.button("June 2024 Section 2: Christianity", width=110000):
    st.session_state.selected_pdf = "pdfs_religious_studies/re.chri.pdf"  # FIXED PATH
if st.button("June 2024 Section 5: Thematics", width=110000):
    st.session_state.selected_pdf = "pdfs_religious_studies/re.the.pdf"  # FIXED PATH

# 2024 Mark Schemes
st.markdown('<h2 class="float-title">2024 Mark Schemes</h2>', unsafe_allow_html=True)

if st.button("June 2024 Mark Scheme: Buddhism", width=110000):
    st.session_state.selected_pdf = "pdfs_religious_studies/re.bms.pdf"  # FIXED PATH
if st.button("June 2024 Mark Scheme: Christianity", width=110000):
    st.session_state.selected_pdf = "pdfs_religious_studies/re.chms.pdf"  # FIXED PATH
if st.button("June 2024 Mark Scheme: Thematics", width=110000):
    st.session_state.selected_pdf = "pdfs_religious_studies/re.tms.pdf"  # FIXED PATH

# Display PDF with safety check
if st.session_state.selected_pdf:
    if os.path.exists(st.session_state.selected_pdf):
        display_pdf(st.session_state.selected_pdf)
    else:
        st.error(f"❌ File not found: {st.session_state.selected_pdf}")
        st.session_state.selected_pdf = None

# YouTube Videos
st.markdown('<h2 class="float-title">Useful Youtube Videos</h2>', unsafe_allow_html=True)

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