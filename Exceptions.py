class NotEmptyException(Exception):
  def __str__(self):
    "Agent not empty"

class NoBlockInHandException(Exception):
  def __str__(self):
    "Agent empty"

class BlockNotFoundException(Exception):
  def __str__(self):
    "Block not found in world"

