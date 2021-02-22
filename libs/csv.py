def readconvert_file(filepath):
    elements = []
    try:
        # open list file
        file = open(filepath, "r")
        # read every line
        for line in file:
            project, device, version = line.strip("\n").split(";")
            elements.append((project, device, version))
        # return as a dictionary
        return elements
    except FileNotFoundError:
        print("Path to file not found!")
        return None

if __name__ == "__main__":
    print("Not directly executable")