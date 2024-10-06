import altair as alt
import pandas as pd
import seaborn as sns
import streamlit as st

st.title("Palmer's Penguins")
st.markdown("使用这个Streamlit应用程序制作您自己的关于企鹅的散布图！")

selected_x_var = st.selectbox(
    "您希望 X轴 变量是什么？",
    ["喙_长度_mm", "喙_深度_mm", "鳍肢_长度_mm", "身体_质量_g"],
)
selected_y_var = st.selectbox(
    "那么 Y轴 变量呢?",
    ["喙_深度_mm", "喙_长度_mm", "鳍肢_长度_mm", "身体_质量_g"],
)

penguin_file = st.file_uploader("选择您本地的企鹅.CSV")
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    st.stop()

alt_chart = (
    alt.Chart(penguins_df, title="帕尔默企鹅的散点图")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species",
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
