"""CS330 Spring 2019: Quiz 2 (take home)."""

import unittest
import shelf
import book

# Steps to consider when writing any unit test:
# 1) Create an instance of the object whose behavior you want to test.
# 2) Ensure that the instance is initialized appropriately to exhibit the behavior need to meet the test objective.
# 3) Use the TestCase methods (self.assertXXXXX()) to show the test objective is met.
# 4) Verify object state before and after (where needed) to show that test actions affect the object's state.
# 5) Run your test class the same way you'd run any Python program.

# PyUnit Docs: https://docs.python.org/3/library/unittest.html


class TestShelf(unittest.TestCase):
    """Tests Shelf behavior."""

    # Write unit tests for these Shelf class methods and behaviors:

    def test_AddBook(self):
        """Tests that a book is successfully added to a shelf, increasing the count of books by 1."""
        test_shelf = shelf.Shelf()
        little_women = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        test_shelf.AddBook(little_women)
        self.assertTrue(test_shelf.GetBookCount(), 1)

    def test_RemoveBook(self):
        """Tests that a book is successfully removed from a shelf, decreasing the book count from 2 to 1."""
        test_shelf = shelf.Shelf()
        little_women = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        warriors = book.Book("Warriors", ("Erin", "", "Hunter"))
        test_shelf.AddBook(warriors)
        test_shelf.AddBook(little_women)
        test_shelf.RemoveBook("Little Women")
        self.assertTrue(test_shelf.GetBookCount(), 1)

    def test_AddBook_reduces_shelf_capacity(self):
        """Tests that shelf capacity is reduced after adding a book,
        so the available capacity should be less than the initial capacity after adding a book."""
        test_shelf = shelf.Shelf()
        initial = test_shelf.GetInitialCapacity()
        warriors = book.Book("Warriors", ("Erin", "", "Hunter"))
        warriors.SetPages(20)
        warriors.SetCoverType(book.CoverType.HARDCOVER)
        test_shelf.AddBook(warriors)
        self.assertLess(test_shelf.GetAvailableCapacity(), initial)

    def test_RemoveBook_increases_shelf_capacity(self):
        """Tests that shelf capacity is increased after removing a book,
        so the available capacity should be greater after removing a book should from a shelf containing 1 book,
        which should also be equal to the initial capacity since there are no longer books on the shelf."""
        test_shelf = shelf.Shelf()
        initial = test_shelf.GetInitialCapacity()
        warriors = book.Book("Warriors", ("Erin", "", "Hunter"))
        warriors.SetPages(20)
        warriors.SetCoverType(book.CoverType.HARDCOVER)
        test_shelf.AddBook(warriors)
        pass1 = test_shelf.GetAvailableCapacity()
        test_shelf.RemoveBook("Warriors")
        self.assertGreater(test_shelf.GetAvailableCapacity(), pass1)
        self.assertEqual(test_shelf.GetAvailableCapacity(), initial)

    # Extra Credit
    def test_shelf_space_exhausted(self):
        """Tests that an exception is raised and the book count does not change when
        adding a book to a shelf with insufficient space."""
        test_shelf = shelf.Shelf()
        little_women = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        warriors = book.Book("Warriors", ("Erin", "", "Hunter"))
        warriors.SetPages(70)
        warriors.SetCoverType(book.CoverType.HARDCOVER)
        little_women.SetPages(20)
        little_women.SetCoverType(book.CoverType.HARDCOVER)
        test_shelf.AddBook(warriors)
        test_shelf.AddBook(little_women)
        self.assertRaises(RuntimeError)
        self.assertTrue(test_shelf.GetBookCount(), 1)

if __name__ == '__main__':
    unittest.main()