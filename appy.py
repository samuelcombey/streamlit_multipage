import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    page="apps/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True
)
project_1_page = st.Page(
    page="apps/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_2_page = st.Page(
    page="apps/app2.py",
    title="Image Generator",
    icon=":material/face:",
)
project_3_page = st.Page(
    page="apps/app3.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_4_page = st.Page(
    page="apps/app4.py",
    title="Image Generator",
    icon=":material/face:",
)
project_5_page = st.Page(
    page="apps/app5.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_6_page = st.Page(
    page="apps/app6.py",
    title="Image Generator",
    icon=":material/face:",
)
project_7_page = st.Page(
    page="apps/app7.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_8_page = st.Page(
    page="apps/app8.py",
    title="Image Generator",
    icon=":material/face:",
)
project_9_page = st.Page(
    page="apps/app9.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_10_page = st.Page(
    page="apps/app10.py",
    title="Image Generator",
    icon=":material/face:",
)
project_11_page = st.Page(
    page="apps/app11.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_12_page = st.Page(
    page="apps/app12.py",
    title="Image Generator",
    icon=":material/face:",
)
project_13_page = st.Page(
    page="apps/app13.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_14_page = st.Page(
    page="apps/app14.py",
    title="Image Generator",
    icon=":material/face:",
)
project_15_page = st.Page(
    page="apps/app15.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITH SECTIONS] ---
apps = st.navigation(
    {
    "Info": [about_page],
    "Apps": [project_1_page, project_2_page, project_3_page, project_4_page, project_5_page, project_6_page, project_7_page, 
             project_8_page, project_9_page, project_10_page, project_11_page, project_12_page, project_13_page, project_14_page, 
             project_15_page]
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/logo.png")
st.sidebar.text("Made with ❤️ by Sam")


# --- RUN NAVIGATION ---
apps.run()