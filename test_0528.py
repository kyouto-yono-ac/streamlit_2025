import streamlit as st


st.write("**課題**: フォームを使って、サークル入会の申し込み情報をまとめて処理するアプリを作成する。")


with st.form("サークル入会フォーム"):
    
    name = st.text_input("名前", key="name")
    grade = st.selectbox("学年",options=["1年", "2年", "3年", "4年"])
    activity = st.selectbox("好きな活動", options=["スポーツ", "音楽", "アート", "ゲーム"])
    coment = st.text_area("意気込み", placeholder="自由にコメントをどうぞ")

    if st.form_submit_button("申し込む"):
        st.success("申し込みが完了しました！")
        st.write(f"名前: {name}")
        st.write(f"学年: {grade}")
        st.write(f"好きな活動: {activity}")
        st.write(f"意気込み: {coment}")
