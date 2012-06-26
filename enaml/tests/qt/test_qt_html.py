#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import unittest
from uuid import uuid4

from enaml.qt.qt.QtGui import QApplication
from enaml.qt.qt_html import QtHtml
from enaml.qt.qt_local_pipe import QtLocalPipe

class TestQtHtml(unittest.TestCase):
    """ Unit tests for the QtHtml

    """
    def setUp(self):
        """ Set up the widget for testing

        """
        self.html = QtHtml(None, uuid4().hex, QtLocalPipe(),
                           QtLocalPipe())
        self.html.create()

    def test_set_source(self):
        """ Test the QtHtml's set_source command

        """
        source = "<html><p>hello</p></html>"
        self.html.recv('set_source', {'value':source})
        # Qt wraps the html with a bunch of metadata and extra tags,
        # so we compare the plain text
        self.assertEqual(self.html.widget.toPlainText(), 'hello')

if __name__ == '__main__':
    app = QApplication([])
    unittest.main()
