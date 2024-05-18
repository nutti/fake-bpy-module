.. mod-type:: update

.. module:: bpy.app.timers

.. function:: is_registered(function)

   :arg function: Function to check.
   :type function: typing.Callable[[], float]
   :mod-option arg function: skip-refine

.. function:: register(function)

   :arg function: The function that should called.
   :type function: typing.Callable[[], float]
   :mod-option arg function: skip-refine

.. function:: unregister(function)

   :arg function: Function to unregister.
   :type function: typing.Callable[[], float]
   :mod-option arg function: skip-refine
