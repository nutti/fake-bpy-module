{
    "update": [
        {
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description updated",
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_1 type updated"
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description updated",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=\"test2\""],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_1 arg_1 description",
                    "data_type": "method_1 arg_1 type updated"
                }],
                "return": {
                    "type": "return",
                    "description": "method_1 return description updated",
                    "data_type": "method_1 return type"
                }
            }]
        }
    ]
}