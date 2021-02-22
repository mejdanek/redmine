from json import load
import sys

def loadjson():
    try:
        config = load(open('config.json'))
        return config
    except:
        print("Configuration not loaded!")
        sys.exit(1)

if __name__ == "__main__":
    print("Not directly executable")