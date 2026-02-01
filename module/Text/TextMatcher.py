import unicodedata


MAX_LCS_CELL_COUNT: int = 20000


def normalize_nfkc(text: str) -> str:
    # NFKC can align full-width/half-width and compatibility characters for matching.
    return unicodedata.normalize("NFKC", text)


def calculate_lcs_length(a: str, b: str) -> int:
    if not a or not b:
        return 0

    if len(a) * len(b) > MAX_LCS_CELL_COUNT:
        # Avoid quadratic cost on long inputs to keep UI checks responsive.
        return 0

    if len(b) > len(a):
        a, b = b, a

    previous: list[int] = [0] * (len(b) + 1)

    for char_a in a:
        current: list[int] = [0]
        for index, char_b in enumerate(b, start=1):
            if char_a == char_b:
                current.append(previous[index - 1] + 1)
            else:
                current.append(max(previous[index], current[index - 1]))
        previous = current

    return previous[-1]


def calculate_lcs_ratio(term: str, source: str) -> float:
    term_length = len(term)
    if term_length == 0:
        return 0.0
    # Use glossary term length so the threshold stays consistent across sources.
    return calculate_lcs_length(term, source) / term_length


def has_lcs_match(term: str, sources: list[str], threshold: float) -> bool:
    if not term:
        return False

    for source in sources:
        if calculate_lcs_ratio(term, source) >= threshold:
            return True

    return False
