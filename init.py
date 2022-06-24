import os
import pathlib

def init():
    os.makedirs('.ygit/objects')
    os.makedirs('.ygit/refs')
    pathlib.Path('.ygit/index').touch()

if __name__ == "__main__":
    init()
