import difflib
import glob
import os
import re

from typing import List, Optional, TextIO


NEWLINE = os.linesep


def remove_values_from_env_vars(lines: List[str]) -> List[str]:
    return [re.sub(r"=.*", r"=", line) for line in lines]


def get_diff_message(
    name1: str, name2: str, lines1: List[str], lines2: List[str]
) -> Optional[str]:
    return (
        NEWLINE.join(
            difflib.unified_diff(
                lines1, lines2, fromfile=name1, tofile=name2, lineterm="", n=0
            )
        )
        or None
    )


def read_lines(file: TextIO) -> List[str]:
    return file.read().splitlines()


def get_no_file_message(name1: str, name2: str, error: FileNotFoundError) -> str:
    return (
        f"000 {name1}{NEWLINE}"
        f"xxx {name2}{NEWLINE}"
        f"@@ @@{NEWLINE}"
        f"{error}{NEWLINE}"
    )


def get_diff_for_dotenv(dotenv: str) -> Optional[str]:
    try:
        with open(dotenv) as file1:
            lines1 = read_lines(file1)
        with open(dotenv2 := f"{dotenv}.example") as file2:
            lines2 = read_lines(file2)

        lines1 = remove_values_from_env_vars(lines1)

        return get_diff_message(dotenv, dotenv2, lines1, lines2)
    except FileNotFoundError as e:
        return get_no_file_message(dotenv, dotenv2, e)


def get_all_dotenvs() -> List[str]:
    return glob.glob("./**/.env", recursive=True)


def get_all_diffs() -> List[str]:
    return [
        diff
        for dotenv in get_all_dotenvs()
        if (diff := get_diff_for_dotenv(dotenv)) is not None
    ]


def main() -> None:
    all_diffs = get_all_diffs()
    if all_diffs:
        message = (NEWLINE * 2).join(all_diffs)
        print(message)
        exit(1)
    else:
        exit(0)
