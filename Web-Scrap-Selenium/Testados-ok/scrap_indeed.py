#!/usr/bin/env python
#
from checar_parametros import checar_input
import sys
import os
n = len(sys.argv) -1
checar_input(n)
#
script = sys.argv[0]
cargo  = sys.argv[1]
# Chamar o script executável
print ("Executando script:", script)
print ("Cargo:", cargo)
#
#python Estudo-indeed-br4.py
os.system('python Estudo-indeed-br4.py ' + cargo )

