from typing import List, Dict, Optional
from .user import User


class Library:

    def __init__(self) -> None:
        self.user_records: List[User] = []
        self.books_available: Dict[str, List[str]] = {}  # {author: [book1, book2,...]}
        self.rented_books: Dict[str, Dict[str, int]] = {}
        # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str,
                 days_to_return: int, user: User) -> str:
        if book_name in self.books_available.get(author, []):
            # it will return the author or False
            if user not in self.user_records:
                self.user_records.append(user)
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            # self.rented_books.setdefault(user.username, {})[book_name]
            # = days_to_return
            self.rented_books[user.username] = {book_name: days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for record in self.rented_books.values():
            if book_name in record:
                days = record[book_name]
                return f'The book "{book_name}" is already rented and will be' \
                       f' available in {days} days!'

    def return_book(self, author: str, book_name: str, user: User) -> Optional[str]:
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        self.rented_books[user.username].pop(book_name)
