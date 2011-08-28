from traits.api import Date, Event

from .i_element import IElement


class ICalendar(IElement):
    """ A calendar widget.

    A Calendar displays a Python datetime.date using an appropriate
    toolkit specific control.
    
    Attributes
    ----------
    date : Date
        The currently selected date. This is only updated when the user
        *activates* the control via double-click or pressing enter.

    minimum_date : Date
        The minimum date available in the calendar.

    maximum_date : Date
        The maximum date available in the calendar.
    
    selected : Event
        Triggered whenever the user clicks or changes the control. The
        event payload will be the date.
    
    activated : Event
        Triggered whenever the user activates a new date via double
        click or pressing enter. The event payload will be the date.

    """    
    date = Date

    minimum_date = Date

    maximum_date = Date

    selected = Event

    activated = Event
