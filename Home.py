import streamlit as st

st.set_page_config(page_title="Victor Olumide | Data Portfolio", layout="wide")

col_pic, col_name = st.columns([1, 4])

with col_pic:
    st.image("passport.jpg", width=120)

with col_name:
    st.title("Victor Olumide")
    st.subheader("Data Science → Data Engineering")

st.write("""
I'm a statistics graduate transitioning from data science and analytics into 
data engineering — building toward roles where I can design and ship real 
data products, not just models.

This portfolio walks through a 30-day self-directed challenge: four connected 
projects moving from global comparative analysis, to statistical modeling, 
to automated data engineering, to a live interactive dashboard — built to 
push myself beyond guided or copied tutorials into real, self-directed problem-solving.
""")

st.markdown("---")

st.header("The Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Week 1: Under-5 Mortality Exploratory Analysis")
    st.write("Global exploratory analysis of child mortality trends, disparities, and patterns across countries.")

    st.subheader("Week 3: Automated Data Pipeline")
    st.write("A production-style ETL pipeline — PostgreSQL, retry logic, validation, and scheduled automation.")

with col2:
    st.subheader("Week 2: What Drives Under-5 Mortality?")
    st.write("A regression model testing GDP, health expenditure, immunization, and sanitation as predictors across ~190 countries.")

    st.subheader("Week 4: Nigeria Humanitarian Dashboard (Live)")
    st.write("An interactive dashboard combining real displacement and food security data for Nigeria.")
    st.markdown("**[🔗 Try it live](YOUR_STREAMLIT_URL_HERE)**")

st.markdown("---")

st.header("Get in Touch")
st.write("Open to remote and contract data engineering opportunities.")
st.markdown("[LinkedIn](https://linkedin.com/in/victor-olumide-olusola) · [GitHub](https://github.com/Victor11072)")