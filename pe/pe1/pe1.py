# 定義基準音符和頻率值
ref_octave = 4
ref_pc = 9
ref_hz = 440

# 讀取八度和音高值
octave = int(input("請輸入八度值："))
pc = int(input("請輸入音高值："))

# 計算差值
o_diff = octave - ref_octave
m_diff = pc - ref_pc

# 計算頻率值
freq = ref_hz * pow(2, o_diff + (m_diff/12))

# 輸出結果
print("對應的頻率值為：", freq, "Hz")