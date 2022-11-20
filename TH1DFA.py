
class DFA:
  def __init__(self, states, transitionTable, acceptTable, sigma):
    self.states = states
    self.transitionTable = transitionTable
    self.acceptTable = acceptTable
    self.sigma = sigma

  @classmethod
  def inputFromData(cls):
    n, m = map(int, input().split())
    states = map(int, input().split())
    sigma = input().split()
    endState = input().split()

    

    return cls(states, transitionTable, acceptTable, sigma)