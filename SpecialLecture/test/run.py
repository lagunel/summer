import unittest
from CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))

    def test_a(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        print(l)
        self.assertEqual(3, len(l))


    def test_b(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual("b2", l[1][1])

    def test_c(self):
        try:
            printer = CSVPrinter("aaa.csv")
            printer.read()
            unittest.TestCase.fail("This line should be invoked")
        except FileNotFoundError as e:
            pass



