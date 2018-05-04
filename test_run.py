#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

code_dir = './disa_func/export_asm.py'
data_dir = 'E:/Works/Data/paper2'
file_dir = 'calc.exe'
command = 'idaw -c -A -S'
# shell_command = command+ '\"' + code_dir+'\" \"'+data_dir + + '\" ' + '> NUL'
shell_command = command + '"' + code_dir + '" "' +data_dir + '/' + file_dir +'"'

print(shell_command)

e = os.system(shell_command)

if not e == 0:
  print ('Error. code:', e)




# Run it with idal -c -A -S./script.py ./test.bin
# idaw -c -A -S"E:\Project\PycharmProjects\function_disassemble\disa_func/export_asm.py" "E:\Works\Data\paper2\calc.exe" > NUL