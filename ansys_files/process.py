import os
import traceback
from extractor.extractor import extractor

class process:
    def __init__(self, path: str, file: str):
        self.path = path
        self.file = file

    def process(self, new_path: str, new_file: str):
        extractor_instance = extractor(self.path, self.file)
        extractor_instance.process(new_path, new_file)

if __name__ == '__main__':
    try:
        current_directory = os.path.dirname(
            os.path.realpath(__file__)
        )

        print(f"Current directory: {current_directory}")

        process_instance = process(current_directory, "/NACA4412CFDdata.txt")
        new_path = current_directory + "/output/"

        if not os.path.exists(new_path):
            os.makedirs(new_path)

        process_instance.process(new_path, "NACA4412CFDdata.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()