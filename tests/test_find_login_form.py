# -*- coding: utf-8 -*-
"""
This module will cover some testcases include:
    services,opensource products , iot devices .. login form
"""
import unittest
from core import tbrowser
class TestParseSimpleLoginForm(unittest.TestCase):
    """This class will cover very simple login form , it should be passall testcases"""
    def test_wordpress(self):
        """Test parse wordpress login form """
        proc = tbrowser.startBrowser()
        proc.open("https://login.wordpress.org/?locale=en_US")
        _, login = tbrowser.parseLoginForm(proc.forms())
        self.assertEqual(login, ['pwd', 'log'])
        proc.close()
        return True
    def test_webmin_customport(self):
        """Test parse webmin login form with custom port  """
        proc = tbrowser.startBrowser()
        proc.open("http://181.198.70.13:10000/")
        _, login = tbrowser.parseLoginForm(proc.forms())
        self.assertEqual(login, ['pass', 'user'])
        proc.close()
        return True
    def test_github(self):
        """Test parse github login form with"""
        proc = tbrowser.startBrowser()
        proc.open("https://github.com/login?return_to=%2Fjoin%3Fsource%3Dheader-home")
        _, login = tbrowser.parseLoginForm(proc.forms())
        self.assertEqual(login, ['password', 'commit'])
        proc.close()
        return True
if __name__ == '__main__':
    unittest.main()
    