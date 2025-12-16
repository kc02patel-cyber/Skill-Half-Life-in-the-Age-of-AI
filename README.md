Skill Half-Life in the Age of AI

Power BI–Grade Workforce Analytics Dashboard (Streamlit)

Overview

The rapid advancement of Artificial Intelligence (AI) is accelerating the rate at which professional skills become obsolete. This project presents a Power BI–grade analytical dashboard built using Python and Streamlit to analyze skill half-life—the time it takes for a skill’s relevance to decline by 50%—in the age of AI.

The dashboard enables stakeholders to understand:

Which skills are decaying fastest

How AI exposure impacts skill relevance

Which industries and skill categories face the highest automation risk

How reskilling strategies can extend skill longevity

Dashboard Objectives

Quantify skill half-life across categories and industries

Analyze AI exposure and automation risk

Identify high-demand yet high-risk skills

Support data-driven workforce planning and reskilling strategies

Key KPIs

Average Skill Half-Life (Years)

Percentage of High AI-Exposure Skills (>70%)

Average Reskilling Interval (Years)

High Automation-Risk Skill Count (>70%)

These KPIs provide an executive-level snapshot before deeper analysis.

Visual Analytics Included
Insight Area	Visualization Type
Skill decay by category	Horizontal Bar Chart
AI exposure vs skill relevance	Scatter Plot
Automation risk distribution	Histogram
Market demand vs automation risk	Bubble Chart
Reskilling frequency variability	Box Plot
Industry exposure to skill decay	Stacked Bar Chart
Learning strategy effectiveness	Grouped Bar Chart

Each visualization serves a distinct analytical purpose with no redundancy.

Dataset

Type: Synthetic (Realistic workforce simulation)

Format: CSV

Rows: 20 skills across multiple industries

Key Features:

AI exposure level

Skill half-life

Automation risk

Market demand

Reskilling frequency

Learning mode

Industry classification

Dataset file:
skill_half_life_ai.csv

Tech Stack

Python

Streamlit (Dashboard Framework)

Pandas (Data Processing)

Plotly (Interactive Visualizations)

Project Structure
skill-half-life-ai-dashboard/
│
├── app.py                     # Single-file Streamlit application
├── skill_half_life_ai.csv      # Synthetic workforce dataset
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
