# This chapter has a lot of section of code that do not build on each other, so therefore I have combined much of the code into this single python file!
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure
import pydeck as pdk

st.title("SF 树")
st.write(
    "该应用程序使用 SF DPW 提供的数据集分析旧金山的树木"
)
trees_df = pd.read_csv("trees.csv")
st.write(trees_df.head())

###Built in Graphing Functions
st.title("SF 树")
st.write(
    "该应用程序使用 SF DPW 提供的数据集分析旧金山的树木"
)
trees_df = pd.read_csv("trees.csv")
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
df_dbh_grouped.columns = ["tree_count"]
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

###Built in Graphing pt 2
st.title("SF 树")
st.write(
	"这个应用程序使用SF DPW友情提供的数据集分析旧金山的树木"
)
trees_df = pd.read_csv("trees.csv")
st.write(trees_df.head())
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
df_dbh_grouped.columns = ["tree_count"]
df_dbh_grouped["new_col"] = np.random.randn(len(df_dbh_grouped)) * 500
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

### Built in Map
st.title("SF 树")
st.write(
	"这个应用程序使用SF DPW友情提供的数据集分析旧金山的树木"
)
trees_df = pd.read_csv("trees.csv")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1000)
st.map(trees_df)

# Plotly
st.title("SF 树")
st.write(
	"这个应用程序使用SF DPW友情提供的数据集分析旧金山的树木"
)
st.subheader("Plotly Chart")
trees_df = pd.read_csv("trees.csv")

fig = px.histogram(trees_df["dbh"])
st.plotly_chart(fig)

# Matplotlib and Seaborn
st.title("SF 树")
st.write(
	"这个应用程序使用SF DPW友情提供的数据集分析旧金山的树木"
)
trees_df = pd.read_csv("trees.csv")
trees_df["age"] = (pd.to_datetime("today") - pd.to_datetime(trees_df["date"])).dt.days

st.subheader("Seaborn Chart")
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df["age"])
plt.xlabel("Age (Days)")
st.pyplot(fig_sb)

st.subheader("Matploblib Chart")
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df["age"])
plt.xlabel("Age (Days)")
st.pyplot(fig_mpl)

# Bokeh
st.title("SF 树")
st.write(
	"这个应用程序使用SF DPW友情提供的数据集分析旧金山的树木"
)
st.subheader("Bokeh Chart")
trees_df = pd.read_csv("trees.csv")

scatterplot = figure(title="Bokeh Scatterplot")
scatterplot.scatter(trees_df["dbh"], trees_df["site_order"])
scatterplot.yaxis.axis_label = "site_order"
scatterplot.xaxis.axis_label = "dbh"
st.bokeh_chart(scatterplot)

# Altair
st.title("SF 树: Altair")
st.write(
	"这个应用程序使用SF DPW友情提供的数据集分析旧金山的树木"
)
trees_df = pd.read_csv("trees.csv")
df_caretaker = trees_df.groupby(["caretaker"]).count()["tree_id"].reset_index()
df_caretaker.columns = ["caretaker", "tree_count"]
fig = alt.Chart(df_caretaker).mark_bar().encode(x="caretaker", y="tree_count")
st.altair_chart(fig)

# Altair pt 2
st.title("SF 树: Altair")
st.write(
	"这个应用程序使用SF DPW友情提供的数据集分析旧金山的树木"
)
trees_df = pd.read_csv("trees.csv")
fig = alt.Chart(trees_df).mark_bar().encode(x="caretaker", y="count(*):Q")
st.altair_chart(fig)

# PyDeck
st.title("SF 树: PyDeck")
st.write(
	"这个应用程序使用SF DPW友情提供的数据集分析旧金山的树木"
)
trees_df = pd.read_csv("trees.csv")
trees_df.dropna(how="any", inplace=True)

sf_initial_view = pdk.ViewState(latitude=37.77, longitude=-122.4, zoom=11, pitch=30)

hx_layer = pdk.Layer(
    "HexagonLayer",
    data=trees_df,
    get_position=["longitude", "latitude"],
    radius=100,
    extruded=True,
)

st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=sf_initial_view,
        layers=[hx_layer],
    )
)