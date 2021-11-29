from unittest import TestCase

from npss import npss, argv_pars, main


class TestArgvPars(TestCase):
    arguments_list = {
        30: [],
        30: ["main.py"],
        1: ["main.py", "-1"],
        1: ["main.py", "-1", "0"],
        1: ["main.py", "-1", "0", "1"],
        1: ["main.py", "-1", "0", "2"],
        10000000000: ["main.py", "10000000000", "0", "2"],
        30: ["3"],
        6: ["5", "6"],
        7: ["7.9", "7", "50", "100"],
    }

    def test_argv_pars(self):
        for expected, arguments in self.arguments_list.items():
            self.assertEqual(expected, argv_pars(arguments))


class TestNpss(TestCase):
    def test_npss(self):
        for i in range(1, 100):
            p = npss(i)
            self.assertTrue(p)
            self.assertIn("-", p)
            self.assertEqual(i, len(p))


class TestMain(TestCase):
    def test_main(self):
        p = main()
        self.assertTrue(p)
        self.assertIn("-", p)
        self.assertEqual(30, len(p))
