
class q1:
    def __init__(self):
        self.tp = None
        self.fp = None
        self.fn = None

    def input_data(self):
        self.tp = int(input("tp: "))
        self.fp = int(input("fp: "))
        self.fn = int(input("fn: "))

        if not isinstance(self.tp, int) or not isinstance(self.fp, int) or not isinstance(self.fn, int):
            print('tp, fp and fn must be int')
            return
        if self.tp <= 0 or self.fp <= 0 or self.fn <= 0:
            print('tp, fp and fn must be greater than zero')
            return

    def calculate(self):
        precision = self.tp / (self.tp + self.fp)
        recall = self.tp / (self.tp + self.fn)
        f1_score = 2 * precision * recall / (precision + recall)
        return precision, recall, f1_score

def main():
    model = q1()
    model.input_data()
    precision, recall, f1_score = model.calculate()
    print('precision:', precision)
    print('recall:', recall)
    print('f1 score:', f1_score)
if __name__ == "__main__":
    main()





