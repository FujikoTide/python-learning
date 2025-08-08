from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Library:
    books: List[str]
    borrowed_by: Dict[str, str]

    def add_book(self, title: str) -> None:
        self.books.append(title)

    def borrow_book(self, title: str, borrower: str) -> bool:
        if title in self.books:
            self.books.remove(title)
            self.borrowed_by[title] = borrower
            return True
        return False

    def return_book(self, title: str) -> bool:
        if title in self.borrowed_by:
            self.borrowed_by.pop(title)
            self.books.append(title)
            return True
        return False
