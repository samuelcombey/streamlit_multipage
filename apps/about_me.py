import streamlit as st
from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
    st.image("./assets/pic.png", width=230)
with col2:
    st.title("Samuel Combey", anchor=False)
    st.write("Senior AWS Cloud Engineer, aspiring AI Engineer with 4+ years of experience in the field.")
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 4+ years of experience in the field of cloud computing and AI
    - Strong hands-on experience with AWS services, python, and generative ai.
    - Strong knowledge of machine learning, deep learning, and computer vision.
    - Excellent team-player and displaying a strong sense of intiative problem-solving skills.
    """
)

# --- skills ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming Languages: Python, JavaScript, HTML, CSS
    - Frameworks: Django, Flask, Tensorflow, PyTorch
    - Tools: AWS, Docker, Git, Linux, Visual Studio Code, Jupyter Notebook
    - DevOps: CI/CD, AWS Cloudformation, GitHub Actions, Terraform
    """
)
