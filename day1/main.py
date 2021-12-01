from typing import List

def getPuzzleCode() -> List[str]:
    f = open("puzzelcode.txt")
    data = f.readlines()
    f.close()
    return data

def convertStringsToInts(listStrings: List[str]) -> List[int]:
    return list(map(lambda x: int(x), listStrings))

#Part 1
def countIncreases(listInts: List[int]) -> int:
    count = 0
    for index, element in enumerate(listInts[:-1]):
        if listInts[index + 1] > element:
            count += 1
    return count

# Part 2
def countIncreaseWindows(listInts: List[int]) -> int:
    count = 0
    for index, element in enumerate(listInts[:-3]):
        firstWindow = element + listInts[index + 1] + listInts[index + 2]
        secondWindow = listInts[index + 1] + listInts[index + 2] + listInts[index + 3]
        if secondWindow > firstWindow:
            count += 1
    return count

if __name__ == "__main__":
    puzzleCodeStrings = getPuzzleCode()
    puzzleCode = convertStringsToInts(puzzleCodeStrings)

    #Part 1
    print(countIncreases(puzzleCode))

    # Part 2
    print(countIncreaseWindows(puzzleCode))