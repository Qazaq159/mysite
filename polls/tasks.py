import time


def make_gg(name: str) -> str:
    if name == 'Yerke':
        raise Exception('Heyyyy!')

    name += ' starteD!'
    surname = name[::-1]
    word = name + ' ' + surname
