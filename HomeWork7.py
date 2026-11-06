class Tvarina:

  def __init__(self, nazva, vik):
    self.nazva = nazva
    self.vik = vik

  def zrobiti_zvuk(self, zvuk):
    return f"{self.nazva} видає звук: {zvuk}"


class Sobaka(Tvarina):

  def __init__(self, nazva, vik, poroda):
    super().__init__(nazva, vik)
    self.poroda = poroda

  def gavkat(self):
    return f"{self.nazva} гавкає: Гав-гав!"


class Kit(Tvarina):

  def __init__(self, nazva, vik, kolir):
    super().__init__(nazva, vik)
    self.kolir = kolir

  def myaukati(self):
    return f"{self.nazva} нявкає: Мяу-мяу!"


dog = Sobaka("Барбос", 3, "Німецька вівчарка")
cat = Kit("Мурчик", 2, "Рудий")

print(dog.zrobiti_zvuk("Гав"))
print(dog.gavkat())
print(cat.zrobiti_zvuk("Мяу"))
print(cat.myaukati())