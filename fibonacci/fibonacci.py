def fibonacci_recursive(n):
    """
    フィボナッチ数列の n 番目の値を再帰で求める（非常に遅い）
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    try:
        count = int(input("何番目までのフィボナッチ数を表示しますか？: "))
        print("フィボナッチ数列:")
        for i in range(count):
            print(fibonacci_recursive(i), end=' ')
        print()
    except ValueError:
        print("整数を入力してください。")
