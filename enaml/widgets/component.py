#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from abc import abstractmethod, abstractproperty

from traits.api import Instance, List, Property, Bool, Tuple, Event, on_trait_change

from .base_component import BaseComponent, AbstractTkBaseComponent
from .layout.box_model import BoxModel
from .layout.symbolics import BaseConstraint
from .layout.layout_ns import LayoutNS
from .layout.layout_manager import AbstractLayoutManager
from .layout.constraints_layout import ConstraintsLayout


class AbstractTkComponent(AbstractTkBaseComponent):
    """ The abstract toolkit Component interface.

    A toolkit component is responsible for handling changes on a shell 
    Component and proxying those changes to and from its internal toolkit
    widget.

    """
    @abstractproperty
    def toolkit_widget(self):
        """ An abstract property that should return the gui toolkit 
        widget being managed by the object.

        """
        raise NotImplementedError

    @abstractmethod
    def size(self):
        """ Return the size of the internal toolkit widget as a 
        (width, height) tuple of integers.

        """
        raise NotImplementedError
    
    @abstractmethod
    def size_hint(self):
        """ Returns a (width, height) tuple of integers which represent
        the suggested size of the widget for its current state. This 
        value is used by the layout manager to determine how much 
        space to allocate the widget.

        """
        raise NotImplementedError

    @abstractmethod
    def resize(self, width, height):
        """ Resizes the internal toolkit widget according the given
        width and height integers.

        """
        raise NotImplementedError
    
    @abstractmethod
    def set_min_size(self, min_width, min_height):
        """ Set the hard minimum width and height of the widget. A widget
        should not be able to be resized smaller than this value.

        """
        raise NotImplementedError

    @abstractmethod
    def pos(self):
        """ Returns the position of the internal toolkit widget as an 
        (x, y) tuple of integers. The coordinates should be relative to
        the origin of the widget's parent.

        """
        raise NotImplementedError
    
    @abstractmethod
    def move(self, x, y):
        """ Moves the internal toolkit widget according to the given
        x and y integers which are relative to the origin of the
        widget's parent.

        """
        raise NotImplementedError
    
    @abstractmethod
    def geometry(self):
        """ Returns an (x, y, width, height) tuple of geometry info
        for the internal toolkit widget. The semantic meaning of the
        values are the same as for the 'size' and 'pos' methods.

        """
        raise NotImplementedError
    
    @abstractmethod
    def set_geometry(self, x, y, width, height):
        """ Sets the geometry of the internal widget to the given 
        x, y, width, and height values. The semantic meaning of the
        values is the same as for the 'resize' and 'move' methods.

        """
        raise NotImplementedError


class Component(BaseComponent):
    """ A BaseComponent subclass that adds a box model and support
    for constraints specification. This class represents the most
    basic visible widget in Enaml.

    """
    #: A private attribute that holds the box model instance
    #: for this component. 
    _box_model = Instance(BoxModel, ())

    #: A private boolean indicating if the contraints have changed
    #: and need to be updated on the next pass.
    _needs_update_constraints = Bool(True)

    #: A private boolean indicating if the component needs to relayout
    #: its children
    _needs_layout = Bool(True)

    # XXX the following two traits will probably need to be 
    # overridden on a per-control basis to do the natural thing.

    #: How strong a component hugs it's content
    hug = Tuple('strong', 'strong')

    #: How strong a component resists compression
    compress = Tuple('strong', 'strong')

    #: An event that should be emitted by the abstract obj when
    #: its size hint has updated.
    size_hint_updated = Event

    #: An object that manages the layout of this component and its 
    #: direct children. The default is simple constraints based
    layout = Instance(AbstractLayoutManager)

    #: A list of linear constraints defined for this object.
    constraints = List(Instance(BaseConstraint))

    #: A read-only symbolic object that represents the left 
    #: boundary of the component
    left = Property

    #: A read-only symbolic object that represents the top 
    #: boundary of the component
    top = Property

    #: A read-only symbolic object that represents the width
    #: of the component
    width = Property

    #: A read-only symbolic object that represents the height 
    #: of the component
    height = Property

    #: A read-only symbolic object that represents the right 
    #: boundary of the component
    right = Property

    #: A read-only symbolic object that represents the bottom 
    #: boundary of the component
    bottom = Property

    #: A read-only symbolic object that represents the vertical 
    #: center of the component
    v_center = Property

    #: A read-only symbolic object that represents the horizontal 
    #: center of the component
    h_center = Property

    #: A read-only object providing a convenient entry point for
    #: constraint-related layout functions.
    # FIXME: This is a dumb hack to be removed when there is better support in
    # the Enaml syntax.
    L = Property

    #: A read-only property that returns the toolkit specific widget
    #: being managed by the abstract widget.
    toolkit_widget = Property

    #: Overridden parent class trait
    abstract_obj = Instance(AbstractTkComponent)

    def _get_left(self):
        """ Property getter for the 'left' property.

        """
        return self._box_model.left
    
    def _get_top(self):
        """ Property getter for the 'top' property.

        """
        return self._box_model.top
    
    def _get_width(self):
        """ Property getter for the 'width' property.

        """
        return self._box_model.width
    
    def _get_height(self):
        """ Property getter for the 'height' property.

        """
        return self._box_model.height
    
    def _get_right(self):
        """ Property getter for the 'right' property.

        """
        return self._box_model.right
    
    def _get_bottom(self):
        """ Property getter for the 'bottom' property.

        """
        return self._box_model.bottom
    
    def _get_v_center(self):
        """ Property getter for the 'v_center' property.

        """
        return self._box_model.v_center
    
    def _get_h_center(self):
        """ Property getter for the 'h_center' property.

        """
        return self._box_model.h_center
    
    def _layout_default(self):
        """ Default value for the layout manager.

        """
        return ConstraintsLayout(self)

    def _get_L(self):
        """ Property getter for the 'L' property.

        """
        return LayoutNS()

    def size(self):
        """ Returns the size tuple as given by the abstract widget.

        """
        return self.abstract_obj.size()
    
    def size_hint(self):
        """ Returns the size hint tuple as given by the abstract widget
        for its current state.

        """
        return self.abstract_obj.size_hint()

    def resize(self, width, height):
        """ Resize the abstract widget as specified by the given
        width and height integers.

        """
        self.abstract_obj.resize(width, height)
    
    def set_min_size(self, min_width, min_height):
        """ Set the hard minimum width and height of the widget. A widget
        should not be able to be resized smaller than this value.

        """
        self.abstract_obj.set_min_size(min_width, min_height)

    def pos(self):
        """ Returns the position tuple as given by the abstract widget.

        """
        return self.abstract_obj.pos()
    
    def move(self, x, y):
        """ Moves the abstract widget to the given x and y integer
        coordinates which are given relative to the parent origin.

        """
        self.abstract_obj.move(x, y)
    
    def geometry(self):
        """ Returns the (x, y, width, height) geometry tuple as given
        by the abstract widget.

        """
        return self.abstract_obj.geometry()
    
    def set_geometry(self, x, y, width, height):
        """ Sets the geometry of the abstract widget with the given
        integer values.

        """
        self.abstract_obj.set_geometry(x, y, width, height)

    def _get_toolkit_widget(self):
        """ Property getter for the 'toolkit_widget' property.

        """
        return self.abstract_obj.toolkit_widget

    def setup(self):
        """ Run the setup process for the ui tree.

        This is overridden to add the layout set up.

        """
        super(Component, self).setup()

        if len(self.children) > 0:
            self.initialize_layout()

    def initialize_layout(self):
        """ Initialize the layout for the first time.

        """
        if len(self.children) > 0:
            self.layout.initialize()
            for child in self.children:
                child.initialize_layout()

    def update_constraints_if_needed(self):
        """ Update the constraints of this component if necessary. This 
        is typically the case when a constraint has been changed.

        """
        if self._needs_update_constraints and len(self.children) > 0:
            self.toolkit.invoke_later(self.update_constraints)

    def set_needs_update_constraints(self, needs=True):
        """ Indicate that the constraints for this component should be
        updated some time later.

        """
        self._needs_update_constraints = needs
        if needs and len(self.children) > 0:
            self.toolkit.invoke_later(self.update_constraints)

    def update_constraints(self):
        """ Update the constraints for this component.

        """
        self.layout.update_constraints()
        for child in self.children:
            child.update_constraints()
        self._needs_update_constraints = False

    def layout_if_needed(self):
        """ Refreshes the layout of this component if necessary. This 
        will typically be needed if this component has been resized or 
        the sizes of any of its children have been changed.

        """
        if self._needs_layout and len(self.children) > 0:
            self.toolkit.invoke_later(self.do_layout)

    def set_needs_layout(self, needs=True):
        """ Indicate that the layout should be refreshed some time 
        later.

        """
        self._needs_layout = needs
        if needs and len(self.children) > 0:
            self.toolkit.invoke_later(self.do_layout)

    def do_layout(self):
        """ Updates the layout of this component.

        """
        self.layout.layout()
        self._needs_layout = False

    @on_trait_change('children:size_hint_updated, children:hug, children:compress')
    def handle_size_hint_changed(self, child, name, old, new):
        self.toolkit.invoke_later(self.layout.update_size_cns, child)
        self.set_needs_layout()
    
    @on_trait_change('constraints[]')
    def handle_constraints_changed(self):
        if self.layout._initialized:
            self.set_needs_update_constraints()
            self.set_needs_layout()


