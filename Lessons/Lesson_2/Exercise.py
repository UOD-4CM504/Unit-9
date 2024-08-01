class Book:
    def __init__(self, title, author, price, no_pages=None, year=None):
        self.title = title
        self.author = author
        self.price = price
        self.no_pages = no_pages
        self.year = year

    def description(self):
        desc_string = ""
        desc_string += f"Title: {self.title}"
        desc_string += f"\nAuthor: {self.author}"
        desc_string += f"\nPrice: £{self.price}"

        if self.year:
            desc_string += f"\nYear Published: {self.year}"
        if self.no_pages:
            desc_string += f"\nNo. of Pages: {self.no_pages}"

        return desc_string


if __name__ == "__main__":
    book_one = Book("1984", "George Orwell", 6.99)
    print(book_one.description())
    print()
    book_one = Book("1984", "George Orwell", 6.99, no_pages=328)
    print(book_one.description())
    print()
    book_one = Book("1984", "George Orwell", 6.99, year=1949)
    print(book_one.description())
    print()
    book_one = Book("1984", "George Orwell", 6.99, no_pages=328, year=1949)
    print(book_one.description())