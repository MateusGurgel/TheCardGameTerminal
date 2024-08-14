from src.modules.agents.generator.battle_generator import BattleGenerator
from src.modules.agents.generator.scene_generator import SceneGenerator


def main() -> None:

    scenegenerator = SceneGenerator()
    battlegenerator = BattleGenerator()

    player_one_score = 0
    player_two_score = 0

    for i in range(0, 3):
        print(f"Rodada {i + 1}")

        card_player_one = input("Digite o nome do jogador 1: ")
        card_player_two = input("Digite o nome do jogador 2: ")

        cenario = scenegenerator.generate(card_player_one, card_player_two)
        battle = battlegenerator.generate(card_player_one, card_player_two, cenario)

        print("Batalha:")
        print(battle.battle)
        print("===================================================================")

        if battle.player_one_won:
            player_one_score += 1
        else:
            player_two_score += 1

    if player_one_score > player_two_score:
        print(f"O jogador 1 venceu com {player_one_score} pontos")
    elif player_one_score < player_two_score:
        print(f"O jogador 2 venceu com {player_two_score} pontos")
    else:
        print("Empate")


if __name__ == "__main__":
    main()
