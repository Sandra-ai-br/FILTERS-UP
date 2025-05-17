# filters_up.py
import csv
import datetime
from ia_agent import responder_agente

# Utilitário para obter data atual
hoje = datetime.date.today()

# Carregar base de editais
EDITAIS_PATH = 'editais.csv'

def carregar_editais():
    editais = []
    with open(EDITAIS_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Verifica se o edital ainda está válido pela data
            data_limite = datetime.datetime.strptime(row['data_limite'], '%Y-%m-%d').date()
            if data_limite >= hoje:
                editais.append(row)
    return editais

def iniciar_formulario():
    print("\n🌀 FILTERS UP — O filtro GEMINI para decolar sua startup\n")
    idade = input("1. Qual a sua idade? ")
    genero = input("2. Qual seu gênero (Feminino, Masculino, Outro)? ")
    if genero.lower() == "outro":
        genero = input("   Especifique seu gênero: ")

    tipo_startup = input("3. Tipo de startup (Ideação, Validação, Pré-semente, etc.): ")
    financiamento = input("4. Você precisa de financiamento em moeda? (Sim/Não): ")
    continente = input("5. Continente da sede da startup: ")
    pais = input("6. País da sede (ou 'TODOS'): ")
    nacionalidade_diferente = input("7. Tem nacionalidade diferente do continente? (Sim/Não): ")

    print("\n🔎 Buscando editais válidos...\n")
    editais = carregar_editais()

    encontrados = []
    for edital in editais:
        if (
            (pais.lower() == "todos" or pais.lower() == edital['pais'].lower()) and
            continente.lower() == edital['continente'].lower() and
            tipo_startup.lower() in edital['estagio'].lower()
        ):
            encontrados.append(edital)

    if encontrados:
        print(f"🎯 Encontramos {len(encontrados)} edital(is) para você:\n")
        for e in encontrados:
            print(f"- {e['nome']} ({e['pais']}, até {e['data_limite']})")
    else:
        print("Nenhum edital compatível encontrado com os filtros atuais.\n")

    # Agente IA responde com uma mensagem contextual
    resposta_ia = responder_agente(idade, genero, tipo_startup, continente, pais, len(encontrados))
    print(f"\n🤖 Agente IA: {resposta_ia}\n")

if __name__ == '__main__':
    iniciar_formulario()
