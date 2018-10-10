# -*- coding: utf-8 -*-
"""
This module will cover some testcases include services,opensource products , iot devices .. login form
"""
import unittest
from core import tbrowser		
class TestParseSimpleLoginForm(unittest.TestCase):

    def test_wordpress(self):
        proc = tbrowser.startBrowser()
        proc.open("https://login.wordpress.org/?locale=en_US")
        result, login = tbrowser.parseLoginForm(proc.forms())
        self.assertEqual(login, ['pwd', 'log'])
        proc.close()
        return True
    
    def test_webmin_customport(self):
        proc = tbrowser.startBrowser()
        proc.open("http://181.198.70.13:10000/")
        result, login = tbrowser.parseLoginForm(proc.forms())
        self.assertEqual(login, ['pass', 'user'])
        proc.close()
        return True

if __name__ == '__main__':
    unittest.main()