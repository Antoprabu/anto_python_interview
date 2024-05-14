class FrequencyCalibiration():

    #Initialize variables
    def __init__(self):
        self.currentFrequency = 0

    """
    Read input files
    """
    def readFile(self,filePath):
        inputList = []
        try:
            with open(filePath, 'r') as inputfile:
                for line in inputfile:
                    inputList.append(int(line.strip()))
        except FileNotFoundError as ff:
            print("FILE NOT FOUND Error: {}".format(ff))
        return inputList

    """
    cf -  currency frequency
    fff - as Change of frequency
    rf - as result of frequency
    """
    def findFrequency(self, inputlist):
        cf = self.currentFrequency
        for fff in inputlist:
            rf = cf + fff
            cf = rf
        print("after applying all the frequncy the result frequncy is :{}".format(cf))
        return

    def callibirateFrequency(self, inputFile2):
        cf = self.currentFrequency

        lastseen = set()
        while True:
            for fff in inputFile2:
                rf = cf + fff
                print("Current frequency {}, change of {}; resulting frequency {}".format(cf, fff, rf))
                if rf in lastseen:
                    print("the first frequency reached twice is :{}".format(rf))
                    return rf
                else:
                    lastseen.add(rf)
                cf = rf
        return

if __name__ == "__main__":
    inputfilepath = "/Users/sofiaanto/PycharmProjects/anto_python_interview/input.txt"
    inputfilepath_2 = "/Users/sofiaanto/PycharmProjects/anto_python_interview/sample-input.txt"
    fc = FrequencyCalibiration()
    inputlist_1 = fc.readFile(inputfilepath)
    inputlist_2 = fc.readFile(inputfilepath_2)

    fc.findFrequency(inputlist_1)

    inputlist_2 = [+3, +3, +4, -2, -4]
    fc.callibirateFrequency(inputlist_1)


    print("inpufile list: {}".format(inputlist_1[:10]))
    print("inputfile list 2: {}".format(inputlist_2[:10]))





