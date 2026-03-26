import random
from abc import ABC, abstractmethod

# ---------------------------------
# CLASSE ABSTRATA
# mantem o uso de abstração 
# ---------------------------------
class GameBase(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def jogar(self):
        pass


# ---------------------------------
# CLASSE PLAYER (NOVA)
# existe um jogador com estado proprio
# ---------------------------------
class Player:
    def __init__(self, nome):
        self.__nome = nome          # encapsulamento
        self.__pontos = 0           # sistema de pontuação (não tinha)

    def get_nome(self):
        return self.__nome

    def get_pontos(self):
        return self.__pontos

    def adicionar_pontos(self, valor):
        # logica de recompensa
        self.__pontos += valor
        print(f"\nMandou bem, {self.__nome}! Você ganhou {valor} pontos.")
        print(f"Pontuação total: {self.__pontos}\n")


# ---------------------------------
# SISTEMA DE RANKING (NOVO)
# o sistema guarda historico de jogadores
# ---------------------------------
class RankingSistema:
    def __init__(self):
        self.jogadores = []

    def registrar(self, player: Player):
        # adiciona jogador na lista
        self.jogadores.append(player)

    def mostrar(self):
        print("\n===== PLACAR GERAL =====")
        
        # uso de sorted + lambda para ordenar por pontos
        ordenado = sorted(self.jogadores, key=lambda p: p.get_pontos(), reverse=True)
        
        for pos, jogador in enumerate(ordenado, start=1):
            print(f"{pos}º lugar -> {jogador.get_nome()} com {jogador.get_pontos()} pontos")
        
        print("========================\n")


# ---------------------------------
# classe mais completa que a versão anterior
# ---------------------------------
class GuessGame(GameBase):
    def __init__(self, player: Player):
        self.numero = random.randint(1, 100)
        self.tentativas = 0
        self.max_tentativas = 0
        self.player = player  # associação com Player

    def escolher_nivel(self):
        # existe dificuldade
        print("\nEscolha o nível de dificuldade:")
        print("1 - Fácil (15 tentativas)")
        print("2 - Médio (10 tentativas)")
        print("3 - Difícil (5 tentativas)")

        while True:
            escolha = input("Digite sua escolha: ")

            if escolha == '1':
                self.max_tentativas = 15
                break
            elif escolha == '2':
                self.max_tentativas = 10
                break
            elif escolha == '3':
                self.max_tentativas = 5
                break
            else:
                print("Opção inválida. Tente novamente (1, 2 ou 3).")

    def iniciar(self):
        # separação clara de responsabilidades
        self.escolher_nivel()
        print(f"\nVamos lá, {self.player.get_nome()}!")
        print("Estou pensando em um número entre 1 e 100...")
        print(f"Você tem {self.max_tentativas} tentativas. Boa sorte!\n")

    def jogar(self):
        while self.tentativas < self.max_tentativas:
            try:
                # Melhoria crítica: tratamento de erro
                chute = int(input(f"Tentativa {self.tentativas + 1}/{self.max_tentativas}: "))
            except ValueError:
                print("Digite apenas números válidos.")
                continue

            self.tentativas += 1

            if chute == self.numero:
                print(f"\nParabéns! Você acertou em {self.tentativas} tentativas.")

                # sistema de pontuação inteligente
                restantes = self.max_tentativas - self.tentativas
                bonus = 10 + (restantes * 2)

                self.player.adicionar_pontos(bonus)
                return

            elif chute < self.numero:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")

        # feedback ao jogador
        print("\nSuas tentativas acabaram.")
        print(f"O número correto era: {self.numero}")


# ---------------------------------
# reutilização com polimorfismo
# ---------------------------------
def rodar_partida(jogo: GameBase):
    jogo.iniciar()
    jogo.jogar()


# ---------------------------------
# suporta múltiplos jogadores e partidas
# ---------------------------------
def main():
    ranking = RankingSistema()

    print("=== JOGO DE ADIVINHAÇÃO ===")

    while True:
        nome = input("\nQual seu nome? ")
        jogador = Player(nome)

        partida = GuessGame(jogador)
        rodar_partida(partida)

        # salva jogador no ranking
        ranking.registrar(jogador)
        ranking.mostrar()

        # loop contínuo
        continuar = input("Outro jogador quer tentar? (s/n): ").lower()
        if continuar != 's':
            print("\nObrigado por jogar. Até a próxima!")
            break


if __name__ == "__main__":
    main()
