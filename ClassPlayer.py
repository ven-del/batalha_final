class Player():
    def __init__(self, nome, vida, mana, qtd_pots, skill):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.qtd_pots = qtd_pots
        self.skill = skill

    def usar_pot(self):
        if self.qtd_pots > 0:
            self.vida += 50
            self.qtd_pots -= 1
            print(f'{self.nome} usou uma poção e recuperou 50 pontos de vida. Vida atual: {self.vida}. Poções restantes: {self.qtd_pots}')
        else:
            print(f'{self.nome} não tem poções restantes para usar.')

    def atacar(self, inimigo):
        dano = 20
        inimigo.vida -= dano
        print(f'{self.nome} atacou {inimigo.nome} e causou {dano} pontos de dano.')
    
    def usar_skill(self, inimigo):
        if self.mana >= 30:
            dano = 100
            inimigo.vida -= dano
            self.mana -= 30
            print(f'{self.nome} usou a skill {self.skill} em {inimigo.nome} e causou {dano} pontos de dano..')
        else:
            print(f'{self.nome} não tem mana suficiente para usar a skill.')
