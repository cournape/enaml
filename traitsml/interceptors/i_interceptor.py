from traits.api import Interface


class IInterceptor(Interface):
    """ Defines the IInterceptor interface for TraitsML.

    An interceptor is injected into a HasTraits object and is
    responsible for intercepting the code flow of a given trait. 

    Methods
    -------
    inject(obj, name, global_ns, local_ns)
        Hooks up the interceptor object for the trait on the object.

    """
    def inject(self, obj, name, global_ns, local_ns):
        """ Hooks up the interceptor object for the trait on the object.

        Injects the interceptor into the object for the trait at the
        provided trait_name in whatever fashion necessary to intercept
        the code flow. The provided namespaces are the context 
        in which the interceptor should execute.

        Arguments
        ---------
        obj : HasTraits
            The HasTraits object which holds the trait we wish to 
            intercept. Beware of reference cycle if maintaining a 
            strong ref to this object.

        trait_name : string
            The name of the trait on obj we wish to intercept.
        
        global_ns : dict
            The global namespace in which any expression code 
            should execute.

        local_ns : dict
            The local namespace in which any expression code
            should execute.

        Returns
        -------
        result : None

        """
        raise NotImplementedError


class IInterceptorFactory(Interface):
    """ Defines the IInterceptorFactory interface for TraitsML.

    The IInterceptorFactory defines the interface for creating factories
    that create IInterceptor objects which bind code and/or expressions 
    to the TraitsML object tree.

    Methods
    -------
    interceptor()
        Creates an IInterceptor instance that is primed for 
        injection into a HasTraits object.

    """
    def interceptor(self):
        """ Creates an IInterceptor instance.

        Creates an IInterceptor instance that is primed for 
        injection into a HasTraits object.

        Arguments
        ---------
        None

        Returns
        -------
        result : IInterceptor
            The interceptor that will handle this code.

        Raises
        ------
        XXX

        """
        raise NotImplementedError
