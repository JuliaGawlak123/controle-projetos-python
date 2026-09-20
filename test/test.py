from src.main import *
from unittest.mock import patch
import pytest


@pytest.fixture
def projeto_teste():

    projeto = {
        "codigo": "001",
        "nome": "Projeto Teste",
        "cliente": "Cliente Teste",
        "status": "Em Cotação",
        "data": "20/09/2026"
    }

    yield projeto

    projetos.clear()


@pytest.mark.asyncio
async def test_exibir_menu(capsys):

    exibir_menu()

    captured = capsys.readouterr()

    assert "CONTROLE DE PROJETOS" in captured.out
    assert "1 - Cadastrar projeto" in captured.out
    assert "2 - Listar projetos" in captured.out
    assert "3 - Buscar projeto" in captured.out
    assert "4 - Alterar status" in captured.out
    assert "0 - Sair" in captured.out


@pytest.mark.asyncio
async def test_cadastrar_projeto():

    projetos.clear()

    with patch("builtins.input", side_effect=[
        "001",
        "Projeto Teste",
        "Cliente Teste",
        "Em Cotação",
        "20/09/2026"
    ]):

        resultado = await cadastrar_projeto()

    assert resultado == {
        "codigo": "001",
        "nome": "Projeto Teste",
        "cliente": "Cliente Teste",
        "status": "Em Cotação",
        "data": "20/09/2026"
    }


@pytest.mark.asyncio
async def test_buscar_projeto(projeto_teste):

    projetos.append(projeto_teste)

    with patch("builtins.input", return_value="001"):

        resultado = await buscar_projeto()

    assert resultado == projeto_teste


@pytest.mark.asyncio
async def test_alterar_status(projeto_teste):

    projetos.append(projeto_teste)

    with patch("builtins.input", side_effect=[
        "001",
        "Nomeado"
    ]):

        resultado = await alterar_status()

    assert resultado["status"] == "Nomeado"