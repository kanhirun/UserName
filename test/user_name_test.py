import pytest
from unittest import TestCase

from user_name import UserName


class TestUserName(TestCase):

  def testTygerTygerIsAvailable(self):
    userName      = UserName()
    existingNames = set(["MasterOfDisaster",
                         "DingBat",
                         "Orpheus",
                         "WolfMan",
                         "MrKnowItAll"])
    newName       = "TygerTyger"

    suggestedName = userName.newMember(existingNames, newName)

    self.assertEqual("TygerTyger", suggestedName)


  def testTygerTygerIsTaken(self):
    userName      = UserName()
    existingNames = set(["MasterOfDisaster",
                         "TygerTyger1",
                         "DingBat",
                         "Orpheus",
                         "TygerTyger",
                         "WolfMan",
                         "MrKnowItAll"])
    newName       = "TygerTyger"

    suggestedName = userName.newMember(existingNames, newName)

    self.assertEqual("TygerTyger2", suggestedName)


#  def testTygerTygerWithLargeVariantButNoBase(self):
#    userName      = UserName()
#    existingNames = set(["TygerTyger2000",
#                         "TygerTyger1",
#                         "MasterDisaster",
#                         "DingBat",
#                         "Orpheus",
#                         "WolfMan",
#                         "MrKnowItAll"])
#    newName       = "TygerTyger"
#
#    suggestedName = userName.newMember(existingNames, newName)
#
#    self.assertEqual("TygerTyger", suggestedName)
#
#
#  def testCaseSensitiveUserNames(self):
#
