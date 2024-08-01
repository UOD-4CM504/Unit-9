import pytest
from Exercise import Book

@pytest.mark.parametrize("book_params, expected_output", [
    (
        {"title": "1984", "author": "George Orwell", "price": 6.99},
        "Title: 1984\nAuthor: George Orwell\nPrice: £6.99"
    ),
    (
        {"title": "1984", "author": "George Orwell", "price": 6.99, "no_pages": 328},
        "Title: 1984\nAuthor: George Orwell\nPrice: £6.99\nNo. of Pages: 328"
    ),
    (
        {"title": "1984", "author": "George Orwell", "price": 6.99, "year": 1949},
        "Title: 1984\nAuthor: George Orwell\nPrice: £6.99\nYear Published: 1949"
    ),
    (
        {"title": "1984", "author": "George Orwell", "price": 6.99, "no_pages": 328, "year": 1949},
        "Title: 1984\nAuthor: George Orwell\nPrice: £6.99\nYear Published: 1949\nNo. of Pages: 328"
    )
])
def test_book_description(book_params, expected_output):
    book = Book(**book_params)
    assert book.description() == expected_output, (
        f"\n\nFailed with parameters:\n"
        f"title={book.title}\n"
        f"author={book.author}\n"
        f"price={book.price}\n"
        f"no_pages={book.no_pages}\n"
        f"year={book.year}\n"
    )

def test_book_title_change():
    book = Book("1984", "George Orwell", 6.99)
    book.title = "Changed the title"
    assert book.title == "Changed the title"