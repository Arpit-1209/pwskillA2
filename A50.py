class Person:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value

    def get_name(self):
        return self.__name

# Example usage
person = Person("Alice", "alice@example.com")
print(person.email)  # Output: alice@example.com

person.email = "alice@newdomain.com"
print(person.email)  # Output: alice@newdomain.com

try:
    person.email = "invalidemail"  # Raises ValueError: Invalid email address
except ValueError as e:
    print(e)
