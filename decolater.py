def my_decolater(func):
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Funcname:", func.__name__)
        print("Arguments:", args)
        print("Keywords:", kwargs)
        ret = func(*args, **kwargs)
        print("Return:", ret)
        return ret
    return wrapper


@my_decolater
def func(msg1, msg2, flag=1, mode=2):
    """A sample function"""
    print("----", msg1, msg2, "----")
    return 1234


if __name__ == '__main__':
    n = func("Hello", "Hello2", flag=1)
    print(n)

    print(repr(func))
    print(func.__doc__)
