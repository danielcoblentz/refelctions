class book:
    def __init__(self, title, pages) -> None:
        self.title = title
        self.pages = pages

my_book = book('hero', 100)
print(my_book.title, my_book.pages)

# this just creates a blue print for an object with multiple features by default or specified by the user.

#creating a private class can be done by prefixing the class name with a double underscore "__" while this still does not totally prevent accessablity it does give indication that this is not intended for public access.