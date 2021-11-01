import os


class Neuron:
    def __init__(self, n: int = 10, m: int = 10, threshold: int = 35):
        self.threshold = threshold
        self.height_list = [[0] * n] * m

    def func(self, filename: str):
        (ch, correct, _) = filename.split("/", 1)[1].split("_", 2)
        summary = 0

        with open(filename, "r") as txt_file:
            lines = txt_file.readlines()
            count = 0
            for i, line in enumerate(lines):
                count += 1
                for j, c in enumerate(line.strip()):
                    summary += int(c) * self.height_list[i][j]

        if summary >= self.threshold:
            return True

        return False


if __name__ == "__main__":
    neuron = Neuron(10, 10, 35)

    samples_folder = "06_files"
    files = os.listdir(samples_folder)
    for file in files:
        print(neuron.func(f"{samples_folder}/{file}"))

