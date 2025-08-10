import TkEasyGUI as sg
import tkinter.ttk as ttk  # ttk.Progressbar 用

# ---- 共通スタイル ----
"""
  - フォント指定を統一するためのラッパー関数。
  - T → Text, I → Input, ML → Multiline, B → Button。
"""

DEFAULT_FONT = ("Meiryo", 11)

def T(text, **kw):
    return sg.Text(text, font=DEFAULT_FONT, **kw)

def I(**kw):
    return sg.Input(font=DEFAULT_FONT, **kw)

def ML(**kw):
    return sg.Multiline(font=DEFAULT_FONT, **kw)

def B(text, **kw):
    return sg.Button(text, font=DEFAULT_FONT, **kw)

# ---- レイアウト ----
col_inputs = [
    [T("重量"), I(key="-LIFTING_WEIGHT-", size=(24, 1))],
    [T("レップ数"), I(key="-REPS-", size=(24, 1))],
    [T("種目"),
        sg.Radio("SQ", "EXERCISE", key="-SQ-", font=DEFAULT_FONT),
        sg.Radio("DL", "EXERCISE", key="-DL-", font=DEFAULT_FONT),
        sg.Radio("BP", "EXERCISE", key="-BP-", font=DEFAULT_FONT)],
    [sg.Button("計算"), sg.Button("終了")],
    [sg.Text("結果：", key="-RESULT-", size=(30, 1))]
]

col_outputs=[
    [T("結果"), I(key="-INPUT-", size=(24, 1))]
]

layout = [
    [sg.Frame("RM換算",
              [[sg.Column(col_inputs)]],
              expand_x=True, font=DEFAULT_FONT)],
]

# --- BP(RM換算)関数 ---
def calc_BP(lifting_weight,reps):
    rm=lifting_weight*reps/40+lifting_weight
    return round(rm,0)

# --- SQ(RM換算)関数 ---
def calc_SQ(lifting_weight,reps):
    rm=lifting_weight*reps/33.3+lifting_weight
    return round(rm,0)

# --- DL(RM換算)関数 ---
def calc_DL(lifting_weight,reps):
    rm=lifting_weight*reps/33.3+lifting_weight
    return round(rm,0)

# ---- Window 生成 ----
window = sg.Window("TkEasyGUI All-in-One Demo", layout, resizable=True)

# ---- イベントループ ----
while True:
    event, values = window.read()
    lifting_weight = float(values["-LIFTING_WEIGHT-"])
    reps = int(values["-REPS-"])
    if event in (None, "終了"):
        break
    if event == "計算":
        if values["-SQ-"]:
            window["-RESULT-"].update(f"1RM: {calc_SQ(lifting_weight,reps)}")
        elif values["-DL-"]:
            window["-RESULT-"].update(f"1RM: {calc_DL(lifting_weight,reps)}")
        elif values["-BP-"]:
            window["-RESULT-"].update(f"1RM: {calc_BP(lifting_weight,reps)}")
        else:
            sg.popup("種目を選択してください")

window.close()