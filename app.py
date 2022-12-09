from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "peter_hrubos_cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic (16).png"
FB = current_dir / "assets" / "FB.svg.png"
LINKD = current_dir / "assets" / "Linkd.svg.png"
GITHUB = current_dir / "assets" / "github_icon.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Peter Hrubos"
PAGE_ICON =  "💼"
NAME = "Peter Hrubos"
DESCRIPTION1 = """
            ★ Assisting the business strategy by supporting data-driven decision-making.
                    """
DESCRIPTION2 ="""
            ★ Finding ways to use Python and SQL to be more efficient and effective in business settings
                """
EMAIL = "peter.hrubos.szte@gmail.com"
PHONE = "+36-20-821-11-77"
SOCIAL_MEDIA = {
                "Facebook" : "https://www.facebook.com/peter.hrubos.9/",
                "LinkedIn" : "https://linkedin.com/in/hrubospeter",
                "GitHub" : "https://github.com/phrubos"
                }
#PROJECTS  = {" 💡 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320"}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PICTURE ----
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- PROFIL PIC AND DESCRIPTIONS SECTION ----
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
## --- PICTURES UPLOAD ---
cols = st.columns((2.2,4,1.65,4.1,1.55,3.8))
index = 0
for x in [FB, LINKD, GITHUB]:
             index += 1
             pic = Image.open(x)
             cols[index].image(pic, width=25)
             index += 1
## --- LINKS ---
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
- ✔️ 4+ Years experience extracting actionable insights from data
- ✔️ Experience and knowledge in Python/SQL and Excel (Power Pivot/Query)
- ✔️ Willingness to learn, strong commitment to continuous development
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
""")

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write("""
- 👩‍💻 Programming: Python (NumPy, Pandas), SQL, Power Query/Pivot
- 📊 Data Visualization: Tableau, MS Excel, Plotly, Matplotlib, Seaborn
- 🗄️ Databases: Hadoop, MySQL
""")


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**CE Productivity Process Manager | Tesco**")
st.write("07/2018 - Present")
st.write(
    """
- ► Designing and building Data Models by using ETL process (Extract, Transform, Load) and handling Central Europe wide data in order to calculate and predict workload for each activity of a targeted area.
- ► Building models with usage of 'Maynard Operation Sequence Technique' (MOST) and 'Random Activity Sampling' (RAS).
- ► The adaptable models are able to calculate different scenarios with the change of 1 or more aspects of the work environment. 
- ► Gathering, transforming, cleaning data using SQL and Python. Continuously investigating data integrity and developing queries.
"""
)

# --- JOB 2
st.write("#")
st.write("🚧", "**Junior CE Productivity Process Manager | Tesco**")
st.write("03/2018 - 07/2018")
st.write(
    """
- ► Responsible for measuring, assessing, redesigning processes in order to create a better consumer experience and improving business results (store measurements, process mapping).
- ► Supporting budget calculations for every department in Central Europe (excel-based productivity models).
"""
)

# --- JOB 3
st.write("#")
st.write("🚧", "**HU Productivity Manager | Tesco**")
st.write("10/2017 - 03/2018")
st.write(
    """
- ► Planning, working out and calculating the budget of HU stores for the next financial year (excel-based productivity models' outputs).
- ► Analyzing, documenting and reporting irregular results during budget planning (debugging in processes).
- ► Collaborating with leadership team to oversee new processes, and updates which have been built in the new budget.
"""
)

# --- JOB 4
st.write("#")
st.write("🚧", "**HU Productivity Analyst | Tesco**")
st.write("08/2015 - 10/2017")
st.write(
    """
- ► Daily requests calculations which help in making a decision related with process improvement on HU stores (excel-based calculations).
- ► Updating „Bottom up” model which allows structure planning (excel-based productivity models).
- ► Collaborating with process managers to oversee end-to-end processes from stores' labor demand point of view. 
"""
)

# --- JOB 5
st.write("#")
st.write("🚧", "**IT Coordinator | Tesco**")
st.write("08/2009 - 08/2015")
st.write(
    """
- ► Maintaining the day to day operations of this logistic center from hardware and software point of view
- ► Reporting software's failure and hardware being unable to work with (issue tracking softwares).
"""
)


# # --- Projects & Accomplishments ---
# st.write("#")
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")

