import unittest

from main import lev_rec, lev_matrix, lev_matrix_recursion, damer_lev
from main import random_string

class TestDistanse(unittest.TestCase):
        
    def testEmpty(self):
        self.assertEqual(self.function("", ""), 0)

    def testSame(self):
        self.assertEqual(self.function("abc", "abc"), 0)
        self.assertEqual(self.function("0", "0"), 0)

    def testDifferent(self):
        self.assertEqual(self.function("a", ""), 1)
        self.assertEqual(self.function("", "1"), 1)
        self.assertEqual(self.function("b", "c"), 1)
        self.assertEqual(self.function("bc", "b"), 1)
        self.assertEqual(self.function("bc", "c"), 1)
        self.assertEqual(self.function("ab", "cd"), 2)


class TestLevDistanse(TestDistanse):
    def setUp(self):
        self.function = lev_matrix
    def testTypo(self):
        self.assertEqual(self.function("ac", "ca"), 2)
        self.assertEqual(self.function("abc", "cba"), 2)

                         
class TestDamLevDistanse(TestDistanse):
    def setUp(self):
        self.function = damer_lev
    def testTypo(self):
        self.assertEqual(self.function("ac", "ca"), 1)
        self.assertEqual(self.function("abc", "cba"), 2)
                         

class TestTwoFunctions(unittest.TestCase):

    n = 15
    def testCompareSameLen(self):
        for i in range(TestTwoFunctions.n):
            str1 = random_string(5)
            str2 = random_string(5)
            self.assertEqual(self.f1(str1, str2), self.f2(str1, str2))

    def testCompareDifLen(self):
        for i in range(TestTwoFunctions.n):
            str1 = random_string(3)
            str2 = random_string(5)
            self.assertEqual(self.f1(str1, str2), self.f2(str1, str2))

    def testCompareEmpty(self):
        for i in range(TestTwoFunctions.n):
            str1 = random_string(4)
            str2 = random_string(5)
            self.assertEqual(self.f1(str1, str2), self.f2(str1, str2))
        

class TestLev(TestTwoFunctions):
    def setUp(self):
        self.f1 = lev_rec
        self.f2 = lev_matrix

        
class TestDamLev(TestTwoFunctions):
    def setUp(self):
        self.f1 = lev_matrix_recursion
        self.f2 = damer_lev
    

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLev)
    suite.addTests(unittest.TestLoader().
                loadTestsFromTestCase(TestDamLev))
    suite.addTests(unittest.TestLoader().
                loadTestsFromTestCase(TestDamLevDistanse))
    suite.addTests(unittest.TestLoader().
                loadTestsFromTestCase(TestLevDistanse))
    unittest.TextTestRunner().run(suite)
    #unittest.main()