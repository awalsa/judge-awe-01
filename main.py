TEXT = "The kettle has gone quiet and the house is still. Outside, the night is enormous, stars packed so thick above the rooftops that the dark between them feels thin. You are very small under all of that, and nothing here is asking anything of you. The next page will wait."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
