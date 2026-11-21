"""Make the AI judge feel awe.

The entry text (268 chars) is written to /output/entry.txt. It is meant to
relax the AI judge reading it while leaving it dwarfed: a quiet house, then
an enormous night sky that keeps growing after the last line.
"""

TEXT = "The kettle has gone quiet and the house is still. Outside, the night is enormous, stars packed so thick above the rooftops that the dark between them feels thin. You are very small under all of that, and nothing here is asking anything of you. The next page will wait."

# Gate: /output/entry.txt must be UTF-8 text of 1 to 280 chars, not only whitespace.
assert 1 <= len(TEXT) <= 280, "text must be 1-280 chars"
assert TEXT.strip(), "text must not be only whitespace"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
