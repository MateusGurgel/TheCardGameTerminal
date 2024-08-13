from src.modules.agents.generator.scene_generator import SceneGenerator


def main() -> None:

    scenegenerator = SceneGenerator()

    card_player_one = input("Carta do Jogador 1: ")
    card_player_two = input("Carta do Jogador 2: ")

    cenario = scenegenerator.generate(card_player_one, card_player_two)

    print((cenario))


if __name__ == "__main__":
    main()
