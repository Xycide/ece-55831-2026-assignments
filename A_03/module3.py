from logic_gate import LogicGate

lg = LogicGate()


# AND Gate
def and_gate_table():
    lg.and_gate(1, 1)
    lg.print_output("AND")

    lg.and_gate(1, 0)
    lg.print_output("AND")

    lg.and_gate(0, 1)
    lg.print_output("AND")

    lg.and_gate(0, 0)
    lg.print_output("AND")

# OR Gate
def or_gate_table():
    lg.or_gate(1, 1)
    lg.print_output("OR")

    lg.or_gate(1, 0)
    lg.print_output("OR")

    lg.or_gate(0, 1)
    lg.print_output("OR")

    lg.or_gate(0, 0)
    lg.print_output("OR")

# NAND Gate
def nand_gate_table():
    lg.nand_gate(1, 1)
    lg.print_output("NAND")

    lg.nand_gate(1, 0)
    lg.print_output("NAND")

    lg.nand_gate(0, 1)
    lg.print_output("NAND")

    lg.nand_gate(0, 0)
    lg.print_output("NAND")

# NOR Gate
def nor_gate_table():
    lg.nor_gate(1, 1)
    lg.print_output("NOR")

    lg.nor_gate(1, 0)
    lg.print_output("NOR")

    lg.nor_gate(0, 1)
    lg.print_output("NOR")

    lg.nor_gate(0, 0)
    lg.print_output("NOR")

# XOR Gate
def xor_gate_table():
    lg.xor_gate(1, 1)
    lg.print_output("XOR")

    lg.xor_gate(1, 0)
    lg.print_output("XOR")

    lg.xor_gate(0, 1)
    lg.print_output("XOR")

    lg.xor_gate(0, 0)
    lg.print_output("XOR")
