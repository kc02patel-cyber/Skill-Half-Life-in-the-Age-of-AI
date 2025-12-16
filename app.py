import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Skill Half-Life in the Age of AI",
    layout="wide"
)

st.title("Skill Half-Life in the Age of AI")
st.caption("Power BI–grade workforce analytics dashboard built with Streamlit")

# ----------------------------
# Load Data
# ----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("skill_half_life_ai.csv")

df = load_data()

# ----------------------------
# Global Filters
# ----------------------------
st.sidebar.header("Global Filters")

category_filter = st.sidebar.multiselect(
    "Skill Category",
    options=df["skill_category"].unique(),
    default=df["skill_category"].unique()
)

industry_filter = st.sidebar.multiselect(
    "Industry",
    options=df["industry"].unique(),
    default=df["industry"].unique()
)

ai_exposure_range = st.sidebar.slider(
    "AI Exposure Level",
    int(df.ai_exposure_level.min()),
    int(df.ai_exposure_level.max()),
    (0, 100)
)

filtered_df = df[
    (df["skill_category"].isin(category_filter)) &
    (df["industry"].isin(industry_filter)) &
    (df["ai_exposure_level"].between(ai_exposure_range[0], ai_exposure_range[1]))
]

# ----------------------------
# KPI Row
# ----------------------------
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "Avg Skill Half-Life (Years)",
    round(filtered_df.skill_half_life_years.mean(), 1)
)

high_ai_pct = (filtered_df.ai_exposure_level > 70).mean() * 100
kpi2.metric(
    "High AI-Exposure Skills (%)",
    f"{round(high_ai_pct,1)}%"
)

kpi3.metric(
    "Avg Reskilling Interval (Years)",
    round(filtered_df.reskilling_frequency_years.mean(), 1)
)

high_risk_count = (filtered_df.automation_risk > 70).sum()
kpi4.metric(
    "High Automation-Risk Skills",
    high_risk_count
)

st.divider()

# ----------------------------
# Analysis Layer
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        filtered_df.groupby("skill_category", as_index=False)
        .skill_half_life_years.mean(),
        x="skill_half_life_years",
        y="skill_category",
        orientation="h",
        title="Average Skill Half-Life by Category"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(
        filtered_df,
        x="ai_exposure_level",
        y="skill_half_life_years",
        color="skill_category",
        size="current_market_demand",
        title="AI Exposure vs Skill Half-Life"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# Risk Insights
# ----------------------------
col3, col4 = st.columns(2)

with col3:
    fig3 = px.histogram(
        filtered_df,
        x="automation_risk",
        nbins=10,
        title="Automation Risk Distribution"
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    fig4 = px.scatter(
        filtered_df,
        x="automation_risk",
        y="current_market_demand",
        size="skill_half_life_years",
        color="skill_category",
        title="Market Demand vs Automation Risk"
    )
    st.plotly_chart(fig4, use_container_width=True)

# ----------------------------
# Deep Insights
# ----------------------------
col5, col6 = st.columns(2)

with col5:
    fig5 = px.box(
        filtered_df,
        x="skill_category",
        y="reskilling_frequency_years",
        title="Reskilling Frequency by Skill Category"
    )
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    exposure_band = pd.cut(
        filtered_df.ai_exposure_level,
        bins=[0,40,70,100],
        labels=["Low","Medium","High"]
    )

    industry_exposure = (
        filtered_df.assign(exposure=exposure_band)
        .groupby(["industry","exposure"])
        .size()
        .reset_index(name="count")
    )

    fig6 = px.bar(
        industry_exposure,
        x="industry",
        y="count",
        color="exposure",
        title="Industry Exposure to Skill Decay"
    )
    st.plotly_chart(fig6, use_container_width=True)

# ----------------------------
# Learning Strategy
# ----------------------------
fig7 = px.bar(
    filtered_df.groupby("learning_mode", as_index=False)
    .skill_half_life_years.mean(),
    x="learning_mode",
    y="skill_half_life_years",
    title="Learning Mode Impact on Skill Longevity"
)

st.plotly_chart(fig7, use_container_width=True)
