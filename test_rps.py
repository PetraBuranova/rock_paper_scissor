import rps
import pytest
import subprocess
import sys
import random

def test_rock_is_valid_play():
    assert rps.is_valid_play("rock") is True

def test_paper_is_valid_play():
    assert rps.is_valid_play("rock") is True

def test_scissors_is_valid_play():
    assert rps.is_valid_play("rock") is True

def test_lizzard_is_valid_play():
    assert rps.is_valid_play("lizard") is False

def test_computer_is_valid():
    for _ in range(5000):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)


def test_computer_plays_randomly():
    plays = [rps.generate_computer_play() for _ in range(5000)]
    rocks = plays.count("rock")
    papers = plays.count("paper")
    scissors = plays.count("scissor")
    print(rocks, papers, scissors)
    # pokud test projde, print nevyjede; pokud test selže, tak pytest vypíše i printy... pro kontrolu
    assert rocks > 200
    assert papers > 200
    assert scissors > 200
    # pokud více assrtů, tak se zastaví u prvního chybového a na další nedoje

def test_paper_beats_rock():
    result = rps.evaluate_game("paper", "rock")
    assert result == "human"

def test_scissor_beats_paper():
    result = rps.evaluate_game("scissor", "paper")
    assert result == "human"

def test_scissor_beats_paper():
    result = rps.evaluate_game("scissor", "paper")
    assert result == "human"

def test_scissor_dont_beats_rock():
    result = rps.evaluate_game("scissor", "rock")
    assert result == "computer"

def test_scissor_tie_scissor():
    result = rps.evaluate_game("scissor", "scissor")
    assert result == "tie"

def input_faked_rock(prompt):
    print(prompt)
    return "rock"

def input_faked_paper(prompt):
    print(prompt)
    return "paper"

def input_faked_scissor(prompt):
    print(prompt)
    return "scissor"


"""
tvoření fixtures: 

@pytest.fixture
def fake_input_rock(monkeypatch):
    monkeypatch.setattr("builtins.input", input_faked_rock)
"""


"""
původní verze, po přdělání : def test_full_game(capsys), nefunguje
def test_full_main(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", input_faked_rock)
    rps.main()
    captured = capsys.readouterr()
    assert "rock, paper, or scissors?" in captured.out

def test_full_main_paper(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", input_faked_paper)
    rps.main()
    captured = capsys.readouterr()
    assert "rock, paper, or scissors?" in captured.out

def test_full_main_scissor(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", input_faked_scissor)
    rps.main()
    captured = capsys.readouterr()
    assert "rock, paper, or scissors?" in captured.out

"""

def test_full_game(capsys):
    rps.main(input=input_faked_rock)
    captured = capsys.readouterr()
    assert "rock, paper, or scissors?" in captured.out


def test_wrong_play_result_in_repeated_question():
    cp = subprocess.run([sys.executable, "rps.py"], encoding="cp1250", stdout=subprocess.PIPE, input="dragon\nrock\n", check=True)
    # check=True -> pokud chyba vypíše podrobnosti
    # input="dragon\nrock\n" vloží dragon enter(\n), rock enter(\n)
    assert cp.stdout.count("rock, paper, or scissors") == 2

def test_computer_plays_randomly():
    pass