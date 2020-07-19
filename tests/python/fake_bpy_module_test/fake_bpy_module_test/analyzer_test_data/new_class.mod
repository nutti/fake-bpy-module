{
    "new": [
        {
            "type": "class",
            "name": "ClassB",
            "module": "module.a",
            "description": "ClassB description",
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassB",
                "module": "module.a",
                "data_type": "attr_1 type"
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassB",
                "module": "module.a",
                "parameters": [],
                "parameter_details": [],
                "return": {
                    "type": "return",
                    "description": "method_1 return description",
                    "data_type": "method_1 return type"
                }
            },
            {
                "type": "classmethod",
                "name": "classmethod_1",
                "description": "classmethod_1 description",
                "class": "ClassB",
                "module": "module.a",
                "parameters": ["arg_1"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "classmethod_1 arg_1 description",
                    "data_type": "classmethod_1 arg_1 type"
                }]
            },
            {
                "type": "staticmethod",
                "name": "staticmethod_1",
                "description": "staticmethod_1 description",
                "class": "ClassB",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=(0, 0)"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "staticmethod_1 arg_1 description",
                    "data_type": "staticmethod_1 arg_1 type"
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "staticmethod_1 arg_2 description",
                    "data_type": "staticmethod_1 arg_2 type"
                }]
            }]
        }
    ]
}