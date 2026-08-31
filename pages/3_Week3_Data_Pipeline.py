import streamlit as st

st.set_page_config(page_title="Week 3: Data Pipeline", layout="wide")

st.title("Week 3: Automated Data Pipeline")

st.write("""
A production-style ETL pipeline built on the same World Bank and WHO data 
sources from Weeks 1-2 — shifting from one-off analysis to automated, 
repeatable data engineering.
""")

st.subheader("What this project covers")
st.markdown("""
- REST API extraction with pagination and error handling
- Modular, reusable transform functions
- PostgreSQL loading with idempotency (safe to re-run without duplicating data)
- Automated data validation and quality checks
- Logging and scheduled execution (Windows Task Scheduler)
""")

st.subheader("Tech stack")
st.write("Python · PostgreSQL · Docker · REST APIs")

st.markdown("---")
st.markdown("**[📂 View full project on GitHub](https://github.com/Victor11072/under_5_mortality_rate_analysis-1/blob/main/README_Week3_Pipeline.md)**")