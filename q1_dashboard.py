# Overall Equipment Effectiveness (OEE) dashboard

import streamlit as st
import pandas as pd
import plotly.express as px

# st.set_page_config(page_title="OEE Dashboard", layout="wide")

st.title("OEE Dashboard")

### 데이터 입력 (sidebar)
st.sidebar.header("Input Parameters")
machines = ['M1', 'M2']
data = []

for machine in machines:
    availability = st.sidebar.slider(f"{machine} - Availability", 0.0, 1.0, 0.9, 0.01)
    performance = st.sidebar.slider(f"{machine} - Performance", 0.0, 1.0, 0.95, 0.01)
    quality = st.sidebar.slider(f"{machine} - Quality", 0.0, 1.0, 0.98, 0.01)
    oee = availability * performance * quality
    data.append({
        "Machine": machine,
        "Availability": availability,
        "Performance": performance,
        "Quality": quality,
        "OEE": oee
    })


### 데이터프레임

df = pd.DataFrame(data)

### 시각화

st.subheader("OEE Data Table")
st.dataframe(df.style.format({
    "Availability": "{:.0%}",
    "Performance": "{:.0%}",
    "Quality": "{:.0%}",
    "OEE": "{:.0%}"
}))

st.subheader("OEE by Machine")
fig = px.bar(df, x='Machine', y='OEE', text='OEE', color='OEE',
             color_continuous_scale='Blues', range_y=[0, 1])
fig.update_traces(texttemplate='%{text:.0%}', textposition='outside')
fig.update_layout(yaxis_title="OEE", xaxis_title="Machine", showlegend=False)

st.plotly_chart(fig, use_container_width=True)



