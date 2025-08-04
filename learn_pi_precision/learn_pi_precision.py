from decimal import Decimal, getcontext
# Decimal：高精度な小数を扱う特別な型
# getcontext()：どこまでの桁数を使うか設定できる

def compute_pi(n_digits):
    """
    円周率をn_digits桁まで計算（Chudnovskyアルゴリズムを使用）
    """

    # n_digits：何桁まで計算したいか

    # getcontext().prec = n_digits + 2
    #　→ 少し多めに桁を確保しておくことで誤差を防ぎます。

    getcontext().prec = n_digits + 2  # 丸め誤差を防ぐために余分に精度を取る


    # Chudnovsky algorithm constants
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, n_digits):
        M = (M * (K**3 - 16*K)) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    return str(pi)[:n_digits + 2]  # "3."を含むので+2

if __name__ == "__main__":
    try:
        n = int(input("表示したい桁数を入力してください（最大1000桁程度を推奨）: "))
        if n > 1000:
            print("桁数が多すぎます。1000桁以下を推奨します。")
        else:
            pi_value = compute_pi(n)
            print(f"\nπ（円周率）の先頭 {n} 桁:\n{pi_value}")
    except ValueError:
        print("整数を入力してください。")

# input()：キーボードから桁数を入力
# int(...)：数字として扱うために文字列→整数に変換
# compute_pi(n)：先ほど作った関数でπを計算
# print(...)：結果を表示
