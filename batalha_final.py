import time
import ClassPlayer
import ClassEnemy

Chrono = ClassPlayer.Player("Chrono", 999, 250, 3, "Luminaire")
Luca = ClassPlayer.Player("Luca", 999, 250, 3, "Eruption")
Marle = ClassPlayer.Player("Marle", 999, 250, 3, "Ice Shot")
Lavos = ClassEnemy.Enemy("Lavos", 500, 100, "Dark Missile")

vida_da_party = Chrono.vida <= 0 and Luca.vida <= 0 and Marle.vida <= 0

while not vida_da_party and Lavos.vida > 0:
    print(f"""
    Status da batalha:
    {Chrono.nome} - Vida: {Chrono.vida}, Mana: {Chrono.mana}, Poções: {Chrono.qtd_pots}
    {Luca.nome} - Vida: {Luca.vida}, Mana: {Luca.mana}, Poções: {Luca.qtd_pots}
    {Marle.nome} - Vida: {Marle.vida}, Mana: {Marle.mana}, Poções: {Marle.qtd_pots}
    {Lavos.nome} - Vida: ???, Mana: ???
           """)
    for player in [Chrono, Luca, Marle]:
        if player.vida > 0:
            time.sleep(2)
            acao = input(
                f"{player.nome}, escolha sua ação (1 - atacar, 2 - usar skill, 3 - usar pot): ").lower()
            if acao == "1":
                player.atacar(Lavos)
            elif acao == "2":
                player.usar_skill(Lavos)
            elif acao == "3":
                player.usar_pot()
            else:
                print("Ação inválida. Tente novamente.")
    if Lavos.vida > 0:
        random_action = ["atacar", "usar_skill"]
        import random
        acao_lavos = random.choice(random_action)
        if acao_lavos == "atacar":
            print("=" * 50)
            print("Lavos usou um ataque em área na equipe")
            print("=" * 50)
            time.sleep(1)
            Lavos.atacar(Chrono)
            Lavos.atacar(Luca)
            Lavos.atacar(Marle)
        elif acao_lavos == "usar_skill":
            print("=" * 50)
            print("Lavos usou uma habilidade em área na equipe")
            print("=" * 50)
            time.sleep(1)
            Lavos.usar_skill(Chrono)
            Lavos.usar_skill(Luca)
            Lavos.usar_skill(Marle)
    vida_da_party = Chrono.vida <= 0 and Luca.vida <= 0 and Marle.vida <= 0

if vida_da_party:
    print("A party foi derrotada por Lavos. Fim de jogo.")
else:
    print("Parabéns! A party derrotou Lavos e salvou o mundo!")