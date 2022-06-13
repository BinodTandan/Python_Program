def increment(num):
    try:
        return int(num) + 1

    except:
        raise ValueError("You can't processed")

print(increment("xfghvdhg"))