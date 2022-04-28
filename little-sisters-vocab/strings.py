"""Functions for creating, transforming, and adding prefixes to strings."""
import string
from typing import List

def add_prefix_un(word: str) -> str:
    return f"un{word}"


def make_word_groups(vocab_words: List[str]) -> str:
    return f"{vocab_words[0]} :: {' :: '.join([f'{vocab_words[0]}{word}' for word in vocab_words[1:]])}"


def remove_suffix_ness(word: str) -> str:
    aux = word[:-4]
    if aux.endswith('i'):
        aux = f"{aux[:-1]}y"
    return aux


def adjective_to_verb(sentence: str, index: int) -> str:
    input = sentence.split()[index].strip(string.punctuation)
    return f"{input}en"
