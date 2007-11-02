import os
import sys
import unittest

from cStringIO import StringIO

from pythongettext.msgfmt import Msgfmt


def this_folder(name):
    module = sys.modules[__name__]
    return os.path.dirname(os.path.abspath(module.__file__))


class TestReader(unittest.TestCase):

    def test_fail(self):
        self.failIf(False)


class TestWriter(unittest.TestCase):
    
    def setUp(self):
        self.folder = this_folder(__name__)

    def compare_po_mo(self, poname, moname):
        po_file = None
        mo_file = None
        try:
            po_file = file(os.path.join(self.folder, poname), 'rb')
            po = Msgfmt(po_file).get()
            mo_file = file(os.path.join(self.folder, moname), 'rb')
            mo = ''.join(mo_file.readlines())
        finally:
            if po_file is not None:
                po_file.close()
            if mo_file is not None:
                mo_file.close()

        self.failUnless(mo == po)

    def test_test(self):
        self.compare_po_mo('test.po', 'test.mo')

    def test_test2(self):
        self.compare_po_mo('test2.po', 'test2.mo')

    def test_msgctxt(self):
        self.compare_po_mo('test3.po', 'test3.mo')

    def test_test4(self):
        po_file = file(os.path.join(self.folder, 'test4.po'), 'rb')
        po = Msgfmt(po_file)
        po.read(header_only=True)
        self.failUnless(po.messages[''].startswith('Project-Id-Version: foo'))

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestReader))
    suite.addTest(makeSuite(TestWriter))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
