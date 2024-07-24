import streamlit as st
import pandas as pd
import matplotlib
import numpy as np
import time

# matplotlib显示中文
matplotlib.rc("font",family='AR PL UMing CN')

# 1. st.write()
st.write("1. st.write()")
st.write(pd.DataFrame({
    '第一列':[1,2,3,4],
    '第二列':[10,20,30,40]}
))

# 2. st.line_chart()
st.write("2. st.line_chart()")
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(chart_data)

# 定义自定义CSS
def set_background_color():
    st.markdown(
        """
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-of-type(1) {
            background: url("https://pic.imgdb.cn/item/66a0a82cd9c307b7e9103de6.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """,

        unsafe_allow_html=True
    )
# 设置折线图背景颜色
set_background_color()




# 3. st.map()
st.write("3. st.map()")
map_data = pd.DataFrame(
    np.random.randn(1000,2)/[50,50] + [37.76,-122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# 4. st.slider()
st.write("4. st.slider()")
x = st.slider("x")
st.write(x, "x*x=", x*x)

# 5. st.text_input()
st.write("5. st.text_input()")
st.text_input("your name", key="name")
st.session_state.name

# 6. st.show dataframe()
st.write("6. st.show dataframe()")
if st.checkbox("show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"]
    )
    chart_data

# 7. st.selectbox()
st.write("7 st.selectbox()")
df = pd.DataFrame({
    '第一列':[1,2,3,4]
})
option = st.selectbox(
    'which number do you like best?',
    df['第一列']
)
"you selecet: ",option

# 8. st.sidebar()
st.write("8. st.sidebar()")
add_selectbox = st.sidebar.selectbox(
    "通讯方式选项",
    ('微信', 'QQ', '手机', '邮件')
)
add_slider = st.sidebar.slider(
    "选择一个范围内的值",
    0.0, 100.0, (25.0, 75.0)
)
"通讯方式选择：", add_selectbox
"范围内的值选择： ", add_slider

# 9. st.radio()
st.write("9. st.radio()")
left_column, right_column = st.columns(2)
left_column.button("Press me!")
with right_column:
    choose = st.radio(
        '手机品牌',
        ('Iphone', 'HUAWEI', 'XiaoMi', 'Sumsung')
    )
    st.write(f'Brand is: {choose}')
# choose = right_column.radio(
#     '手机品牌',
#     ('Iphone', 'HUAWEI', 'XiaoMi', 'Sumsung')
# )
# right_column.write(f'Brand is: {choose}')

# 11. st.file_uploader()
st.write("11. st.file_uploader()")
upload_file = st.file_uploader(
    label= '上传CSV文件'
)
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.success("上传文件成功！")
else:
    st.stop()

# 10. st.progress()
st.write("10. st.progress()")
st.write("Clock up......")
latest_iteration = st.empty()# 添加PlaceHolder
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
st.write("times up")