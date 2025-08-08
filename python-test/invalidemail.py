from dataclasses import dataclass


class InvalidEmailError(ValueError):
    pass


@dataclass
class UserRegistration:
    def register_user(self, username, email):
        if not ("@" in email and "." in email):
            raise InvalidEmailError(f"Incorrect email !!!, {email}")


user_reg = UserRegistration()
user_reg.register_user("Harold", "harold@bigtech.com")
user_reg.register_user("George", "bademail.shoe")
