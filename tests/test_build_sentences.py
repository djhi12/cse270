import pytest
import json
from unittest.mock import patch, mock_open
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                             get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)


def test_get_seven_letter_word():
    with patch('builtins.input', return_value='elephant'):
        assert get_seven_letter_word() == 'ELEPHANT'
    with patch('builtins.input', return_value='cat'):
        with pytest.raises(ValueError):
            get_seven_letter_word()


def test_parse_json_from_file():
    mock_data = {'adjectives': ['happy', 'sad'], 'nouns': ['cat', 'dog']}
    with patch('builtins.open', mock_open(read_data=json.dumps(mock_data))):
        result = parse_json_from_file('fake_path.json')
        assert result == mock_data
    with patch('builtins.open', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            parse_json_from_file('nonexistent_file.json')
    with patch('builtins.open', mock_open(read_data='invalid_json')):
        with pytest.raises(json.JSONDecodeError):
            parse_json_from_file('invalid_json.json')


def test_choose_sentence_structure():
    structure = choose_sentence_structure()
    assert structure in structures


def test_get_pronoun():
    pronoun = get_pronoun()
    assert pronoun in ["he", "she", "they", "I", "we"]


def test_get_article():
    article = get_article()
    assert article in ["a", "the"]


def test_get_word():
    data = {
        'adjectives': ['happy', 'sad', 'angry', 'cheerful'],
        'nouns': ['cat', 'dog', 'house', 'car'],
        'verbs': ['run', 'jump', 'swim', 'drive'],
        'adverbs': ['quickly', 'slowly', 'happily', 'sadly'],
        'prepositions': ['on', 'under', 'over', 'through']
    }
    assert get_word('A', data['adjectives']) == 'happy'
    assert get_word('C', data['nouns']) == 'house'


def test_fix_agreement():
    sentence = ["he", "quickly", "run", "to", "a", "old", "house"]
    fix_agreement(sentence)
    assert sentence == ["he", "quickly", "runs", "to", "an", "old", "house"]

    sentence = ["the", "happy", "cat", "run", "to", "the", "big", "house"]
    fix_agreement(sentence)
    assert sentence == ["the", "happy", "cat",
                        "runs", "to", "the", "big", "house"]


def test_build_sentence():
    data = {
        'adjectives': ['happy', 'sad', 'angry', 'cheerful'],
        'nouns': ['cat', 'dog', 'house', 'car'],
        'verbs': ['run', 'jump', 'swim', 'drive'],
        'adverbs': ['quickly', 'slowly', 'happily', 'sadly'],
        'prepositions': ['on', 'under', 'over', 'through']
    }
    seed_word = "elephant"
    structure = ["ART", "ADJ", "NOUN", "ADV",
                 "VERB", "PREP", "ART", "ADJ", "NOUN"]
    sentence = build_sentence(seed_word, structure, data)
    assert isinstance(sentence, str)
    assert len(sentence) > 0
