import streamlit as st

from model.recommender import recommend_career
from services.voice_input import get_voice_text
from services.image_ocr import extract_text


st.set_page_config(
    page_title="CareerLens AI",
    page_icon="🎓",
    layout="wide"
)

# =========================
# GLOBAL CSS 
# =========================
st.markdown("""

<style>

/* APP BACKGROUND */
.stApp {
    background: linear-gradient(130deg, #2f80ed, #1c6ef2, #4facfe);
    font-family: 'Arial';
}

/* REMOVE DEFAULT PADDING */
.block-container {
    padding-top: 1.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #f4f7ff;
    border-right: 1px solid #e6eaf5;
}

/* HERO CARD */
.hero {
    background: rgba(255, 255, 255, 0.92);
    padding: 40px;
    border-radius: 25px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    text-align: center;
}

/* FEATURE CARDS */
.feature-card {
    background: rgba(255,255,255,0.95);
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.10);
    text-align: center;
    transition: 0.3s;
}

.feature-card:hover {
    transform: translateY(-5px);
}

/* INPUT BOX */
.stTextArea textarea {
    background-color: #f8fafc !important;
    border-radius: 14px !important;
    border: 1px solid #d0d7e6 !important;
    padding: 12px !important;
    font-size: 15px;
}

/* BUTTON */
.stButton button {
    background: rgba(255,255,255,0.92);

    color: #1e3a8a;

    padding: 14px 25px;

    border-radius: 14px;

    border: 1px solid rgba(255,255,255,0.6);

    font-size: 16px;

    font-weight: 600;

    width: 100%;

    box-shadow: 
        0 8px 20px rgba(0,0,0,0.12);

    transition: all 0.3s ease;
}


/* HOVER EFFECT */
.stButton button:hover {

    background: #ffffff;

    color: #2563eb;

    transform: translateY(-2px);

    box-shadow:
        0 12px 24px rgba(0,0,0,0.15);

}

/* TABS CONTAINER LOOK */

.stTabs {

background: rgba(
255,
255,
255,
0.95
);

padding: 18px;

border-radius: 20px;

border: 2px solid #dbeafe;

box-shadow:
0 8px 20px rgba(
0,
0,
0,
0.08
);

margin-bottom: 20px;

}

/* CAPTURED TEXT CARD */

.output-card {

background: white;

padding: 18px;

border-radius: 16px;

margin-top: 12px;

margin-bottom: 12px;

color: #111827;

font-size: 15px;

border: 1px solid #dbeafe;

box-shadow:
0 6px 18px rgba(
0,
0,
0,
0.08
);

word-wrap: break-word;

}
            

/* RESULT CARD */
.result-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

/* LABELS */
.small-label {
    color: #6b7280;
    font-size: 13px;
}

/* SIDEBAR BOX */
.sidebar-box {
    background: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
}

</style>

""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/student-male--v1.png", width=100)

    st.title("CareerLens AI")

    st.markdown("### Intelligent Career System")

    st.markdown("---")

    st.markdown("#### Features")
    st.markdown("✅ Text Input")
    st.markdown("✅ Voice Input (Azure Speech)")
    st.markdown("✅ Resume OCR (Azure Vision)")
    st.markdown("✅ AI Matching")

    st.markdown("---")

    st.selectbox("Recommendation Mode", ["Best Match", "Skills", "Education"])

    st.markdown("---")

    st.markdown(
        """
        <div class="sidebar-box">
        ⚡ Powered by Azure AI Services
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# HERO SECTION
# =========================
st.markdown("""
<div class="hero">

<h1>🎓 CareerLens AI</h1>

<p style="color:#4b5563;font-size:18px;">
Intelligent Multimodal Career Recommendation System using Azure AI Services
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# FEATURE CARDS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
    📝 <h4>Text Input</h4>
    <p class="small-label">Enter skills & interests</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    🎤 <h4>Voice Input</h4>
    <p class="small-label">Speak your goals</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
    📄 <h4>Resume OCR</h4>
    <p class="small-label">Upload documents</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================
# INPUT MODE SELECTION
# =====================================

st.markdown(
"## 🟡 Choose Input Method"
)

input_mode = st.radio(

"Select how you want to provide your information:",

[
"📝 Text Input",
"🎤 Voice Input",
"📄 Resume OCR"
],

horizontal=True

)

final_input = ""


# =====================================
# TEXT INPUT
# =====================================

if input_mode == "📝 Text Input":

    st.subheader(
    "Tell us about yourself"
    )

    user_input = st.text_area(

    "",

placeholder=
"""
Python

Machine Learning

Cloud

AI

Data Science
"""

    )

    final_input = user_input



# =====================================
# VOICE INPUT
# =====================================

elif input_mode == "🎤 Voice Input":

    if "voice_text" not in st.session_state:

        st.session_state.voice_text = ""


    st.subheader(
    "Speak your skills"
    )

    if st.button(
    "🎤 Start Voice Input"
    ):

        voice_text = get_voice_text()

        st.session_state.voice_text = voice_text

        st.success(
        "Voice captured"
        )


    if st.session_state.voice_text:

        st.markdown(
        f"""
        <div class="output-card">

        <b>Captured Voice Text</b>

        <br><br>

        {st.session_state.voice_text}

        </div>
        """,

        unsafe_allow_html=True
        )  


    final_input = st.session_state.voice_text



# =====================================
# IMAGE OCR INPUT
# =====================================

elif input_mode == "📄 Resume OCR":

    if "ocr_text" not in st.session_state:

        st.session_state.ocr_text = ""


    uploaded_file = st.file_uploader(

    "Upload Resume / Certificate",

    type=[
    "png",
    "jpg",
    "jpeg"
    ]

    )


    if uploaded_file is not None:

        col1, col2 = st.columns(
        2
        )

        with col1:

            st.image(
            uploaded_file,
            width=300
            )

        with col2:

            image_bytes = uploaded_file.read()

            extracted = extract_text(
            image_bytes
            )

            st.session_state.ocr_text = extracted

            st.markdown(
            f"""
            <div class="output-card">

            <b>Extracted Resume Text</b>

            <br><br>

            {extracted}

            </div>
            """,

            unsafe_allow_html=True
            )


    final_input = st.session_state.ocr_text



# =====================================
# GENERATE BUTTON
# =====================================

generate = st.button(
"🚀 Generate Recommendation",
use_container_width=True
)

if generate:

    if final_input.strip() == "":

        st.warning(
        "Please provide input first"
        )

    else:

        results = recommend_career(
        final_input
        )

        st.markdown(
        "### 🏆 Top Career Matches"
        )

        for r in results:

            st.markdown(
            f"""
            <div class="result-card">

            <h3>

            💼 {r['career']}

            </h3>

            <p>

            Match Score:
            <b>{r['score']}%</b>

            </p>

            <p>

            {r['reason']}

            </p>

            </div>

            """,

            unsafe_allow_html=True
            )