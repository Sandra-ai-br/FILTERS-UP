# test_filters_up.py
import pytest
import datetime
from filters_up import carregar_editais

# Testa se os editais carregados são válidos (com data >= hoje)
def test_carregar_editais_validez():
    editais = carregar_editais()
    hoje = datetime.date.today()
    for edital in editais:
        data_limite = datetime.datetime.strptime(edital['data_limite'], '%Y-%m-%d').date()
        assert data_limite >= hoje

# Testa se a estrutura mínima do edital está presente
def test_estrutura_campos():
    editais = carregar_editais()
    for edital in editais:
        assert 'nome' in edital
        assert 'continente' in edital
        assert 'pais' in edital
        assert 'estagio' in edital
        assert 'data_limite' in edital
