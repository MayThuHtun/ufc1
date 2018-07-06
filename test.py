
# -*- coding: utf-8 -*-
import unittest
import zg2uni

class TestZG2UNI(unittest.TestCase):
    def test_article_one(self):
        zawgyi = u'''ကခဂဃငစဆဇညဋဌဍဏတထဒဓနပဖဗဘမယရလ၀သဟဠအ'''
        unicode = u'''ကခဂဃငစဆဇညဋဌဍဏတထဒဓနပဖဗဘမယရလ၀သဟဠအ'''
        result = zg2uni.convert(zawgyi)
        self.assertEqual(unicode, result, "Failed converting Article One")


if __name__ == "__main__":
    unittest.main()
