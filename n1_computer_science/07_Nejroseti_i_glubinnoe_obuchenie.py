import os


class Neuron:
    def __init__(self, ch="a", n: int = 10, m: int = 10, threshold: int = 35):
        self.ch = ch
        self.threshold = threshold
        self.height_list = [[0]*n for _ in range(m)]

    def func(self):
        samples_folder = "06_files"
        files = os.listdir(samples_folder)

        for i in range(100):
            for filename in files:
                (ch, is_correct, _) = filename.split("_", 2)
                is_correct = True if is_correct == '1' else False
                (is_recognized, inp) = self.recognize(f"{samples_folder}/{filename}")

                if (ch == self.ch and is_correct) and is_recognized:
                    continue
                elif ch != self.ch and not is_recognized:
                    continue
                elif ch != self.ch and is_recognized:
                    self.correlate(inp, "down")
                elif ch == self.ch and is_correct and not is_recognized:
                    self.correlate(inp, "up")

    def correlate(self, inp, move: str):
        for i in range(len(self.height_list)):
            for j in range(len(self.height_list[i])):
                if move == "down":
                    self.height_list[i][j] = self.height_list[i][j] - inp[i][j]
                if move == "up":
                    self.height_list[i][j] = self.height_list[i][j] + inp[i][j]

    def recognize(self, filename: str):
        summary = 0
        inp = []

        with open(filename, "r") as txt_file:
            lines = txt_file.readlines()
            count = 0
            for i, line in enumerate(lines):
                count += 1
                inp_line = []
                for j, c in enumerate(line.strip()):
                    summary += int(c) * self.height_list[i][j]
                    inp_line.append(int(c))
                inp.append(inp_line)

        if summary >= self.threshold:
            return True, inp

        return False, inp

    def pprint(self):
        for i in self.height_list:
            print(i)


if __name__ == "__main__":
    neuron = Neuron('a', 10, 10, 66)
    neuron.func()
    neuron.pprint()

