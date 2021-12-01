from typing import List

def getPuzzleCode() -> List[str]:
    f = open("puzzelcode.txt")
    data = f.readlines()
    f.close()
    return data

def convertStringsToInts(listStrings: List[str]) -> List[int]:
    return list(map(lambda x: int(x), listStrings))

def countIncreases(listInts: List[int]) -> int:
    count = 0
    for index, element in enumerate(listInts[:-1]):
        if listInts[index + 1] > element:
            count += 1
    return count

if __name__ == "__main__":
    puzzleCodeStrings = getPuzzleCode()
    puzzleCode = convertStringsToInts(puzzleCodeStrings)
    print(countIncreases(puzzleCode))