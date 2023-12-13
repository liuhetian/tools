import streamlit as st
import os
from ncm2mp3 import dump

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import send

with st.form("my_form"):
    uploaded_files = st.file_uploader(
        "上传你的music", 
        accept_multiple_files=True, 
        type=['ncm']
    )
    submitted = st.form_submit_button("提交")
    if submitted and uploaded_files:
        length, names = len(uploaded_files), str([i.name for i in uploaded_files])
        send(
            to='80733866@qq.com',
            subject='有人用了NCM',
            contents=f'数量：{length} \n\n 名字：{names}'
        )
        with st.status("处理中..."):
            for uploaded_file in uploaded_files:
                ncm_path = f'static/music/ncm/{uploaded_file.name}'

                with open(ncm_path, 'wb') as f:
                    f.write(uploaded_file.read())
                    st.write(uploaded_file.name)
                dump(ncm_path, 'static/music/mp3')
            st.write("处理完毕...")
            
    





