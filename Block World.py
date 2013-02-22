'''
BLOCK WORLD
'''
from Exceptions import *

class block(object):
  '''block model'''
  def __init__(self, on=True):
    '''on refers to the object the block is on. None = Table'''
    self.clear = True
    self.on = on

  def getOn(self):
    '''returns the object it's on'''
    return self.on

  def getClear(self):
    '''returns whether it's clear or not'''
    return self.clear

class agent(object):
  '''artificial intelligence agent'''
  def __init__(self):
    self.empty = True

  def pickUp(self, x):
    '''picks up block x iff self.empty'''
    if not self.empty == True: raise NotEmptyException
    self.empty = x
  
  def drop(self):
    '''drops the block in hand'''
    if not self.empty: raise NoBlockInHandException
    self.empty = True

class blockWorld:
  '''World

  conditions:
    on(X, Y)
    onTable(X)
    clear(X)
    empty

  operations:
    pickup(X)
    put(X, Y)
    putOnTable(X)
  '''
  def __init__(self, blocks=None, agent=agent()):
    self.blocks = blocks
    self.agent = agent

  def isClear(self, X):
    '''returns true if X is clear and False if otherwise'''
    if X not in self.blocks: raise BlockNotFoundException
    return X.getClear()

  def addNewBlock(self, X):
    '''appends block to world'''
    if X in self.blocks: return X
    self.block.append(X)
    return X

  def newBlock(self, X=None):
    '''creates a new block in world'''

  def on(self, X, Y):
    '''moves X on Y'''
    if not Y in self.blocks:
      self.blocks.append(Y)
    if X not in self.blocks:
      self.blocks.append(X)

      if isClear(Y):




if __name__ == "__main__":
  block1 = block()
  block2 = block(block1)

