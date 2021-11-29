from secrets import token_urlsafe
from sys import argv
from typing import List


def npss(length: int) -> str:
    """Generates random string of the given length with at least one "-".

    Args:
        length (int): Desired length.

    Returns:
        str: Your new shiny random password.
    """
    while True:
        pss = token_urlsafe(length)[:length]
        if "-" in pss:
            return pss


def argv_pars(arguments: List[str]) -> int:
    """Returns second argv or 30.

    Args:
        argv (List[str]): sys.argv

    Returns:
        int: i >= 1, or 30
    """
    try:
        return max(int(arguments[1]), 1)
    except Exception:
        return 30


def main():
    return npss(argv_pars(argv))


if __name__ == "__main__":
    print(main())
