from agente import AgenteDuvidas

agente = AgenteDuvidas("Tutor IA")

assert agente.nome == "Tutor IA"
assert agente.responder("O que é Python?") == "Python é uma linguagem de programação."
assert agente.responder("O QUE É API?") == "API é uma forma de comunicação entre sistemas."
assert agente.responder("  o que é api?  ") == "API é uma forma de comunicação entre sistemas."
assert agente.responder("O que é banco de dados?") == "Desculpe, ainda não sei responder essa pergunta."

print("✅ Todos os testes passaram!")
