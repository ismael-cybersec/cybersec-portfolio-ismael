with open("log.txt") as f:
    for line in f:
        if "Failed" in line:
            print(line)