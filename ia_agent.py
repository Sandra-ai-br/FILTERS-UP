# ia_agent.py
def responder_agente(idade, genero, tipo_startup, continente, pais, total_encontrado):
    idade = int(idade)
    if total_encontrado == 0:
        return (
            f"Mesmo sem editais disponíveis no momento para {tipo_startup} em {pais}, "
            f"continue firme. O cenário está sempre mudando, e sua iniciativa tem grande valor."
        )

    mensagem_base = (
        f"Para uma pessoa de {idade} anos, gênero {genero}, com uma startup em fase de {tipo_startup}, "
        f"com sede em {pais} ({continente}), foram encontrados {total_encontrado} edital(is)."
    )

    if idade <= 25:
        incentivo = "É uma excelente fase para ousar, aprender e crescer." 
    elif idade <= 40:
        incentivo = "Você está num momento estratégico para acelerar sua startup." 
    else:
        incentivo = "Sua experiência pode transformar ideias em realidades sólidas."

    return f"{mensagem_base} {incentivo} Aproveite essas oportunidades e vá com tudo!"
