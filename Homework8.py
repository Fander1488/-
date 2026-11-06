class Osoba:

  def __init__(self, imya, vik):
    self.imya = imya
    self.vik = vik

  def inf_osoba(self):
    return f"Ім'я: {self.imya}, Вік: {self.vik} років"


class Vodiy(Osoba):

  def __init__(self, imya, vik, nomer_posvidchennya):
    super().__init__(imya, vik)
    self.nomer_posvidchennya = nomer_posvidchennya

  def inf_vodiy(self):
    return (
        f"Водій {self.imya}, вік {self.vik}, номер посвідчення:"
        f" {self.nomer_posvidchennya}"
    )


driver = Vodiy("Олександр", 39, "AB125462343456")
print(driver.inf_osoba())
print(driver.inf_vodiy())