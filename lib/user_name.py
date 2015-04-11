class UserName(object):

  def __init__(self, existingNames):
    self.existingNames = existingNames


  def newMember(self, existingNames, newName):
    if self.isNameTaken(newName):
      return self.suggestNameFor(newName) 
    else:
      return newName 


  def suggestNameFor(self, newName):
    variant       = 1  # an incremental key appended to the userName to make
                       # userName unique 
    suggestedName = newName + str(variant)

    while self.isNameTaken(suggestedName):
      variant += 1
      suggestedName = newName + str(variant)

    return suggestedName


  def isNameTaken(self, givenName):
    return (givenName in self.existingNames)

