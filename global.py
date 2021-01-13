def func() -> None:
    """グローバル変数の確認用"""
    global num
    num = 20
    print(num)


if __name__ == '__main__':
    num = 10
    print(num)
    func()
    print(num)
