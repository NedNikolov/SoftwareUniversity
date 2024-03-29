class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        username_len = len(value)
        if 5 > username_len or username_len > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return ''.join('*' * len(self.__password))

    @password.setter
    def password(self, value):
        if 8 > len(value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        if len([x for x in value if x.isupper()]) < 1:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        if len([x for x in value if x.isdigit()]) < 1:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {self.password}"
