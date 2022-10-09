class NFA:
    def __init__(self, sigma, states, NFATable, acceptTable):
        self.sigma = sigma
        self.states = states
        self.NFATable = NFATable
        self.acceptTable = acceptTable

    def toDFA(self):
        DFAStates = []
        DFATable = [[[] for x in range(len(self.sigma))] for x in range(2 ** len(self.states) + 1)]
        DFAStack = [[self.states[0]]]
        # [[q0]]
        idx = 0
        while DFAStack:
            state = DFAStack.pop(0) # [q0]
            DFAStates.append(state) # [[q0]]
            for s in state:
                if s in self.states:
                    for c in range(len(self.sigma)):
                        DFATable[idx][c].extend([x for x in self.NFATable[self.states.index(s)]
                        [c] if x not in DFATable[idx][c]])
                        DFATable[idx][c].sort(key = lambda x: self.states.index(x)) #[]
            DFAStack.extend([x for x in DFATable[idx] if x not in DFAStates]) #[[q1,q2], []]
            idx += 1
        print("==DFA table==")
        for i in range(idx):
            print(DFAStates[i], ": ", DFATable[i])



    @classmethod
    def inputFromKB(cls):
        try:
            states = [x for x  in input().split()] #[q0, q1, q2]
            sigma = [x for x  in input().split()] #[0, 1]

            # print(len(states), len(sigma))

            acceptingStates = list(input().split()) #[q2]
            acceptTable = [False for i in range(len(states))] #[false, false, false]
            for a in acceptingStates:
                acceptTable[states.index(a)] = True #[false, false, true]

            n = int(input()) #5
            NFATable = [[[] for x in range(len(sigma))] for x in range(len(states))]
            # [       0  1
                # 0 [[q1, q2],[]], 
                # 1 [[q1,q2],[q1]], 
                # 2 [[],[]] 
            # ]
            # [ [[],[]] ] -> [ { 0: [0,0] } ]
            for i in range(n):
                start, transition, end = input().split()
                NFATable[states.index(start)][sigma.index(transition)].append(end)

            return cls(sigma, states, NFATable, acceptTable)

        except:
            print("==Du lieu sai!==")
            return cls([], [], [], [])

def main():
    NFA1 = NFA.inputFromKB()
    print("==NFA table==")
    for t in NFA1.NFATable:
        print(t)
    NFA1.toDFA()
    

if __name__ == "__main__":
    main()