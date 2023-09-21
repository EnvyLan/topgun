from unittest import TestCase


class Test(TestCase):

    def test_find_top1(self):
        from topgun.nlphandler import find_top1
        print(find_top1("help me to validation company name does match"))

    def test_find_top1_not_match(self):
        from topgun.nlphandler import find_top1
        print(find_top1("what your name"))

        # self.assertRaises(find_top1("what your name"), Exception)