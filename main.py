# vim:fileencoding=utf-8:ts=4:sw=4:sts=4:expandtab


from rich.pretty import pprint
from Granite import AS3


person_as3_input = {
    "+Type": "Object",
    "Name": "String",
    "Age": "Integer",
} 

person_as3_validator = AS3(person_as3_input)

person_data_input = {"Name": 'Jason', 'Age': '24'}

person_data_output = person_as3_validator(person_data_input)



pprint("person AS3 Input Struct:")
pprint(person_as3_input, expand_all=True)
print()

pprint("person AS3 Internal Struct:")
pprint(person_as3_validator.Struct, expand_all=True)
print()

pprint("person_data_input:")
pprint(person_data_input, expand_all=True)
print()

pprint("person_data_output:")
pprint(person_data_output, expand_all=True)
print()


