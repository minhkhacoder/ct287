import json

class NFA:
    def __init__(self, states, sigma, delta, start, endState):
        self.states = states
        self.sigma = sigma
        self.delta = delta
        self.start = start
        self.endState = endState
    @classmethod
    def inputDataForm(cls):
      fileName = input()
      f = open(fileName)
      data = json.load(f)
      f.close()
      return cls(data["Q"], data["sigma"], data["delta"], data["q0"], data["f"])

def main():
  nfa = NFA.inputDataForm()
  for i in nfa.states:
    print(i, end=" ")
  print()
  for i in nfa.sigma:
    print(i, end=" ")
  print()
  print(nfa.start)
  for i in nfa.endState:
    print(i, end=" ")
  print()
  for keyDelta, valueDelta in nfa.delta.items():
    for keyItem, valueItem in valueDelta.items():
      print(str(keyDelta) + " ->", end = " ")
      print(str(keyItem) + ":", end=" ")
      for i in valueItem:
        print(i, end=" ")
      print()
    


if __name__ == "__main__":
    main()