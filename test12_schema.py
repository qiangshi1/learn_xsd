#!/usr/bin/python3
# 暂未测试通过，先忽略吧
import xmlschema
from pprint import pprint

xml_file="test12.xml"

schema_file = open('test12.xsd')
my_schema = xmlschema.XMLSchema(schema_file, build=False)
# _ = my_schema.include_schema('test12_gender.xsd')
my_schema.build()

print("XSD file is: [\033[1;35m"+'test12.xsd'+' '+'test12_gender.xsd'+"\033[0m]. XML file is: [\033[1;35m"+xml_file+"\033[0m].")

ret2=my_schema.validate(xml_file)
if ret2 is None: 
  print("\033[1;32mcorrect\033[0m")
else:
  print("\033[1;31mcorrect\033[0m") # 如果validate失败，它会抛异常，所以事实上不会执行这行代码

  