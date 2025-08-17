from models.formulas import FORMULAS
from views.layout import build_window, update_result, alert

def _selected_exercise(values) -> str | None:
    if values.get("-SQ-"): return "SQ"
    if values.get("-DL-"): return "DL"
    if values.get("-BP-"): return "BP"
    return None


def run():
    window = build_window()
    while True:
        event, values = window.read()
        if event in (None, "終了"):
            break

        if event == "計算":
            ex = _selected_exercise(values)
            if ex is None:
                alert("種目を選択してください")
                continue

            try:
                w = float(values.get("-LIFTING_WEIGHT-", ""))
                r = int(values.get("-REPS-", ""))
            except ValueError:
                alert("重量は数値、レップは整数で入力してください")
                continue

            result = FORMULAS[ex](w, r)  # Modelに“丸投げ”
            update_result(window, result) # Viewに表示だけ頼む

    window.close()