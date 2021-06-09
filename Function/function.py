import os

os.system('cls')


def main():
    first = open("FirstFile.txt", "r")
    second = open("SecondFile.txt", "r")
    firstRead = first.read()
    SecondRead = second.read()

    writingPart(firstRead, SecondRead)


def writingPart(firstRead, SecondRead):
    firstWrite = open("FirstFile.txt", "w")
    SecondWrite = open("SecondFile.txt", "w")
    firstWrite.write(SecondRead)
    SecondWrite.write(firstRead)


main()
