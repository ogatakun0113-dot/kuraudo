<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>伝送値換算 (3200-FA00)</title>
    <style>
        :root { --blue: #1E90FF; --bg: #f0f8ff; --text: #31333F; }
        body { font-family: sans-serif; color: var(--text); background: #fff; margin: 0; padding: 15px; }
        .credit { text-align: right; font-size: 14px; color: #666; margin-bottom: 5px; }
        h1 { font-size: 20px; margin: 10px 0; color: var(--text); border-bottom: 2px solid var(--blue); padding-bottom: 5px; }
        
        .input-section { margin-bottom: 20px; }
        label { display: block; font-size: 24px; font-weight: 800; color: var(--blue); margin-bottom: 10px; }
        input { width: 100%; height: 65px; padding: 10px; border: 3px solid var(--blue); border-radius: 12px; box-sizing: border-box; font-size: 32px; font-weight: bold; text-transform: uppercase; outline: none; }
        
        .result-box { background: var(--bg); padding: 20px; border-radius: 15px; border: 1px solid var(--blue); }
        .res-item { margin-bottom: 15px; }
        .res-label { font-size: 14px; color: #666; display: block; }
        .res-value { font-size: 28px; font-weight: bold; color: #000; }
        
        .error { color: #dc3545; font-weight: bold; font-size: 14px; margin-top: 5px; display: none; }
        .range-info { font-size: 12px; color: #777; margin-top: 15px; padding: 10px; background: #eee; border-radius: 5px; }
    </style>
</head>
<body>

<div class="credit">開発/制作：緒方</div>
<h1>🔢 伝送値換算 (3200-FA00 HEX)</h1>

<div class="input-section">
    <label>16進数(HEX)を入力</label>
    <input type="text" id="hex_in" value="3200" maxlength="4" oninput="calc()">
    <div id="error_msg" class="error">範囲外です (3200 - FA00)</div>
</div>

<div class="result-box">
    <div class="res-item">
        <span class="res-label">10進数 (DEC)</span>
        <span id="res_dec" class="res-value">12800</span>
    </div>
    <div class="res-item">
        <span class="res-label">換算率 (%)</span>
        <span id="res_per" class="res-value">0.00 %</span>
    </div>
</div>

<div class="range-info">
    入力範囲目安:<br>
    ・3200 (12800) = 0%<br>
    ・FA00 (64000) = 100%
</div>

<script>
    function calc() {
        const hexIn = document.getElementById('hex_in').value.toUpperCase();
        const errorMsg = document.getElementById('error_msg');
        
        // 入力チェック
        if (!/^[0-9A-F]{1,4}$/.test(hexIn)) {
            return;
        }

        const decVal = parseInt(hexIn, 16);
        const minVal = 0x3200; // 12800
        const maxVal = 0xFA00; // 64000

        if (decVal < minVal || decVal > maxVal) {
            errorMsg.style.display = 'block';
        } else {
            errorMsg.style.display = 'none';
        }

        // パーセント計算: (現在値 - 下限) / (上限 - 下限) * 100
        const percent = ((decVal - minVal) / (maxVal - minVal)) * 100;

        document.getElementById('res_dec').innerText = decVal.toLocaleString();
        document.getElementById('res_per').innerText = percent.toFixed(2) + " %";
    }

    // 初期計算
    window.onload = calc;
</script>

</body>
</html>
