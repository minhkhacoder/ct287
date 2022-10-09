class DFA:
  def __init__(self, states, transitionTable, acceptTable, sigma ):
    self.states = states
    self.transitionTable = transitionTable
    self.acceptTable = acceptTable
    self.sigma = sigma
  
  # abbaaab
  def process(self, inputD):
    try:
        state = 0
        for c in inputD:
            state = self.transitionTable[state][self.sigma.index(c)]
        return self.acceptTable[state];
    except:
        return False

  @classmethod
  def inputDataForm(cls):
    n, m = map(int, input().split()) # [5, 2]
    states = list(map(int, input().split())) #[0, 1, 2, 3, 4]
    sigma = input().split() #[a, b]
    endStates = list(map(int, input().split())) #[2,4]
    acceptTable = [False for i in range(n)] # [False, False, False, False, False]
    for end in endStates:
      acceptTable[end] = True
    # [False, False, True, False, True]
    transitionTable = {}
    for i in range(n):
      transitionTable[i] = [0, 0]
    
    for i in range(n*m):
      start, inpData, des =input().split()
      # 0 a 1
      start = int(start) # 0
      des = int(des) # 1
      transitionTable[start][sigma.index(inpData)] = des

    return cls(states, transitionTable, acceptTable, sigma)

dfa = DFA.inputDataForm()
inputData = input()

if dfa.process(inputData):
    print("YES")
else:
    print("NO")