#!/usr/bin/python3
""" 
User class
"""


class User:
    """
    A class that represents a user.

    Attributes:
        __email (str): The email address of the user.

    Example Usage:
        user = User()  # Create a new user object
        user.email = "example@example.com"  # Set the email address of the user
        print(user.email)  # Get and print the email address of the user
    """

    def __init__(self):
        """
        Initializes a new instance of the User class.

        Args:
            None

        Returns:
            None
        """
        self.__email = None

    @property
    def email(self):
        """
        Getter method for retrieving the email address of the user.

        Args:
            None

        Returns:
            str: The email address of the user.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Setter method for setting the email address of the user.

        Args:
            value (str): The email address to be set.

        Returns:
            None

        Raises:
            TypeError: If the input value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
