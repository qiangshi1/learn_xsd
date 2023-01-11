#!/usr/bin/python3

import xmlschema
from pprint import pprint

xml_file="test14.xml"

schema_file_1 = open('test14_1.xsd')
my_schema = xmlschema.XMLSchema(schema_file_1, build=False)
my_schema.build()
print("XSD file is: [\033[1;35m"+'test14_1.xsd'+"\033[0m]. XML file is: [\033[1;35m"+xml_file+"\033[0m].")
ret_1=my_schema.validate(xml_file)
if ret_1 is None: 
  print("\033[1;32mcorrect\033[0m")
else:
  print("\033[1;31merror\033[0m") # 如果validate失败，它会抛异常，所以事实上不会执行这行代码

schema_file_2 = open('test14_2.xsd')
my_schema = xmlschema.XMLSchema(schema_file_2, build=False)
my_schema.build()
print("XSD file is: [\033[1;35m"+'test14_2.xsd'+"\033[0m]. XML file is: [\033[1;35m"+xml_file+"\033[0m].")
ret_1=my_schema.validate(xml_file)
if ret_1 is None: 
  print("\033[1;32mcorrect\033[0m")
else:
  print("\033[1;31merror\033[0m") # 如果validate失败，它会抛异常，所以事实上不会执行这行代码

schema_file_3 = open('test14_3.xsd')
my_schema = xmlschema.XMLSchema(schema_file_3, build=False)
my_schema.build()
print("XSD file is: [\033[1;35m"+'test14_3.xsd'+"\033[0m]. XML file is: [\033[1;35m"+xml_file+"\033[0m].")
ret_1=my_schema.validate(xml_file)
if ret_1 is None: 
  print("\033[1;32mcorrect\033[0m")
else:
  print("\033[1;31merror\033[0m") # 如果validate失败，它会抛异常，所以事实上不会执行这行代码

  