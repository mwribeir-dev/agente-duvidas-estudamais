class AgenteDuvidas:

    def __init__(self, nome):
        self.nome = nome

    def responder(self, pergunta):
        pergunta = pergunta.lower().strip()

        if pergunta == "o que é python?":
            return "Python é uma linguagem de programação."

        elif pergunta == "o que é api?":
            return "API é uma forma de comunicação entre sistemas."

        return "Desculpe, ainda não sei responder essa pergunta."
