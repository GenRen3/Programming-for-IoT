#!/usr/bin/env python3
import json
import numpy


class Calculator(object):

    def __init__(self):
        self.result = 0

    def add(self, number, elements, it):
        for it in range(number):
            self.result += elements[it]

    def sub(self, number, elements, it):
        for it in range(number):
            self.result += self.result-elements[it]

    def mul(self, number, elements, it):
        for it in range(number):
            self.result += self.result*elements[it]

    def div(self, number, elements, it):
        for it in range(number):
            if(ZeroDivisionError is True):
                pass
            else:
                self.result += self.result/elements[it]


a = Calculator()

while(1 == 1):

    it = 2
    string = input("Write your choice: \n")
    elements = string.split()
    number = int(len(elements))
    function = elements[0]

    for it in range(number):
        int(elements[it])
        print(elements[it])

    if(function == 'add'):
        a.add(number, elements, it)
    elif(function == 'sub'):
        a.sub(number, elements, it)
    elif(function == 'mul'):
        a.mul(number, elements, it)
    elif(function == 'div'):
        a.div(number, elements, it)
    else:
        break

    #dict = [{"Operand ": a.operand1, "Operand 2": a.operand2, "Result": a.result}]
    # print(json.dumps(dict))
    print("\n")
