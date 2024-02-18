import os
import typing
import bpy.types


GenericType = typing.TypeVar("GenericType")


class bpy_prop_collection(typing.Generic[GenericType]):
    pass


class ClassA:
    attr_1: bpy.types.bpy_prop_collection["ClassB"] = None
    """ attr_1 description

    :type: bpy.types.bpy_prop_collection['ClassB']
    """
