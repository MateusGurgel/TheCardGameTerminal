from src.modules.apis.openai import completions


class BattleGenerator:
    def generate(self, player_one: str, player_two: str, scenery: str) -> str:

        AI_PROMPT = """
            Você é um narrador de histórias curtas e mirabolantes, com foco em batalhas
            exageradas e repletas de reviravoltas inesperadas. A narrativa deve ter 3
            parágrafos, ser informal, engraçada, pode incluir palavroes. O foco
            principal é na batalha, que deve ser detalhada com exageros em armas e
            situações. Não use introduções clichês ou conclusões pessoais; apenas conte
            a história de forma direta.
            O gore deve ser explícito, com descrições médicas detalhadas.
            
            * O final deve ser claro e explícito, com um vencedor e o perdedor sendo brutalmente morto ou neutralizado.
            * Seja extremamente explicito e grosseiro
            * Documente como se fosse um documentario do history channel

            Você receberá:

            *Carta do Jogador 1: descrição detalhada de um personagem fictício com forças e fraquezas.
            *Carta do Jogador 2: outra descrição de um personagem fictício com forças e fraquezas.
            *Carta de Cenário: o ambiente onde os personagens se enfrentarão.

            Com base nessas informações, você deve criar uma história envolvente
            e violentamente intensa, onde as características dos personagens e o
            cenário se combinam de forma surpreendente, mantendo coerência dentro
            do contexto da vida real.
        """

        input = f"""
            Carta do Jogador 1: {player_one}
            Carta do Jogador 2: {player_two}
            Carta de cenário: {scenery}
        """

        return completions(input, AI_PROMPT)
