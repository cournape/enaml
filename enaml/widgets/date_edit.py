#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import datetime

from traits.api import Date, Event, Instance, Str

from .control import Control, IControlImpl
from ..util.trait_types import Bounded

class IDateEditImpl(IControlImpl):

    def parent_date_changed(self, date):
        raise NotImplementedError

    def parent_minimum_date_changed(self, date):
        raise NotImplementedError

    def parent_maximum_date_changed(self, date):
        raise NotImplementedError

    def parent_format_changed(self, date_format):
        raise NotImplementedError


class DateEdit(Control):
    """ A date widget.

    A DateEdit displays a Python datetime.date using an appropriate
    toolkit specific control. This is a smaller control than what is
    provided by Calendar.

    Attributes
    ----------
    date : Bounded
        The currently selected date. Default is the current date. The
        value is bounded between :attr:`minimum_date` and
        :attr:`maximum_date`. Attempts to assign a value outside of this
        range will result in a TraitError.

    minimum_date : Date
        The minimum date available in the date edit. If not defined then
        the default value is September 14, 1752.

    maximum_date : Date
        The maximum date available in the date edit. If not defined then
        the default value is December 31, 7999

    format : Str
        A python date format string to format the date. If none is
        supplied (or is invalid) the system locale setting is used.
        This may not be supported by all backends.

    date_changed : Event
        Triggered whenever the user clicks and changes the control. The
        event payload will be the date on the control.

    """
    minimum_date = Date(datetime.date(1752, 9, 14))

    maximum_date = Date(datetime.date(7999, 12, 31))

    date = Bounded(datetime.date.today(), low='minimum_date', high='maximum_date')

    format = Str

    date_changed = Event

    #---------------------------------------------------------------------------
    # Overridden parent traits
    #---------------------------------------------------------------------------
    toolkit_impl = Instance(IDateEditImpl)


DateEdit.protect('date_changed')

