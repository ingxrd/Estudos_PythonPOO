class Carro:
    def __init__(self, ligado=False, cor="Preto", modelo="BMW i4", velocidade=0):
        self.ligado = ligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade

    def liga(self):
        self.ligado = True
        print("Carro ligado.")

    def desliga(self):
        self.ligado = False
        self.velocidade = 0
        print("Carro desligado.")

    def acelera(self, aumento=10):
        if self.ligado:
            self.velocidade += aumento
            print(f"Velocidade aumentada para {self.velocidade} km/h.")
        else:
            print("O carro precisa estar ligado para acelerar.")

    def desacelera(self, desacelera=10):
        if self.ligado:
            if self.velocidade > 0:
                self.velocidade -= desacelera
                if self.velocidade < 0:
                    self.velocidade = 0
                print(f"Velocidade diminuída para {self.velocidade} km/h.")
            else:
                print("Velocidade já está em 0 km/h.")
        else:
            print("O carro precisa estar ligado para desacelerar.")

    def mostrar_informacoes(self):
        estado = "ligado" if self.ligado else "desligado"
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")
        print(f"Estado: {estado}")

# Instância de carro
meuCarro = Carro(True, "Azul", "Fusca", 30)

# Carro andar utilizando método
meuCarro.mostrar_informacoes()
meuCarro.acelera(40)
meuCarro.acelera(30)
meuCarro.desacelera(10)

# Carro parar utilizando método
meuCarro.mostrar_informacoes()
meuCarro.desliga()
