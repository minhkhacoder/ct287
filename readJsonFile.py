import json
from re import T

def readDataFromJsonFile(fileName):
    f = open(fileName)
    data = json.load(f)
    return data

def printData(data):
    print(*data['Q'])
    print(*data['sigma'])
    print(data['q0'])
    print(*data['f'])
    for start, end in data['delta'].items():
        for transition, des in end.items():
            print(f"{start}->{transition}", end = ': ')
            print(*des)

def main():
    fileName = str(input())
    data = readDataFromJsonFile(fileName)
    printData(data)

if __name__ == "__main__":
    main()