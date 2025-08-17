import TkEasyGUI as sg
import tkinter.ttk as ttk  # ttk.Progressbar 用
import platform

# ---- 共通スタイル ----
"""
  - フォント指定を統一するためのラッパー関数。
  - T → Text, I → Input, ML → Multiline, B → Button。
"""

APP_NAME = "TkEasyGUI All-in-One Demo"
IS_MAC = platform.system() == "Darwin"
ACC_SAVE = "⌘S" if IS_MAC else "Ctrl+S"
ACC_OPEN = "⌘O" if IS_MAC else "Ctrl+O"
ACC_NEW  = "⌘N" if IS_MAC else "Ctrl+N"
ACC_FIND = "⌘F" if IS_MAC else "Ctrl+F"
ACC_CLEAR = "⌘L" if IS_MAC else "Ctrl+L"
DEFAULT_FONT = ("Meiryo", 11)

def T(text, **kw):
    return sg.Text(text, font=DEFAULT_FONT, **kw)

def I(**kw):
    return sg.Input(font=DEFAULT_FONT, **kw)

def ML(**kw):
    return sg.Multiline(font=DEFAULT_FONT, **kw)

def B(text, **kw):
    return sg.Button(text, font=DEFAULT_FONT, **kw)

# ---- Window 生成 ----
def build_window():
    # --- メニュー定義（タブ区切りでショートカットも設定可） ---
    menu_def = [
        ["ファイル", [ f"新規\t{ACC_NEW}",
                f"開く...\t{ACC_OPEN}",
                f"上書き保存\t{ACC_SAVE}",
                "名前を付けて保存", "---",
                "終了" ]],
        ["編集",   [ f"入力をクリア\t{ACC_CLEAR}" ]],
        ["表示",   [ "折り返しの切替" ]],
        ["ヘルプ", [ "使い方", "バージョン情報" ]]
    ]

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

    layout = [
        [sg.Menu(menu_def, key="-MENU-")],
        [sg.Frame("RM換算",
                [[sg.Column(col_inputs)]],
                expand_x=True, font=DEFAULT_FONT)],
    ]
    return sg.Window(APP_NAME, layout, resizable=True)

# 以下は“表示の責務”として用意（Controllerから呼ぶ）
def update_result(window, value: float):
    window["-RESULT-"].update(f"1RM: {value}")

def alert(message: str):
    sg.popup(message)