# Test case for login validation

def test_login(username, password):
    if username == "student" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid username or password"


# Test execution
print(test_login("student", "1234"))
print(test_login("student", "wrong"))
print(test_login("", "" ))