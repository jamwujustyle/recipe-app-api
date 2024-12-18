"""
sample tests
"""

from django.test import SimpleTestCase
from .calc import add, subtract


class CalcTests(SimpleTestCase):
    """
    test calc module
    """

    def test_add_numbers(self):
        """
        test adding numbers
        """
        response = add(5, 6)
        self.assertEquals(response, 11)

    def test_subtract(self):
        response = subtract(10, 5)
        self.assertEquals(response, 5)
