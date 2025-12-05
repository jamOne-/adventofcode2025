def read_lines(filename: str) -> list[str]:
    with open(filename, encoding="UTF-8") as f:
        lines = f.readlines()
    return lines
