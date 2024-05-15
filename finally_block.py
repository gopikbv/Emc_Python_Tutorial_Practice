try:
    a=int(input())
    b=int(input())
except ValueError as e:
    print("Value Error",e)
except Exception:
    print("Something Fishy")
finally:
    print("Done")
    