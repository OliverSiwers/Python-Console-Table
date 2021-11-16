def getSpaces(num):
  return " "*num

def appendSpaces(base, targetLength):
  return str(base) + getSpaces(targetLength - len(str(base)))

class Table:
  spacing = []
  allowOverflow = False
  def __init__(self, spacing, allowOverflow = False):
    self.spacing = spacing
    self.allowOverflow = False

  def printRow(self, items):
    for index, item in enumerate(items):
      toPrint = appendSpaces(item, self.spacing[index])
      if(not self.allowOverflow):
        toPrint = toPrint[0:self.spacing[index]]
      print(f"{toPrint}", end=" ")
    print()

#Exmaple:
table = Table([15, 12, 5, 5, 5]);
table.printRow(["Test", "val", "x", "y", "z"]);
table.printRow(["Column 1", "a value", 6, 3.601, "z1z1"]);
table.printRow(["Clmn 2", "another value", "06", 3.6, "z"]);
table.printRow(["Col 3", "yet another value", 7.3333, 3, "zZz"]);