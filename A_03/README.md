# ece-55831-2026-assignments
# A_03

Author: Errick Lisk
Class: ECE 55831
Date - 10/06/2026

This folder contains the files required for the 3rd assignment in ECE 55831.

### logic_gate.py
Contains 7 functions, one init function, 5 which use numpy to create logic gates for the AND, OR, NAND, NOR, XOR and 1 to print the output of a gate
* __init__(self)
* or_gate(self, x1, x2)
* and_gate(self, x1, x2)
* nand_gate(self, x1, x2)
* nor_gate(self, x1, x2)
* xor_gate(self, x1, x2)
* print_output(self, gate_name)

### module3.py
Contains 5 functions to test the outputs of the logic gates in logic_gate.py with each input: [0,0], [0,1], [1,0], [1,1]
* and_gate_table
* or_gate_table
* nand_gate_table
* nor_gate_table
* xor_gate_table

### module3.ipynb
Jupyter notebook which invokes module3.py to show the output of each logic gate and show the logic tables.