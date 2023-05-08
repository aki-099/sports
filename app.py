import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import os

@st.cache_data
def error_time(path):
    for f in os.listdir(path):
        e = pd.read_pickle(f'{path}/{f}')
        time0 = list(e.index)[0]
        time1 = list(e.index)[-1]
        li.add_vrect(x0=time0 , x1=time1 , line_width=0, fillcolor="gray", opacity=0.2)
    return li.show()
st.set_page_config(layout="wide")

# Data
df = pd.read_pickle('program/pkl/Qton/220101-230201/hoterubeamonte/ALL/hoterubeamonte_Qton1main_ALL.pickle')
df = df.set_index("datetime")
columns = list(df.columns)
columns.remove("Error_Code")
columns = [c for c in columns if "sub" not in c]
default_columns = [c for c in columns if "CM" in c]
df = df["2022-05-01":"2022-12-01"]
df= df[columns]

# Layout (Sidebar)
st.sidebar.markdown("## Settings")
cont_multi_selected = st.sidebar.multiselect('Correlation Matrix', columns,default=default_columns)

# Continuous Variable Distribution in Content
li = px.line(data_frame = df[cont_multi_selected],x = df.index,y=cont_multi_selected)

path = "Series/Qton/220101-230201/hoterubeamonte/ALL/Qton1main"
error_time(path)


# Correlation Matrix in Content
df_corr = df[cont_multi_selected].corr()
fig_corr = go.Figure([go.Heatmap(z=df_corr.values,
                                 x=df_corr.index.values,
                                 y=df_corr.columns.values)])
fig_corr.update_layout(height=300,
                       width=400,
                       margin={'l': 20, 'r': 20, 't': 0, 'b': 0})

# # Layout (Content)
st.plotly_chart(li)
st.plotly_chart(fig_corr)