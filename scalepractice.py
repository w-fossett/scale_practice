from random import seed, randint
import re

def main():
    seed(a = None)

    qualities = []
    toPractice = []

    getScales(qualities)
    assembleScales(qualities, toPractice)
    displayScales(toPractice)

def getScales(practiceList):
    print("\nEnter scales (default: major and minor)\n\nEnter 'done' when finished.\nRemove scale: 'rm scalename'\nView current scales: 'ls'\n\n")

    scale = input()
    removePattern = re.compile(r'^rm ') # Handles the 'rm' command

    while scale != 'done':
        if scale == 'ls':
            for x in range(len(practiceList)):
                print(practiceList[x], end="")
                if x != len(practiceList) - 1:
                    print(", ", end="")
                else:
                    print()
        elif removePattern.match(scale):
            commands = scale.split(" ", 1)
            if commands[1] in practiceList:
                practiceList.remove(commands[1])
            else:
                print(f"Error: No item named '{commands[1]}'.")
        elif scale != "":
            practiceList.append(scale)
        scale = input()
    if len(practiceList) == 0: # Default case
        practiceList.append("Major")
        practiceList.append("Minor")

def assembleScales(qualities, output):
    roots = ["A", "Bb / A#", "B", "C", "C# / Db", "D", "Eb / D#", "E", "F", "F# / Gb", "G", "Ab / G#"]

    for i in range(len(qualities)):
        for j in range(len(roots)):
            output.append(f"{roots[j]} {qualities[i]}")

def displayScales(scales):
    scalesPlayed = 0
    scaleTotal = len(scales)
    print() # Separate scale entry from scale display

    while scalesPlayed < scaleTotal:
        currentScale = scales[randint(0, len(scales) - 1)]
        print(currentScale)
        scales.remove(currentScale)
        buffer = "-" * max((len(currentScale) - 6), 1) # 6 is an approximation for the length of the progres display

        command = input(f"[{scalesPlayed + 1}/{scaleTotal}] {buffer} Press 'enter' to continue or enter 's' to stop.\n")
        while command not in ['s', '']:
            command = input(f"[{scalesPlayed + 1}/{scaleTotal}] {buffer} Press 'enter' to continue or enter 's' to stop.\n")
        if command == 's':
            break
        
        scalesPlayed += 1

main()
