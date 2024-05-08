s_username="emc"
s_password="123"
username=input("Enter username:")
password=input("Enter password:")
def validate():
    if(s_username==username) and (s_password==password):
        return True
    else:
        return False
status=validate()
print(status)