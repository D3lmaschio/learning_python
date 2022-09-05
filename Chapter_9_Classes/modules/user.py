class User:
    """
    Represents the user profile from a website.
    """

    def __init__(self, first_name='', last_name=''):
        """
        Assign the atributes first_name and last_name with given
        arguments.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Adds the 1 to login_attempts."""
        self.login_attempts += 1

    def reset_login_attemps(self):
        """Reset the count of login_attempts."""
        self.login_attempts = 0

    def describe_user(self):
        """Display a description of instance"""
        print(f"Full name: {self.first_name.title()}"
              f" {self.last_name.title()}")

    def greet_user(self):
        """Display greetings =)"""
        print(f"Welcome, {self.last_name.title()}")


user_00 = User("Matheus", "Delmaschio")
user_01 = User("Yasmin", "Delmaschio")
user_02 = User("Sara", "Delmaschio")

user_00.describe_user()
user_00.greet_user()

user_01.describe_user()
user_01.greet_user()

user_02.describe_user()
user_02.greet_user()

print(user_00.login_attempts)
user_00.increment_login_attempts()
user_00.increment_login_attempts()
user_00.increment_login_attempts()
user_00.increment_login_attempts()
print(user_00.login_attempts)
user_00.reset_login_attemps()
print(user_00.login_attempts)
