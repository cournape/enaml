#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import unittest
from uuid import uuid4

from enaml.qt.qt.QtCore import Qt
from enaml.qt.qt.QtGui import QApplication, QSlider
from enaml.qt.qt_slider import QtSlider
from enaml.qt.qt_local_pipe import QtLocalPipe

class TestQtSlider(unittest.TestCase):
    """ Unit tests for the QtSlider

    """
    def setUp(self):
        """ Set up the widget for testing

        """
        self.slider = QtSlider(None, uuid4().hex, QtLocalPipe(),
                               QtLocalPipe())
        self.slider.create()

    def test_set_maximum(self):
        """ Test the QtSlider's set_maximum command

        """
        maximum = 50
        self.slider.recv('set_maximum', {'value':maximum})
        self.assertEqual(self.slider.widget.maximum(), maximum)

    def test_set_minimum(self):
        """ Test the QtSlider's set_minimum command

        """
        minimum = 10
        self.slider.recv('set_minimum', {'value':minimum})
        self.assertEqual(self.slider.widget.minimum(), minimum)

    def test_set_value(self):
        """ Test the QtSlider's set_value command

        """
        value = 20
        self.slider.recv('set_value', {'value':value})
        self.assertEqual(self.slider.widget.value(), value)

    def test_set_orientation(self):
        """ Test the QtSlider's set_orientation command

        """
        self.slider.recv('set_orientation', {'value':'vertical'})
        self.assertEqual(self.slider.widget.orientation(), Qt.Vertical)

    def test_set_page_step(self):
        """ Test the QtSlider's set_page_step command

        """
        step = 2
        self.slider.recv('set_page_step', {'value':step})
        self.assertEqual(self.slider.widget.pageStep(), step)

    def test_set_single_step(self):
        """ Test the QtSlider's set_single_step command

        """
        step = 10
        self.slider.recv('set_single_step', {'value':step})
        self.assertEqual(self.slider.widget.singleStep(), step)

    def test_set_tick_interval(self):
        """ Test the QtSlider's set_tick_interval command

        """
        interval = 5
        self.slider.recv('set_tick_interval', {'value':interval})
        self.assertEqual(self.slider.widget.tickInterval(), interval)

    def test_set_tick_position(self):
        """ Test the QtSlider's set_tick_position command

        """
        self.slider.recv('set_tick_position', {'value':'left'})
        self.assertEqual(self.slider.widget.tickPosition(), QSlider.TicksLeft)

    def test_set_tracking(self):
        """ Test the QtSlider's set_tracking command

        """
        self.slider.recv('set_tracking', {'value':False})
        self.assertEqual(self.slider.widget.hasTracking(), False)
        
if __name__ == '__main__':
    app = QApplication([])
    unittest.main()
