import streamlit as st

st.set_page_config(page_title="Week 4: Nigeria Dashboard", layout="wide")

st.title("Week 4: Nigeria Humanitarian Dashboard")

st.write("""
An interactive dashboard combining IOM's Displacement Tracking Matrix and 
Cadre Harmonisé food security data for Nigeria, built for a non-technical 
NGO audience to explore without touching code.
""")

st.subheader("What this project covers")
st.markdown("""
- Interactive choropleth map with a combined severity index
- Displacement trends built from real reporting dates
- State-level detail panel showing assessment depth, not just summary numbers
- A national context panel linking back to Week 2's findings — shown 
  side by side, deliberately not merged into the state-level data
""")

st.subheader("Tech stack")
st.write("Python · Streamlit · Folium · Plotly · GeoPandas")

st.markdown("---")
st.markdown("**🔗 [Try the live dashboard](https://nigeria-humanitarian-dashboard.streamlit.app/)**")
st.markdown("**[📂 View full project on GitHub](https://github.com/Victor11072/under_5_mortality_rate_analysis-1/blob/main/README_Week4_Dasboard.md)**")