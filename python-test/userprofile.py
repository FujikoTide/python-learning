class UserProfile:
  def __init__(self, username: str, email: str, is_active: bool = False):
    self.username = username
    self.email = email
    self.is_active = is_active

  def activate(self):
    self.is_active = True

  def deactivate(self):
    self.is_active = False

admin = UserProfile("harold", "admin@haroldtech.com", True)
user = UserProfile("barry", "barry@haroldtech.com", True)
guest = UserProfile("george", "george@somewhereelse.com", False)