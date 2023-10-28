### Libraries import
import streamlit as st
from st_functions import st_button, load_css
st.set_page_config(page_title="📝 Main Page")

### Side bar
st.sidebar.write("Welcome all interested parties to my streamlit app. It is prepared as a portfolio of skills that I have :bulb:")
st.sidebar.write("The main page shows the work experience, education and skills I have. At the very bottom of the page you will also find channels to contact me such as linkedin and github :envelope_with_arrow:")
st.sidebar.write("In the subpages you will find projects that I have done or are in the process of doing. I would like to point out that if the page is empty, it means that work on the project is still in progress. At the bottom of the page you will also find the date when the project was released 	:bell:")
st.sidebar.write("I encourage you to try each of the projects because they are interactive with the application user :sunglasses:")

### Title
st.title("Streamlit app by Igor Winek :sunglasses:")


### First layout declaration
col_my_description, col_my_photo = st.columns(2)

### My decription
col_my_description.header("Hello everyone!")
col_my_description.write("""I am a second-year master's degree student at the Polish-Japanese Academy of Information Technology, specializing in Data Science. I have been interested in the field of Data Science and Machine Learning for over 3 years, and I started my programming journey 5 years ago. During this time, I have prepared many smaller models using Linear and Logistic Regression, KNN, K-means, and Naive Bayes. Currently, I work as a Data Science Assistant, bpreparing models for media campaigns in the Polish and foreign markets (mainly CEE and SEE). Currently, I am most interested in neuro-linguistic programming and computer vision. I am also a member of the data sciene club at my university, and I co-lead the cosmos project which aims to create a model that recognizes exoplanets in space. """)

### My photo
col_my_photo.header(" ")
col_my_photo.header(" ")
col_my_photo.image("images/my_photo.jpg", use_column_width=True)
st.markdown("""---""")

### Skills section
st.write("""<h1 style="text-align:center;">Skills</h1>""", unsafe_allow_html=True)

### Second layout declaration
col_programming_skills, col_other_skills, col_language_skills  = st.columns(3)

### Languages skills layout
col_language_skills.markdown('<span style="font-size:24px;">Language skills</span>', unsafe_allow_html=True)
col_language_skills.write(""":bulb: Polish Native""")
col_language_skills.write(""":bulb: English B2""")

### Programming skills layout
col_programming_skills.markdown('<span style="font-size:24px;">Programming skills</span>', unsafe_allow_html=True)
col_programming_skills.write(""":bulb: Python (Pandas, Numpy, PyTorch, Scikit-learn, Tensorflow, Keras, Matplotlib, Plotly, Seaborn, Beautiful Soup, Selenium, Streamlit)""")
col_programming_skills.write(""":bulb: R (dplyr, ggplot2, tidyr, moments, TTR, e1071, car, plyr)""")
col_programming_skills.write(""":bulb: HTML (entry level)""")
col_programming_skills.write(""":bulb: C++ (entry level)""")
col_programming_skills.write(""":bulb: JAVA (entry level)""")
col_programming_skills.write(""":bulb: CSS (entry level)""")
col_programming_skills.write(""":bulb: SQL (entry level)""")

### Other skills layout
col_other_skills.markdown('<span style="font-size:24px;">Other skills</span>', unsafe_allow_html=True)
col_other_skills.write(""":bulb: Excel (advanced level)""")
col_other_skills.write(""":bulb: GIT (entry level)""")
col_other_skills.write(""":bulb: LINUX (entry level)""")
col_other_skills.write(""":bulb: Tableau (entry level)""")
col_other_skills.write(""":bulb: PowerBI (entry level)""")
col_other_skills.write(""":bulb: AWS (entry level)""")
col_other_skills.write(""":bulb: GCP (entry level)""")

### Experience section
st.markdown("""---""")
st.write("""<h1 style="text-align:center;">Experience</h1>""", unsafe_allow_html=True)

### Wavemaker
st.subheader("""Data Science Assistant | Wavemaker Warsaw | 03.2022 - Currently""")
st.write(""":large_blue_circle: Data processing""")
st.write(""":large_blue_circle: Creating descriptive models of media campaigns""")
st.write(""":large_blue_circle: Data scraping""")
st.write(""":large_blue_circle: Creating simple ETL solutions""")
st.write(""":large_blue_circle: Data visualization and presentation""")
st.write(""":large_blue_circle: Using APIs in Python for data extraction""")
st.write(""":large_blue_circle: Updating the dashboard with results from models""")

### Digesta
st.subheader("""Junior Accountan | Digesta Otwock | 10.2020 - 02.2022""")
st.write(""":large_blue_circle: Accounting for flat-rate business activities""")
st.write(""":large_blue_circle: Accounting for VAT-registered business activities""")
st.write(""":large_blue_circle: Invoicing settlement for limited liability companies (LLCs)""")
st.write(""":large_blue_circle: Continuous contact with the tax office, office clients and Social Insurance Institution (ZUS)""")

### Bunkier Store
st.subheader("""Sales assistant | BunkierStore Sobienie-Jeziory | 06.2019 - 09.2020""")
st.write(""":large_blue_circle: Customer service""")
st.write(""":large_blue_circle: Handling complaints""")
st.write(""":large_blue_circle: Ordering goods""")
st.write(""":large_blue_circle: Processing individual customer orders""")
st.write(""":large_blue_circle: Creating and accepting inter-warehouse transfers""")

### Education section
st.markdown("""---""")
st.write("""<h1 style="text-align:center;">Education</h1>""", unsafe_allow_html=True)

### PJATK
st.subheader("""Polish-Japanese Academy of Information Technology 10.2022 - Currently""")
st.write(""":mortar_board: Faculty of Computer Science""")
st.write(""":mortar_board: Specialization Data Science""")
st.write(""":mortar_board: Master's degree""")

### UW
st.subheader("""University of Warsaw10.2019 - 07.2022""")
st.write(""":mortar_board: Faculty of Economics""")
st.write(""":mortar_board: Specialization Computer Science and Econometrics""")
st.write(""":mortar_board: Bachelor's degree""")

### Courses and certifications section
st.markdown("""---""")
st.write("""<h1 style="text-align:center;">Courses and certifications</h1>""", unsafe_allow_html=True)
st.write(""":page_with_curl: AWS Academy Cloud Foundations | AWS academy | Amazon | 03.2023""")
st.write(""":page_with_curl: From Data to Insights with Google Cloud | Coursera | Google | 06.2022""")
st.write(""":page_with_curl: The Fundamentals of Digital Marketing | Google | 06.2022""")
st.write(""":page_with_curl: Digital Economy | Faculty of Economic Sciences | University of Warsaw | 06.2022""")


### Achievements section
st.markdown("""---""")
st.write("""<h1 style="text-align:center;">Achievements</h1>""", unsafe_allow_html=True)
st.write(""":medal: 2nd place in the supervision_hack hackaton organized by UKNF | topic: #fakejobhunter | 05.2023""")

### More about me section
st.markdown("""---""")
st.write("""<h1 style="text-align:center;">More about me</h1>""", unsafe_allow_html=True)
st.header(" ")

### Links sections
#st_button('linkedin', 'https://pl.linkedin.com/in/igor-winek-ba43261a4', 'Visit my linkedin', 25)
#st.write(" ")
#st_button('github', 'https://github.com/IgorWinek', 'Visit my github', 25)
#st.write(" ")

### Last update
st.header(" ", divider='rainbow')
st.write("""Released: 17.10.2023""")
st.write("Created by: Igor Winek")