import json

class NFA:
    def __init__(self, states, sigma, delta, start, endState):
        self.states = states
        self.sigma = sigma
        self.delta = delta
        self.start = start
        self.endState = endState

    def proccess(self,currentState, step, str):
        if step >= len(str):
            return currentState in self.endState
        else:
            if currentState not in self.delta.keys():
                return False
            if str[step] not in self.delta[currentState].keys():#ababababa
                return False
            return True in [self.proccess(x, step + 1, str) for x in self.delta[currentState][str[step]]]

        
    
    @classmethod
    def inputDataForm(cls):
        fileName = input()
        f = open(fileName)
        data = json.load(f)

        f.close()
        return cls(data["Q"], data["sigma"], data["delta"], data["q0"], data["f"])

def main():
    nfa = NFA.inputDataForm()
    # print(nfa.endState)
    n = int(input())
    for i in range(n):
        str = input() #ababababa
        if nfa.proccess(nfa.start, 0, str):
            print("YES")
        else:
            print("NO")
    


if __name__ == "__main__":
    main()