def is_registered(function):
    '''Check if this function is registered as a timer. 

    :param function: Function to check. 
    :type function: int
    :return:  True when this function is registered, otherwise False. 
    '''

    pass


def register(function, first_interval=0, persistent=False):
    '''Add a new function that will be called after the specified amount of seconds. The function gets no arguments and is expected to return either None or a float. If None is returned, the timer will be unregistered. A returned number specifies the delay until the function is called again. functools.partial can be used to assign some parameters. 

    :param function: The function that should called. 
    :type function: Callable[[], Union[float, None]]
    :param first_interval: Seconds until the callback should be called the first time. 
    :type first_interval: float
    :param persistent: Don’t remove timer when a new file is loaded. 
    :type persistent: bool
    '''

    pass


def unregister(function):
    '''Unregister timer. 

    :param function: Function to unregister. 
    :type function: function
    '''

    pass
