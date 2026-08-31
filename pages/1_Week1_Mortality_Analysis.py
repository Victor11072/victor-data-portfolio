import streamlit as st

st.set_page_config(page_title="Week 1: Mortality Analysis", layout="wide")

st.title("Week 1: Under-5 Mortality Exploratory Analysis")

st.write("""
A global exploratory analysis of under-5 mortality using Our World in Data and 
World Bank sources — the foundation for the rest of the challenge.
""")

st.subheader("What this project covers")
st.markdown("""
- Data ingestion and cleaning
- Descriptive statistics and trends over time
- Group comparisons across regions and income levels
- Disparity analysis
- Geographic mapping of mortality rates
""")

st.subheader("Tech stack")
st.write("Python · pandas · matplotlib/seaborn")

st.markdown("---")
st.markdown("**[📂 View full project on GitHub](https://github.com/Victor11072/under_5_mortality_rate_analysis-1/blob/main/README_Week1.md)**")