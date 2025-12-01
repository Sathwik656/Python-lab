try:
    raise KeyError
    raise TypeError
    raise ValueError

except KeyError:
    print("Key error")
except TypeError:
    print("Type error")
except ValueError:
    print("Value error")
