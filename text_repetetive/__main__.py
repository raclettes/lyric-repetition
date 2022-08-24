import argparse
import random
import re
import sys

from PIL import Image

regex = re.compile("[^a-zA-Z\\s]")

unique_colors = {}


def compose(title, lyrics):
    image = Image.new("RGB", (len(lyrics), len(lyrics)), color="black")

    for w, word in enumerate(lyrics):
        word = word.lower()
        print("{} - {:.2f}%         ".format(word, w / len(lyrics) * 100), end="\r")
        for o, other_word in enumerate(lyrics):
            other_word = other_word.lower()
            if word == other_word:
                if not unique_colors.get(word, None):
                    unique_colors[word] = (
                        random.randint(100, 255),
                        random.randint(100, 255),
                        random.randint(100, 255),
                    )
                image.putpixel((w, o), unique_colors[word])

    image = image.resize((image.size[0] * 8, image.size[1] * 8), Image.NEAREST)
    image.save("{}.png".format(title))


def main():
    parser = argparse.ArgumentParser(description="Create lyric repetition map.")
    parser.add_argument("file", action="store", type=str)

    args = parser.parse_args()

    try:
        lyrics = regex.sub("", open(args.file, "r").read()).split()
    except IOError:
        print("Could not open file {}".format(args.file))
        sys.exit(1)
    else:
        compose(args.file, lyrics)
        sys.exit(0)


if __name__ == "__main__":
    main()
