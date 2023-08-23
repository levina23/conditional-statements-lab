def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

# Test cases
print(admin_login("admin", "12345"))  # Should print "Access granted"
print(admin_login("Admin", "12345"))  # Should print "Access granted"
print(admin_login("user", "password"))  # Should print "Access denied"

# new code
def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

# Test cases
print(hows_the_weather(30))   # Should print "It's brisk out there!"
print(hows_the_weather(50))   # Should print "It's a little chilly out there!"
print(hows_the_weather(90))   # Should print "It's too dang hot out there!"
print(hows_the_weather(70))   # Should print "It's perfect out there!"


# new code
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

# Test cases
print(fizzbuzz(3))    # Should print "Fizz"
print(fizzbuzz(5))    # Should print "Buzz"
print(fizzbuzz(15))   # Should print "FizzBuzz"
print(fizzbuzz(7))    # Should print 7

