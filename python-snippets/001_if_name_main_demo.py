def hello():
    print("Hello from function!")

print("この行は常に実行されます（importしても表示される）")

# **「このファイルが直接実行されたときだけ、「if __name__ == "__main__":」ここから下のコードが実行される」**という意味。
if __name__ == "__main__":
    print("この行は直接実行されたときだけ表示されます")
    hello()