class UserName(object):

  def newMember(self, existingNames, newName):
    if self.isNameTaken(existingNames, newName):
      return self.suggestNameFor(existingNames, newName) 
    else:
      return newName 


  def suggestNameFor(self, existingNames, newName):
    variant       = 1  # an incremental key appended to the userName to make
                       # it userName unique 
    suggestedName = newName + str(variant)

    while self.isNameTaken(existingNames, suggestedName):
      variant += 1
      suggestedName = newName + str(variant)

    return suggestedName


  def isNameTaken(self, existingNames, suggestedName):
    return (suggestedName in existingNames)

