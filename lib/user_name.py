class UserName(object):

  def __init__(self, existingNames):
    self.existingNames = existingNames


  def newMember(self, newName):
    if self.isNameTaken(newName):
      suggestedName = self.suggestName(newName)

      return suggestedName
    else:
      return newName 


  def suggestName(self, oldName):
    variant       = 1  # an incremental key added to the userName to make
                       # userName unique 
    suggestedName = oldName + str(variant)

    while self.isNameTaken(suggestedName):
      variant += 1
      suggestedName = oldName + str(variant)

    return suggestedName


  def isNameTaken(self, givenName):
    return (givenName in self.existingNames)

