import streamlit as st

# --- ページ設定 ---
st.set_page_config(page_title="伝送値換算 (3200-FA00)", layout="centered")

# --- 見た目の設定（CSS） ---
# 全角スペースを完全に排除したクリーンな記述です
st.markdown("""
<style>
.credit { text-align: right; font-size: 14px; color: #666; margin-bottom: -20px; }
.stTextInput label { font-size: 24px !important; color: #1E90FF !important; font-weight: 800 !important; }
div[data-baseweb="input"] { height: 65px !important; font-size: 32px !important; border: 3px solid #1E90FF !important; border-radius: 12px; }
.result-box { background-color: #f0f8ff; padding: 20px; border-radius: 15px; border: 1px solid #1E90FF; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title('🔢 伝送値換算 (3200-FA00 HEX)')
st.markdown("---")

# --- 入力セクション ---
hex_in = st.text_input("16進数(HEX)を入力", value="3200").upper()

# --- 計算ロジック ---
try:
    # 16進数から10進数へ変換
    dec_val = int(hex_in, 16)
    
    min_val = 0x3200 # 12800
    max_val = 0xFA00 # 64000

    # 範囲チェック
    if dec_val < min_val or dec_val > max_val:
        st.warning(f"範囲外です: 3200(12800) ～ FA00(64000)")
    
    # パーセント計算
    percent = ((dec_val - min_val) / (max_val - min_val)) * 100

    # --- 表示セクション ---
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.subheader("📊 換算結果")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("10進数 (DEC)", f"{dec_val:,}")
    with c2:
        st.metric("換算率 (%)", f"{percent:.2f} %")
    
    st.markdown('</div>', unsafe_allow_html=True)

except ValueError:
    st.error("有効な16進数を入力してください")

st.markdown("---")
st.info("入力範囲目安:\n\n・3200 (12800) = 0%\n\n・FA00 (64000) = 100%")
