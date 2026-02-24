class Enemy():
    def __init__(self, nome, vida, mana, skill):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.skill = skill

    def atacar(self, jogador):
        dano = 15
        jogador.vida -= dano
        print(f'{self.nome} atacou {jogador.nome} e causou {dano} pontos de dano. Vida de {jogador.nome} agora: {jogador.vida}')

    def usar_skill(self, jogador):
        if self.mana >= 25:
            dano = 70
            jogador.vida -= dano
            self.mana -= 25
            print(f'{self.nome} usou a skill {self.skill} em {jogador.nome} e causou {dano} pontos de dano.')
        else:
            print(f'{self.nome} não tem mana suficiente para usar a skill.')
