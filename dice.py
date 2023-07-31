import random

import streamlit as st
import numpy as np

st.title('点名器')

with st.sidebar:
    st.header('⚙️ 配置')
    names = st.text_area('名字列表', height=300, help='每行一个名字')
    names = names.split('\n')
    names = [name.strip() for name in names]
    names = [name for name in names if name]

st.divider()
st.caption('点击下面的按钮，随机选择一个人')
if st.button('随机选择'):
    if len(names) == 0:
        st.error('名字列表不能为空')
    else:
        selected = random.choice(names)
        st.success(f'🎉 恭喜 **{selected}** 被选中')

# TODO: 用 Session State 来保存 names 实现每按一次出现一个人名
# https://docs.streamlit.io/library/api-reference/session-state
st.divider()
st.caption('点击下面的按钮，随机排序')
if st.button('随机排序'):
    if len(names) == 0:
        st.error('名字列表不能为空')
    else:
        random.shuffle(names)
        for name in names:
            st.success(f'🎉 恭喜 **{name}** 被选中')

st.divider()
st.caption('🎲 摇骰子')
columns = st.columns(2)
with columns[0]:
    max_value = st.number_input('最大值', value=6, min_value=1, max_value=1000)
with columns[1]:
    num_dices = st.number_input('骰子个数', value=1, min_value=1, max_value=1000)
if st.button('Roll'):
    faces = np.random.randint(1, max_value + 1, size=num_dices)
    faces
