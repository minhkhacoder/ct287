class NFA:
  def __init__(self, states, sigma, acceptTable, NFATable):
    self.states = states
    self.sigma = sigma
    self.acceptTable = acceptTable
    self.NFATable = NFATable

  def convertToDFA(self):
    NFATable = {}
    DFAStates = []
    Dict = {}
    for i in range(2 ** len(self.states) + 1):
      for j in range(len(self.sigma)):
        Dict[j] = []
      NFATable[i] = Dict
    StackDFA = [[self.states[0]]] #[[q0]]
    idx = 0
    while StackDFA:
      state = StackDFA.pop(0) # [q0]
      DFAStates.append(state) # [[q0]]
      for i in state:
          if i in self.states:
            for c in range(len(self.sigma)):
  @classmethod
  def inputForm(cls):
    states = list(map(int, input().split())) #[q0, q1, q2]
    sigma = input().split() #[0, 1]
    endStates = list(map(int, input().split())) #[q2]
    acceptTable = [False for i in range(len(states))] # [False, False, False]
    for end in endStates:
      acceptTable[end] = True
    # [False, False, True]
    n = int(input()) #5

    NFATable = {}
    Dict = {}
    for i in range(len(states)):
      for j in range(len(sigma)):
        Dict[j] = []
      NFATable[i] = Dict
    
    for i in range(n):
      start, transition, end = input().split()
      NFATable[states.index(start)][sigma.index(transition)].append(end)

    return cls(sigma, states, NFATable, acceptTable)