import numpy as np

class LogicGate:
    def __init__(self):
        self.w1 = None
        self.w2 = None
        self.th = None
        self.out = None
        self.x1 = self.x2 = None

    def or_gate(self, x1, x2):
        self.w1 = 0.5
        self.w2 = 0.5
        self.th = 0.0

        self.x1 = x1
        self.x2 = x2

        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])

        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0

    def and_gate(self, x1, x2):
        self.w1 = 0.5
        self.w2 = 0.5
        self.th = 0.99

        self.x1 = x1
        self.x2 = x2

        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])

        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0

    def nand_gate(self, x1, x2):
        self.w1 = -1
        self.w2 = -1
        self.th = -1.5

        self.x1 = x1
        self.x2 = x2

        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])
        z = np.dot(x, w)

        if z > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0

    def nor_gate(self, x1, x2):
        self.w1 = -1
        self.w2 = -1
        self.th = -0.5

        self.x1 = x1
        self.x2 = x2

        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])

        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0

    def xor_gate(self, x1, x2):
        c = self.or_gate(x1, x2)
        d = self.nand_gate(x1, x2)
        e = self.and_gate(c, d)

        self.x1 = x1
        self.x2 = x2

        if e == 1:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0
        
    def print_output(self, gate_name):
        if gate_name == "AND":
            print(f"AND Gate: {self.x1} AND {self.x2} = {self.out}")
        elif gate_name == "OR":
            print(f"OR Gate: {self.x1} OR {self.x2} = {self.out}")
        elif gate_name == "NAND":
            print(f"NAND Gate: {self.x1} NAND {self.x2} = {self.out}")
        elif gate_name == "NOR":
            print(f"NOR Gate: {self.x1} NOR {self.x2} = {self.out}")
        elif gate_name == "XOR":
            print(f"XOR Gate: {self.x1} XOR {self.x2} = {self.out}")