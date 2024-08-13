from src.modules.apis.openai import completions


class SceneGenerator:
    def generate(self, player_one: str, player_two: str) -> str:
        AI_PROMPT = """
            Crie um cenario de confronto baseado no seguinte input:
            
            jogador1: <Descrição do jogador 1>
            jogador2: <Descrição do jogador 2>

            * O cenario deve ser relevante para o contexto dos 2 personagens

            *Use localizacoes reais, e de nacionalidade compativel com os personagens

            *Seja extremamente breve

            exemplos:

            Uma ponte em afua, belem do para, onde ambos os personagens se encaram

            Brasilia, onde o jogador1 esta no topo do palacio do planalto, 
            encarando o jogador2 no meio da praca dos 3 poderes

            Estudio principal da rede globo, onde o jogador1 esta apresentando, 
            enquanto o jogador2 esta olhando fixamente para o jogador1
        """

        input = f"""
            Jogador1: {player_one}
            Jogador2: {player_two}
        """

        return completions(input, AI_PROMPT)
