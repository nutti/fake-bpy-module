def actuator_add(type='', name="", object=""):
    '''Add an actuator to the active object 

    :param type: Type, Type of actuator to add 
    :type type: enum in [], (optional)
    :param name: Name, Name of the Actuator to add 
    :type name: string, (optional, never None)
    :param object: Object, Name of the Object to add the Actuator to 
    :type object: string, (optional, never None)
    '''

    pass


def actuator_move(actuator="", object="", direction='UP'):
    '''Move Actuator 

    :param actuator: Actuator, Name of the actuator to edit 
    :type actuator: string, (optional, never None)
    :param object: Object, Name of the object the actuator belongs to 
    :type object: string, (optional, never None)
    :param direction: Direction, Move Up or Down 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def actuator_remove(actuator="", object=""):
    '''Remove an actuator from the active object 

    :param actuator: Actuator, Name of the actuator to edit 
    :type actuator: string, (optional, never None)
    :param object: Object, Name of the object the actuator belongs to 
    :type object: string, (optional, never None)
    '''

    pass


def controller_add(type='LOGIC_AND', name="", object=""):
    '''Add a controller to the active object 

    :param type: Type, Type of controller to addLOGIC_AND And, Logic And.LOGIC_OR Or, Logic Or.LOGIC_NAND Nand, Logic Nand.LOGIC_NOR Nor, Logic Nor.LOGIC_XOR Xor, Logic Xor.LOGIC_XNOR Xnor, Logic Xnor.EXPRESSION Expression.PYTHON Python. 
    :type type: enum in ['LOGIC_AND', 'LOGIC_OR', 'LOGIC_NAND', 'LOGIC_NOR', 'LOGIC_XOR', 'LOGIC_XNOR', 'EXPRESSION', 'PYTHON'], (optional)
    :param name: Name, Name of the Controller to add 
    :type name: string, (optional, never None)
    :param object: Object, Name of the Object to add the Controller to 
    :type object: string, (optional, never None)
    '''

    pass


def controller_move(controller="", object="", direction='UP'):
    '''Move Controller 

    :param controller: Controller, Name of the controller to edit 
    :type controller: string, (optional, never None)
    :param object: Object, Name of the object the controller belongs to 
    :type object: string, (optional, never None)
    :param direction: Direction, Move Up or Down 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def controller_remove(controller="", object=""):
    '''Remove a controller from the active object 

    :param controller: Controller, Name of the controller to edit 
    :type controller: string, (optional, never None)
    :param object: Object, Name of the object the controller belongs to 
    :type object: string, (optional, never None)
    '''

    pass


def links_cut(path=None, cursor=9):
    '''Remove logic brick connections 

    :param path: path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param cursor: Cursor 
    :type cursor: int in [0, inf], (optional)
    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def sensor_add(type='', name="", object=""):
    '''Add a sensor to the active object 

    :param type: Type, Type of sensor to add 
    :type type: enum in [], (optional)
    :param name: Name, Name of the Sensor to add 
    :type name: string, (optional, never None)
    :param object: Object, Name of the Object to add the Sensor to 
    :type object: string, (optional, never None)
    '''

    pass


def sensor_move(sensor="", object="", direction='UP'):
    '''Move Sensor 

    :param sensor: Sensor, Name of the sensor to edit 
    :type sensor: string, (optional, never None)
    :param object: Object, Name of the object the sensor belongs to 
    :type object: string, (optional, never None)
    :param direction: Direction, Move Up or Down 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def sensor_remove(sensor="", object=""):
    '''Remove a sensor from the active object 

    :param sensor: Sensor, Name of the sensor to edit 
    :type sensor: string, (optional, never None)
    :param object: Object, Name of the object the sensor belongs to 
    :type object: string, (optional, never None)
    '''

    pass


def view_all():
    '''Resize view so you can see all logic bricks 

    '''

    pass
