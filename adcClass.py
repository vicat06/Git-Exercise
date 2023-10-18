import re


class Adc:
    def __init__(self) -> None:
        self.analogVolt = 2.3



    def toDigital(self):
        # returns digital number according to analog value

        decimalDigitalNum = (2**10 - 1) / 5 * self.analogVolt       # calculate digital number in decimal
        decimalDigitalNum = int(round(decimalDigitalNum))           # round digital number to int
        digitalNum = bin(decimalDigitalNum)                         # convert digital number to binary
        digitalNum = int(digitalNum[2:])                            # get only the binary value
        return digitalNum


    def setDigitalValue(self, digitalNum):
        # sets analog value according to digital number

        digitalNum = str(digitalNum)
        if not self.isBinaryNumCorrect(digitalNum):
            return
        
        decimalDigitalNum = int(digitalNum, 2)
        analogVolt = decimalDigitalNum / (2**10 - 1) * 5
        self.analogVolt = analogVolt

    def isBinaryNumCorrect(self, binaryNum):
        if len(binaryNum) > 10 or re.search(r'[^01]', binaryNum):
            return False
        return True
