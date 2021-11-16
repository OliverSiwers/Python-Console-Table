def getSpaces(num):
  return " "*num

def appendSpaces(base, targetLength):
  return str(base) + getSpaces(targetLength - len(str(base)))

class Table:
  spacing = []
  def __init__(self, spacing):
    self.spacing = spacing

  def printRow(self, items):
    for index, item in enumerate(items):
      print(f"{appendSpaces(item, self.spacing[index])}", end="")
    print()

#Exmaple:
table = Table([15, 12, 5, 5, 5]);
table.printRow(["Test", "val", "x", "y", "z"]);
table.printRow(["Column 1", "a value", 6, 3.6, "zzzz"]);