# Create a class called Profile. Upon initialization, it should receive:

# •	username: str - the username should be between 5 and 15 characters (inclusive). If it 
# is not, raise a ValueError with the message "The username must be between 5 and 15 
# characters."

# •	password: str - the password must be at least 8 characters long; it must contain at 
# least one upper case letter and at least one digit. If it does not, raise a ValueError
# with the message "The password must be 8 or more characters with at least 1 digit and 1 
# uppercase letter."

# Hint: Use Getters and Setters to name-mangle them.
# Override the __str__() method of the base class, so it returns: "You have a profile
# with username: "{username}" and password: {"*" with the length of password}".

class Profile:
    
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15  characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_long_enough = len(value) >= 8
        upper_case = len([char for char in value if char.isupper()]) > 0
        is_digit = len([char for char in value if char.isdigit()]) > 0

        if not is_long_enough or not upper_case or not is_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 "
                             "digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f"You have a profile with username: '{self.username}' and" \
               f" password: {'*' * len(self.password)}"


# Test code 1
# profile_with_invalid_password = Profile('My_username', 'My-password')

# Test code 2
# profile_with_invalid_username = Profile('Too_long_username', 'Any')

# Test code 3
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
