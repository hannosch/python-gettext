# -*- coding: utf-8 -*-
import os

import unittest2 as unittest

from pythongettext.msgfmt import Msgfmt
from pythongettext.msgfmt import PoSyntaxError

FOLDER = os.path.dirname(__file__)


class TestWriter(unittest.TestCase):

    def compare_po_mo(self, poname, moname):
        po_file = None
        mo_file = None
        try:
            po_file = file(os.path.join(FOLDER, poname), 'rb')
            po = Msgfmt(po_file).get()
            mo_file = file(os.path.join(FOLDER, moname), 'rb')
            mo = ''.join(mo_file.readlines())
        finally:
            if po_file is not None:
                po_file.close()
            if mo_file is not None:
                mo_file.close()

        self.assertEqual(mo, po)

    def test_empty(self):
        self.compare_po_mo('test_empty.po', 'test_empty.mo')

    def test_test(self):
        self.compare_po_mo('test.po', 'test.mo')

    def test_test2(self):
        self.compare_po_mo('test2.po', 'test2.mo')

    def test_msgctxt(self):
        self.compare_po_mo('test3.po', 'test3.mo')

    def test_test4(self):
        po_file = file(os.path.join(FOLDER, 'test4.po'), 'rb')
        po = Msgfmt(po_file)
        po.read(header_only=True)
        self.assertTrue(po.messages[''].startswith('Project-Id-Version: foo'))

    def test_test5(self):
        po_file = file(os.path.join(FOLDER, 'test5.po'), 'rb')
        po = Msgfmt(po_file)
        with self.assertRaises(PoSyntaxError):
            po.read()

    def test_test5_unicode_name(self):
        po_file = file(os.path.join(FOLDER, 'test5.po'), 'rb')
        po = Msgfmt(po_file, name=u'dømain')
        with self.assertRaises(PoSyntaxError):
            po.read()

    def test_escape(self):
        po_file = file(os.path.join(FOLDER, 'test_escape.po'), 'rb')
        po = Msgfmt(po_file)
        with self.assertRaises(PoSyntaxError) as e:
            po.read()
        self.assertTrue('line 19' in e.exception.msg)

    def test_unicode_bom(self):
        self.compare_po_mo('test_unicode_bom.po', 'test_unicode_bom.mo')
