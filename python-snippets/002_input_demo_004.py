# num = int(input("数字を入力してください: "))
# 「abc」など数字じゃない文字を入力すると…
# ValueError: invalid literal for int() with base 10: 'abc'

try:
    num = int(input("数字を入力してください: "))
except ValueError:
    print("それは整数じゃないよ！")