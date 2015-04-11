import pytest
from unittest import TestCase

from user_name import UserName


class TestUserName(TestCase):

  def testTygerTygerIsAvailable(self):
    existingNames = set(["MasterOfDisaster",
                         "DingBat",
                         "Orpheus",
                         "WolfMan",
                         "MrKnowItAll"])
    newName       = "TygerTyger"
    userName      = UserName(existingNames)

    suggestedName = userName.newMember(newName)

    self.assertEqual("TygerTyger", suggestedName)


  def testTygerTygerIsTaken(self):
    existingNames = set(["MasterOfDisaster",
                         "TygerTyger1",
                         "DingBat",
                         "Orpheus",
                         "TygerTyger",
                         "WolfMan",
                         "MrKnowItAll"])
    newName       = "TygerTyger"
    userName      = UserName(existingNames)

    suggestedName = userName.newMember(newName)

    self.assertEqual("TygerTyger2", suggestedName)


  def testTygerTygerWithLargeVariantButNoBase(self):
    existingNames = set(["TygerTyger2000",
                         "TygerTyger1",
                         "MasterDisaster",
                         "DingBat",
                         "Orpheus",
                         "WolfMan",
                         "MrKnowItAll"])
    newName       = "TygerTyger"
    userName      = UserName(existingNames)

    suggestedName = userName.newMember(newName)

    self.assertEqual("TygerTyger", suggestedName)


  def testCaseSensitiveUserNames(self):
    existingNames = set(["grokster2",
                         "BrownEyedBoy",
                         "Yoop",
                         "BlueEyedGirl",
                         "grokster",
                         "Elemental",
                         "NightShade",
                         "Grokster1"])
    newName       = "grokster"
    userName      = UserName(existingNames)

    suggestedName = userName.newMember(newName)

    self.assertEqual("grokster1", suggestedName)


  def testBartWithLargeVariant(self):
    existingNames = set(["Bart4",
                         "Bart5",
                         "Bart6",
                         "Bart7",
                         "Bart8",
                         "Bart9",
                         "Bart10",
                         "Lisa",
                         "Marge",
                         "Homer",
                         "Bart",
                         "Bart1",
                         "Bart2",
                         "Bart3",
                         "Bart11",
                         "Bart12"])
    newName      = "Bart"
    userName     = UserName(existingNames)

    suggestedName = userName.newMember(newName)

    self.assertEqual("Bart13", suggestedName)
