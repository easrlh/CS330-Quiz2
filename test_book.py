"""Created by Bob Zwolinski on 2019-03-19."""

import unittest
import book


class TestBook(unittest.TestCase):
    """Tests Book object behavior."""

    def testMakeBookInstance(self):
        """Tests that the Book constructor returns an instance of the Book class."""
        self.assertIsInstance(book.Book("Little Women", ("Louisa", "May", "Alcott")), book.Book)

    def test_equals_operator(self):
        """Tests the == operator for the Book class."""
        book1 = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        book2 = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        self.assertEqual(book1, book2)

        book3 = book.Book("War and Peace", ("Leo", "", "Tolstoy"))
        self.assertNotEqual(book1, book3)

    def test_GetAuthorAsString(self):
        """Tests that the author is returned as a properly formatted string."""
        little_women = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        self.assertEqual("Louisa May Alcott", little_women.GetAuthorAsString())

        war_and_peace = book.Book("War and Peace", ("Leo", "", "Tolstoy"))
        self.assertEqual("Leo Tolstoy", war_and_peace.GetAuthorAsString())

        hobbit = book.Book("The Hobbit", ("J", "R R", "Tolkien"))
        self.assertEqual("J R R Tolkien", hobbit.GetAuthorAsString())

    def test_GetAuthor(self):
        """Tests that the author is a tuple."""
        little_women = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        self.assertIsInstance(little_women.GetAuthor(), tuple)
        self.assertEqual(3, len(little_women.GetAuthor()))

        little_women = book.Book("Little Women", ())
        self.assertIsInstance(little_women.GetAuthor(), tuple)
        self.assertEqual(0, len(little_women.GetAuthor()))

    def testGetThickness(self):
        """Tests that book thickness is calculated correctly."""
        little_women = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        little_women.SetCoverType(book.CoverType.HARDCOVER)
        little_women.SetPages(306)
        self.assertEqual(1.112, little_women.GetThickness())

    def test_GetTitle(self):
        """Tests that title is returned in its raw form (a tuple)."""
        little_women = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        self.assertIsInstance(little_women.GetTitle(), tuple)

    def test_GetTitleFormatted(self):
        """Tests that title is returned as a formatted string with capitalized words."""
        little_women = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        self.assertEqual("Little Women", little_women.GetTitleFormatted())

    def test_GetPages(self):
        """Tests that GetPages returns the correct page count when set or unset."""
        little_women = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        self.assertIsNone(little_women.GetPages())

        little_women.SetPages(306)
        self.assertEqual(306, little_women.GetPages())

    def test_GetEdition(self):
        """Tests that GetEdition returns the correct edition."""
        war_and_peace = book.Book("War and Peace", ("Leo", "", "Tolstoy"))
        war_and_peace.SetEdition(10)
        self.assertEqual(10, war_and_peace.GetEdition())

    def testGetCoverType(self):
        """Tests that GetCoverType returns the correct cover type."""
        war_and_peace = book.Book("War and Peace", ("Leo", "", "Tolstoy"))
        war_and_peace.SetCoverType(book.CoverType.HARDCOVER)
        self.assertEqual(book.CoverType.HARDCOVER, war_and_peace.GetCoverType())

    def test_SetPages(self):
        """Tests that SetPages raises an exception when attempting to set to a float value."""
        war_and_peace = book.Book("War and Peace", ("Leo", "", "Tolstoy"))

        # Example uses a 'lambda' as a wrapper to catch the exception.
        self.assertRaises(ValueError, lambda: war_and_peace.SetPages(1000.5))

        # Example uses a 'with' as a wrapper to catch the exception.
        with self.assertRaises(ValueError):
            war_and_peace.SetPages(1000.5)

if __name__ == '__main__':
    unittest.main()
