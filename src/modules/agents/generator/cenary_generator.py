from src.modules.apis.openai import completions


class CenaryGenerator:
    def generate(player_one: str, player_two: str) -> str:
        AI_PROMPT = """
            Crie um cenario de confronto baseado no seguinte input:
            jogador1: {player_one}
            jogador2: {player_two}

            * O cenario deve ser relevante para o contexto dos 2 personagens

            *Use localizacoes reais, e de nacionalidade compativel com os personagens

            *Seja extremamente breve

            exemplos:

            Uma ponte em afua, belem do para, onde ambos os personagens se encaram

            Brasilia, onde o {player_one} esta no topo do palacio do planalto, 
            encarando o {player_two} no meio da praca dos 3 poderes

            Estudio principal da rede globo, onde o {player_one} esta apresentando, 
            enquanto o {player_two} esta olhando fixamente para o {player_one}
        """

        input = f"""
            Jogador1: {player_one}
            Jogador2: {player_two}
        """

        return completions(input, AI_PROMPT)
