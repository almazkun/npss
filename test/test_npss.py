from unittest import TestCase

from npss import npss, argv_pars


class TestArgvPars(TestCase):
    arguments_list = {
        30: [],
        30: ["main.py"],
        30: ["main.py", "-1"],
        30: ["main.py", "-1", "0"],
        1: ["main.py", "-1", "0", "1"],
        2: ["main.py", "-1", "0", "2"],
        3: ["3"],
        6: ["5", "6"],
        7: ["7.9", "7"],
        100: ["7.9", "7", "50", "100"],
    }

    def test_argv_pars(self):
        for expected, arguments in self.arguments_list.items():
            self.assertEqual(expected, argv_pars(arguments))


class TestPss(TestCase):
    def test_pss(self):
        for i in range(1, 100):
            p = npss(i)
            self.assertTrue(p)
            self.assertIn("-", p)
            self.assertEqual(i, len(p))
