from typing import List


def getPuzzleCode() -> List[str]:
    f = open("puzzelcode.txt")
    data = f.readlines()
    f.close()
    return data

def createIntList(strList: List[str]) -> List[List[int]]:
    newList = []
    for element in strList:
        newList.append(list(map(lambda x: int(x), element.strip())))
    return newList

def calculateGamma(binaryList: List[List[int]]) -> int:
    gammaBinary = ""
    for i in range(len(binaryList[0])):
        countZero = 0
        countOne = 0
        for element in binaryList:
            if element[i] == 0:
                countZero += 1
            else:
                countOne += 1
        gammaBinary += "1" if countOne > countZero else "0"
    return binaryToInt(gammaBinary)

def calculateEpsilon(binaryList: List[List[int]]) -> int:
    epsilonBinary = ""
    for i in range(len(binaryList[0])):
        countZero = 0
        countOne = 0
        for element in binaryList:
            if element[i] == 0:
                countZero += 1
            else:
                countOne += 1
        epsilonBinary += "1" if countOne < countZero else "0"
    return binaryToInt(epsilonBinary)

def binaryToInt(binary: str) -> int:
    return int(binary, 2)

if __name__ == "__main__":
    puzzleCode = getPuzzleCode()
    binaryList = createIntList(puzzleCode)
    gamma = calculateGamma(binaryList)
    epsilon = calculateEpsilon(binaryList)
    print(gamma * epsilon)