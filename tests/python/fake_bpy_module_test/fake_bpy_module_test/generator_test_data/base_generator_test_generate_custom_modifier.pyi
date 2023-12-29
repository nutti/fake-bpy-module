import sys
import typing
import os
import bpy.types

GenericType = typing.TypeVar("GenericType")

class bpy_prop_collection(typing.Generic[GenericType]): ...

class ClassA:
    attr_1: bpy.types.bpy_prop_collection["ClassB"]
    """ attr_1 description

    :type: bpy.types.bpy_prop_collection['ClassB']
    """
