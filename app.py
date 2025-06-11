import streamlit as st
from PIL import Image

# タイトルを設定
st.title("ローカル画像表示アプリ")

# ローカル画像のパスを指定
image_path = "image.png" # 表示したい画像のパスを指定してください

# 画像を読み込む
image = Image.open(image_path)
# 画像を表示
st.image(image, caption="かわいい猫の画像", use_column_width=True)
