try:
    a=int(input())
    b=int(input())
    c=input()
    print(d)
except ValueError as e:
    print("Value Error",e)
except TypeError as e:
    print("Type Error",e)
except Exception:
    print("Something Fishy")