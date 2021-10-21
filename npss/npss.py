from secrets import token_urlsafe
from sys import argv
from typing import List


def npss(length: int) -> str:
    """Generates random password of the given length with at least one "-".

    Args:
        length (int, optional): Password length.

    Returns:
        str: Your new random password
    """
    if not length:
        length = 30

    while True:
        pss = token_urlsafe(length)[:length]
        if "-" in pss:
            return pss


def argv_pars(arguments: List[str]) -> int:
    """Parses argv, bigest int in arguments or 1

    Args:
        argv (List[str]): sys.argv

    Returns:
        int: i >= 1, or 30
    """

    r = []
    for i in arguments:
        try:
            r.append(int(i))
        except Exception:
            pass

    r = [x for x in r if x > 0]
    return max(r) if r else 30


if __name__ == "__main__":
    print(npss(argv_pars(argv)))
