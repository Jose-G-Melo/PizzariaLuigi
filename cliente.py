class Cliente:
  def __init__(self):
    self.endereco = None
    self.intoleranciaGluten = False
    self.intoleranciaLactose = False

  def efetuarPedido(self):
    print("Quero rola!")