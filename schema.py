#!/usr/bin/python3

# 用xsd校验xml脚本
# 用法: ./schema.py --prefix=test
# 表示用test.xsd校验test.xml
# 前提: 安装xmlschema: python -m pip install xmlschema
# python版本：3.8

import xmlschema
import sys, getopt
from pprint import pprint

def version():
  print("version: 1.0.1")
  sys.exit(1)

def usage():
  print("help")
  sys.exit(1)

opts, args = getopt.getopt(sys.argv[1:], '',["xsd=", "xml=", "prefix=", "version", "help"])

xsd_file=""
xml_file=""
for opt, arg in opts:
  if opt in ["--xsd"]:
    xsd_file = arg
  elif opt in ["--xml"]:
    xml_file = arg
  elif opt in ["--prefix"]:
    xml_file = arg+'.xml'
    xsd_file = arg+'.xsd'
  elif opt in ["--version"]:
    version()
  elif opt in ["--help"]:
    usage()

print("XSD file is: [\033[1;35m"+xsd_file+"\033[0m]. XML file is: [\033[1;35m"+xml_file+"\033[0m].")

my_schema=xmlschema.XMLSchema(xsd_file)
# ret=my_schema.is_valid('note.xml')
# print(ret)
ret2=my_schema.validate(xml_file)
if ret2 is None: 
  print("\033[1;32mcorrect\033[0m")
else:
  print("\033[1;31mcorrect\033[0m") # 如果validate失败，它会抛异常，所以事实上不会执行这行代码
# xs=xmlschema.XMLSchema('note.xsd')
# pprint(xs.to_dict('note.xml'))