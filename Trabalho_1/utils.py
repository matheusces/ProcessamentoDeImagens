import os;

INPUT_DIR = "Trabalho_1/input"
OUTPUT_DIR = "Trabalho_1/output"

def in_file(filename):
    return os.path.join(INPUT_DIR, filename)


def out_file(filename):
    return os.path.join(OUTPUT_DIR, filename)