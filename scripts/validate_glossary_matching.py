import sys
from pathlib import Path


def main() -> None:
    root_dir = Path(__file__).resolve().parents[1]
    # Allow running the script directly without installing the package.
    sys.path.append(str(root_dir))

    from module.Text.TextMatcher import calculate_lcs_ratio
    from module.Text.TextMatcher import normalize_nfkc

    srcs: list[str] = ["ABCＰ"]
    glossary_src: str = "ABCP"
    normalized_full = normalize_nfkc("\n".join(srcs))
    assert normalize_nfkc(glossary_src) in normalized_full

    src_text: str = "Colour"
    glossary_color: str = "Color"
    normalized_src = normalize_nfkc(src_text.lower())
    normalized_term = normalize_nfkc(glossary_color.lower())
    ratio = calculate_lcs_ratio(normalized_term, normalized_src)
    assert ratio >= 0.8

    src_text_short: str = "abc"
    glossary_longer: str = "abcd"
    normalized_src_short = normalize_nfkc(src_text_short.lower())
    normalized_term_longer = normalize_nfkc(glossary_longer.lower())
    ratio = calculate_lcs_ratio(normalized_term_longer, normalized_src_short)
    assert ratio == 0.75


if __name__ == "__main__":
    main()
