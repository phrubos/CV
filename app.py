from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic (16).png"
FB = current_dir / "assets" / "FB.svg.png"
LINKD = current_dir / "assets" / "Linkd.svg.png"
GITHUB = current_dir / "assets" / "github.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Peter Hrubos"
PAGE_ICON = "random" #":wave:"
NAME = "Peter Hrubos"
DESCRIPTION1 = """
            ★ Assisting enterprises by supporting data-driven decision-making.
                    """
DESCRIPTION2 ="""
            ★ Finding ways to use Python and SQL to be more efficient and effective in business settings
                """
EMAIL = "peter.hrubos.szte@gmail.com"
PHONE = "+36-20-821-11-77"
SOCIAL_MEDIA = {
                "Facebook" : "https://www.facebook.com/peter.hrubos.9/",
                "LinkedIn" : "https://linkedin.com/in/hrubos-péter-36a32ba8",
                "GitHub" : "https://github.com/phrubos"
                }
PROJECTS  = {" 💡 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320"}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PICTURE ----
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ----
col1, col2 = st.columns((1,1) , gap="small")
with col1:
    st.image(profile_pic, width=230)
    st.markdown('')


with col2:
    st.title(NAME)
    st.write("CE Productivity Process Manager")
    st.write("---")
    st.write(DESCRIPTION1)
    st.write(DESCRIPTION2)


# --- AVAILABILITIES ---
st.write("#")
col_a, col_b, col_c = st.columns((1.2,0.8,1))
       
with col_a:
                st.write("📧 ", EMAIL)                     
with col_b:
                st.write(":phone: ", PHONE)

                       
with col_c:
                st.download_button(
                label="📋 Download Resume",
                data=PDFbyte,
                file_name=resume_file.name,
                mime = "application/octet-stream",) 
st.write("---")
# --- SOCIAL LINKS ---

st.write("#")
cols = st.columns((1.5,4,1.5,4,1.5,4))
cols[0].image(x, width=25)
index = 0
for x in [FB, LINKD, GITHUB]:
            index += 1
            cols[index].image(x, width=25)
            index += 1

cols = st.columns((1.5,4,1.5,4,1.5,4))
index = 0
for (platform, link) in SOCIAL_MEDIA.items():
            index += 1
            cols[index].write(f"[{platform}]({link})")
            index += 1
            
st.write("---")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write("""
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
""")

# --- SKILS ---
st.write("#")
st.subheader("Hard Skills")
st.write("""
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
""")


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write("#")
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write("#")
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)

# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

