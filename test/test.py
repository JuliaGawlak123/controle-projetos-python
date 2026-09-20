from src.main import *
from unittest.mock import patch


def test_exibir_menu(capsys):

    exibir_menu()

    captured = capsys.readouterr()

    assert "CONTROLE DE PROJETOS" in captured.out
    assert "1 - Cadastrar projeto" in captured.out
    assert "2 - Listar projetos" in captured.out
    assert "3 - Buscar projeto" in captured.out
    assert "4 - Alterar status" in captured.out
    assert "0 - Sair" in captured.out


def test_cadastrar_projeto():

    projetos.clear()

    with patch("builtins.input", side_effect=[
        "001",
        "Projeto Teste",
        "Cliente Teste",
        "Em Cotação",
        "20/09/2026"
    ]):

        resultado = cadastrar_projeto()

    assert resultado == {
        "codigo": "001",
        "nome": "Projeto Teste",
        "cliente": "Cliente Teste",
        "status": "Em Cotação",
        "data": "20/09/2026"
    }


def test_buscar_projeto():

    projetos.clear()

    projetos.append({
        "codigo": "001",
        "nome": "Projeto Teste",
        "cliente": "Cliente Teste",
        "status": "Em Cotação",
        "data": "20/09/2026"
    })

    with patch("builtins.input", return_value="001"):

        resultado = buscar_projeto()

    assert resultado["codigo"] == "001"
    assert resultado["nome"] == "Projeto Teste"


def test_alterar_status():

    projetos.clear()

    projetos.append({
        "codigo": "001",
        "nome": "Projeto Teste",
        "cliente": "Cliente Teste",
        "status": "Em Cotação",
        "data": "20/09/2026"
    })

    with patch("builtins.input", side_effect=[
        "001",
        "Nomeado"
    ]):

        resultado = alterar_status()

    assert resultado["status"] == "Nomeado"