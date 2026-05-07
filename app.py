import streamlit as st

st.set_page_config(page_title="伝送換算 (3200-FA00)クラウドＴＭ用", layout="centered")

st.markdown("""
<style>
.stNumberInput label { font-size: 18px !important; font-weight: 800 !important; color: #1E90FF !important; }
.result-box { background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #1E90FF; margin-top: 20px; }
.credit { text-align: right; font-size: 14px; color: #666; margin-bottom: -20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title('📱 伝送換算 (3200h-FA00h)(HEX)')

with st.expander("⚙️ 基本情報設定", expanded=True):
    col1, col2 = st.columns(2)
    s_min = col1.number_input("スケール下限 (0%)", value=0.00)
    s_max = col2.number_input("スケール上限 (100%)", value=100.00)
    
    resistance = st.selectbox("入力抵抗を選択 (Ω)", [250, 500, 50], index=0)
    v_min_ref = (4.0 / 1000.0) * resistance
    v_max_ref = (20.0 / 1000.0) * resistance
    st.caption(f"💡 4-20mA時の目安: {v_min_ref:.3f}V - {v_max_ref:.3f}V")

    t_min = float(int("3200", 16))
    t_max = float(int("FA00", 16))

mode = st.radio("項目を選択して入力", ["伝送値(HEX)", "指示値", "割合(%)", "電流(mA)", "電圧(V)"], horizontal=True)

percent = 0.0
try:
    if mode == "伝送値(HEX)":
        h_in = st.text_input("HEX入力", value="3200").upper()
        percent = (float(int(h_in, 16)) - t_min) / (t_max - t_min)
    elif mode == "指示値":
        val = st.number_input("値", value=s_min)
        percent = (val - s_min) / (s_max - s_min) if (s_max-s_min)!=0 else 0
    elif mode == "割合(%)":
        percent = st.number_input("%", value=0.0) / 100.0
    elif mode == "電流(mA)":
        val = st.number_input("mA", value=4.00, format="%.2f")
        percent = (val - 4.0) / 16.0
    elif mode == "電圧(V)":
        # 電圧入力を小数点3桁に変更
        val = st.number_input("V入力", value=v_min_ref, format="%.3f")
        percent = (val - v_min_ref) / (v_max_ref - v_min_ref) if (v_max_ref-v_min_ref)!=0 else 0
except:
    st.error("入力エラー")

res_scale = s_min + (s_max - s_min) * percent
res_ma = 4.0 + 16.0 * percent
res_v = v_min_ref + (v_max_ref - v_min_ref) * percent
res_hex = hex(int(round(t_min + (t_max - t_min) * percent))).replace('0x','').upper()

st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.subheader("📊 換算結果")
c1, c2, c3 = st.columns(3)
c1.metric("指示値", f"{res_scale:.2f}")
c2.metric("電流", f"{res_ma:.2f} mA")
c3.metric("電圧", f"{res_v:.3f} V") # 結果も3桁
st.metric("伝送値 (HEX)", f"{res_hex} h")
st.markdown('</div>', unsafe_allow_html=True)
