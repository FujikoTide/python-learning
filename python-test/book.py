class Book:
  def __init__(self, title: str, author: str, publication_year: int):
    self.title = title
    self.author = author
    self.publication_year = publication_year

  def __repr__(self):
    return (f"Book(title={self.title}, author={self.author}, publication_year={self.publication_year})")

  def get_age(self, current_year: int) -> int:
    return current_year - self.publication_year


helicopter_book = Book("helicopters", "Harold Finch", 1998)
animal_book = Book("Animals of the World", "George Somebody", 2001)

print(helicopter_book)
print(animal_book)
print(helicopter_book.get_age(2025))
print(animal_book.get_age(2025))

