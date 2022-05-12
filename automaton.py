class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        self.words = []
        self.transitions = []
        self.states = []

    def validate(self):
        okf = 0
        oks = 0
        for s in self.states:
            if s[-1] == 'F':
                okf = 1
            if s[-1] == 'S':
                oks = 1

        if oks == 1 and okf == 1:
            return True
        return False

    def accepts_input(self):
        t = []
        t1 = []
        for tr in self.transitions:
            c = tr.strip().split(", ")
            t.append(c)

        print(self.states)
        print(self.words)
        print(t)
        for tr in t:
            if tr[0] not in self.states or tr[1][:-1] not in self.words or tr[2] not in self.states:
                return False
        return True
    def read_input(self, nume_fisier):
        lines = []
        with open(nume_fisier) as f:
            lines = f.readlines()
        lines1 = []
        for l in lines[:-1]:
            lines1.append(l[:-1])
        lines1.append(lines[-1])
        cuvinte = False
        stari = False
        tranzitii = False
        for line in lines1:
            if line[0] == '#':
                continue
            else:
                if line == "Sigma :":
                    cuvinte = True
                    continue
                elif line == "States :":
                    stari = True
                    continue
                elif line == "Transitions :":
                    tranzitii = True
                    continue
                if cuvinte == True :
                    if line == "End":
                        cuvinte = False
                        continue
                    self.words.append(line.strip())
                elif stari == True:
                    if line == "End":
                         stari = False
                         continue
                    self.states.append(line.strip())
                elif tranzitii == True:
                    if line == "End":
                        tranzitii = False
                        continue
                    self.transitions.append(line.strip())


if __name__ == "__main__":
    a = Automaton('input.txt')
    a.read_input('input.txt')

    if a.validate() == True:
        if a.accepts_input() == True:
            print("The following input is correct!")
        else:
            print("The following input is not correct!")
    else:
        print("The input is not validated!")
