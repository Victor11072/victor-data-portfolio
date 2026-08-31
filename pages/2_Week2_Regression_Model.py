import streamlit as st

st.set_page_config(page_title="Week 2: Regression Model", layout="wide")

st.title("Week 2: What Drives Under-5 Mortality?")

st.write("""
A statistical model testing GDP per capita, health expenditure, immunization 
rates, and sanitation access as predictors of under-5 mortality across ~190 
countries (2022 cross-section).
""")

st.subheader("What this project covers")
st.markdown("""
- OLS regression with standardized predictors
- Ridge and Lasso regularization
- Multicollinearity checks (VIF)
- Outlier detection with Cook's Distance
- 80/20 train-test validation
""")

st.subheader("Headline finding")
st.write("""
Several countries — including Uganda, Tanzania, Ghana, and Pacific Island 
nations like Papua New Guinea — perform meaningfully better on child mortality 
than their GDP alone would predict. Nigeria and Niger are among the largest 
under-performers, alongside a distinct "resource curse" pattern in Equatorial 
Guinea and Turkmenistan, where high GDP doesn't translate to better outcomes.
""")

st.subheader("Tech stack")
st.write("Python · pandas · scikit-learn · statsmodels")

st.markdown("---")
st.markdown("**[📂 View full project on GitHub](https://github.com/Victor11072/under_5_mortality_rate_analysis-1/blob/main/README_Week2.md)**")