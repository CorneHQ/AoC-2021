from typing import Dict, List

def getPuzzleCode() -> List[str]:
    f = open("puzzelcode.txt")
    data = f.readlines()
    f.close()
    return data

def sortPuzzleCode(stringList: List[str]) -> List[Dict[str, int]]:
    sortedList = []
    for element in stringList:
        splittedElement = element.split(" ")
        sortedList.append({"direction": splittedElement[0], "amount": int(splittedElement[1])})
    return sortedList

def calculateDepth(list: List[Dict[str, int]]) -> int:
    depth = 0
    for element in list:
        if element["direction"] == "down":
            depth += element["amount"]
        elif element["direction"] == "up":
            depth -= element["amount"]
    return depth

def calculateHorizontal(list: List[Dict[str, int]]) -> int:
    return sum([element["amount"] for element in list if element["direction"] == "forward"])

if __name__ == '__main__':
    puzzleCodeString = getPuzzleCode()
    sortedPuzzleCode = sortPuzzleCode(puzzleCodeString)
    depth = calculateDepth(sortedPuzzleCode)
    horizontal = calculateHorizontal(sortedPuzzleCode)
    print(horizontal * depth)