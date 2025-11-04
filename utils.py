def style(
    text: str, *styles, fg: tuple[int, int, int] = None, bg: tuple[int, int, int] = None
) -> str:
    """
    Styles text using RGB colors and ANSI text styles.

    Args:
        text: string to style
        *styles: text styles: bold, dim, italic, underline, blink, reverse, hidden, strikethrough
        fg: optional foreground RGB tuple (R,G,B)
        bg: optional background RGB tuple (R,G,B)

    Returns:
        Text wrapped in ANSI escape codes for truecolor + styles
    """

    # Text styles (ANSI)
    ANSI_CODES = {
        "bold": "1",
        "dim": "2",
        "italic": "3",
        "underline": "4",
        "blink": "5",
        "reverse": "7",
        "hidden": "8",
        "strikethrough": "9",
    }

    codes = [ANSI_CODES[s] for s in styles if s in ANSI_CODES]

    # RGB colors
    if fg:
        codes.append(f"38;2;{fg[0]};{fg[1]};{fg[2]}")
    if bg:
        codes.append(f"48;2;{bg[0]};{bg[1]};{bg[2]}")

    if codes:
        return f"\033[{';'.join(codes)}m{text}\033[0m"
    return text
