from typing import Optional


class User:
    def __init__(self, username: str, password: str, email: Optional[str] = None):
        self.username = username
        self.password = password
        self.email = email
        self._is_active = True

    def __repr__(self):
        return f"User(username={self.username}, password={self.password}, email={self.email}, is_active={self._is_active})"

    def deactivate_account(self):
        self._is_active = False


user1 = User("Harold", "cat", "harold@haroldtech.com")
user2 = User("George", "dog")

print(user1)
print(user2)

user2.deactivate_account()
print(user1)
print(user2)
