import pandas as pd
import streamlit as st

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
