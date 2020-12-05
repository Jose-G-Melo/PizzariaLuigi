class Estoque:
  def __init__(self):
    self.quantidade = 0
    self.produto = None

  def atualizarEstoque(self):
    self.produto = input("Produto: ")
    self.quantidade = int(input("Quantidade: "))