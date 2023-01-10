#!/usr/bin/python3

import xmlschema
from pprint import pprint

xml_file="test11.xml"

schema_file = open('test11.xsd')
my_schema = xmlschema.XMLSchema(schema_file, build=False)
_ = my_schema.include_schema('test11_children.xsd')
my_schema.build()

print("XSD file is: [\033[1;35m"+'test11.xsd'+' '+'test11_children.xsd'+"\033[0m]. XML file is: [\033[1;35m"+xml_file+"\033[0m].")

ret2=my_schema.validate(xml_file)
if ret2 is None: 
  print("\033[1;32mcorrect\033[0m")
else:
  print("\033[1;31mcorrect\033[0m") # 如果validate失败，它会抛异常，所以事实上不会执行这行代码
  