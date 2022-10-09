class DFA:
    def __init__(self, states, transitonTable, acceptTable, sigma):
        self.states = states
        self.transitionTable = transitonTable
        self.acceptTable = acceptTable
        self.sigma = sigma

    def process(self, inputD):
        try:
            state = 0
            for c in inputD:
                state = self.transitionTable[state][self.sigma.index(c)]
            return self.acceptTable[state];
        except:
            return False

    @classmethod
    def inputDataFormKB(cls):
        n, m = map(int, input().split()) # [5, 2]
        states = list(map(int, input().split())) 
        # [q0, q1, q2, q3, q4]
        sigma = input().split() # [a, b]

        acceptingStates = list(map(int, input().split())) # [2, 4]
        acceptTable = [False for i in range(n)]  
        #[false, false, false, false, false]
        for apt in acceptingStates:
            acceptTable[apt] = True
        #[false, false, true, false, true]
        transitionTable = [[0 for i in range(m)] for j in range(n)]
        #[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        for i in range(n*m):
            start, inpData, des =input().split()
            #0 a 1
            start = int(start)
            des = int(des)
            transitionTable[start][sigma.index(inpData)] = des

        return cls(states, transitionTable, acceptTable, sigma)

dfa = DFA.inputDataFormKB()
inputData = input()

if dfa.process(inputData):
    print("YES")
else:
    print("NO")