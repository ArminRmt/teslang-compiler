import re

next_temp_reg = 0
next_label = 0
next_temp_reg2 = 0


class CodeGenerator:
    def __init__(self):
        self.registers = ["r1", "r2", "r3", "r4", "r5"]
        # self.next_temp_reg = 0
        self.labels = ["L1", "L2", "L3", "L4", "L5"]
        # self.labels = {}
        self.code = []

    def get_temp_reg(self):
        global next_temp_reg
        if next_temp_reg >= len(self.registers):
            # If we run out of registers, use the stack to store values
            next_temp_reg = 0
            reg = self.registers[next_temp_reg]
            next_temp_reg += 1
            next_temp_reg2 = next_temp_reg
            return reg

        else:
            reg = self.registers[next_temp_reg]
            next_temp_reg += 1
            next_temp_reg2 = next_temp_reg
            return reg

    def get_args_regs(self):
        global next_temp_reg2
        reg = self.registers[next_temp_reg2]
        next_temp_reg2 += 1
        # next_temp_reg2 -= 1
        return reg

    def get_ret_reg(self):
        return "r0"

    def get_label(self):
        global next_label
        reg = self.labels[next_label]
        next_label += 1
        return reg

    def add_code(self, code):
        file = open("IRtest.txt", "a")
        file.write(code)

    def add_code2(self, code):
        self.code.insert(0, code)

    def printresult(self):
        print(self.code)

    def __str__(self):
        return "".join(self.code)
