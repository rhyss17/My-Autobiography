from pathlib import Path
import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Autobiography and Portfolio", layout="wide")

base_path = Path(__file__).parent  # Gets the directory where the script is located

home_logo = Image.open(base_path / "home.png")
portfolio_logo = Image.open(base_path / "portfolio.png")
resume_logo = Image.open(base_path / "resume.png")
contact_logo = Image.open(base_path / "contacts.png")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

def set_page(page_name):
    st.session_state.page = page_name

st.sidebar.title("Navigation")

def sidebar_button_with_logo(logo, label, page_name):
    col1, col2 = st.sidebar.columns([1, 5])  
    with col1:
        st.image(logo, use_column_width=True) 
    with col2:
        if st.button(label):
            set_page(page_name)

sidebar_button_with_logo(home_logo, "Home", "Home")
sidebar_button_with_logo(portfolio_logo, "Portfolio", "Portfolio")
sidebar_button_with_logo(resume_logo, "Resume", "Resume")
sidebar_button_with_logo(contact_logo, "Contact", "Contact")

page = st.session_state.page

def display_image(image_path, caption):
    image = Image.open(image_path)
    st.image(image, caption=caption, use_column_width=True)

if page == "Home":
    st.title("Welcome to My Autobiography!!!")
    st.header("About Me")
    st.write("""
    Hello, Good day! I am Rhyss Gianne Mendoza Almeda and I am currently an IT student with a passion for technology, 
    problem-solving and continuous learning. My journey into the world of Information Technology has been one of exploration, challenges and growth, shaping me into who I am today.
    """)

    display_image(base_path / "rhyss.jpg", "This is me!")

    st.subheader("Early Life")
    st.write("I was born and raised in Laspiñas City, where I developed an early interest in computers and technology. From a young age, I was fascinated by how things worked, often taking apart gadgets and trying to understand their inner workings. This curiosity naturally led me to pursue IT as my field of study..")
    st.subheader("Academic Journey")
    st.write("My formal journey in IT began when I enrolled in Cebu Institute of Technology University(CITU), where I am currently pursuing a degree in Information Technology. Throughout my studies, I've delved into various areas such as programming, network security, software development and database management. My coursework has provided me with a solid foundation, while hands-on projects had given me practical experience.")
    st.subheader("Hobbies & Interests")
    st.write("My Hobbies are watching anime, playing online games like dota2, mobile legends, and open world games.")

elif page == "Portfolio":
    st.title("My Portfolio")
    st.write("Here is our capstone projects I have worked on.")
    st.subheader("[Frontend](https://github.com/reeyyyxd/CIMP_FrontEnd.git)")
    st.write("- It uses React and MUI")
    st.subheader("[Backend](https://github.com/reeyyyxd/CIMP_BackEnd.git)")
    st.write("- It uses Springboot")

elif page == "Resume":
    st.title("Resume")
    st.write("Download my resume by clicking the button below.")
    
    with open(base_path / "Almeda_Resume.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Almeda_Resume.pdf",
            mime="application/pdf"
        )
    
    st.subheader("Education")
    st.write("Bachelor of Information Technology from Cebu Institute of Technology University.")

elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out through the form below.")
    
    contact_form = st.form(key="contact_form")
    with contact_form:
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label="Send")

    if submit_button:
        st.write(f"Thank you {name}, your message has been sent!")
