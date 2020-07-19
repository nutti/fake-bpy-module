{
    "append": [
        {
            "name": "ClassA",
            "type": "class",
            "module": "module.a",
            "attributes": [{
                "name": "attr_2",
                "type": "attribute",
                "description": "attr_2 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_2 type"
            }],
            "methods": [{
                "name": "method_2",
                "type": "function",
                "description": "method_2 description",
                "module": "module.a",
                "parameters": ["arg_1"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_2 arg_1 description",
                    "data_type": "method_2 arg_1 type"
                }],
                "return": {
                    "type": "return",
                    "description": "method_2 return description",
                    "data_type": "method_2 return type"
                }
            }]
        }
    ]
}