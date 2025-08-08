from dataclasses import dataclass
from typing import Optional


@dataclass
class Contact:
    name: str
    email: Optional[str] = None
    phone: str | int | None = None


contact1 = Contact("Harold")
contact2 = Contact("George", "g@bigtech.com")
contact3 = Contact("Oswald", "o@bigtech.com", 29323442)
contact4 = Contact("Harold", phone=4423423442)
