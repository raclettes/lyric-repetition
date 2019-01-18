import argparse
import sys
import re

from PIL import Image

regex = re.compile('[^a-zA-Z\\s]')

def compose(title, lyrics):
    image = Image.new('RGB', (len(lyrics), len(lyrics)), color = 'black')
    pixels = image.load()

    for w, word in enumerate(lyrics):
        print('{} - {:.2f}%         '.format(word, w/len(lyrics)*100), end='\r')
        for o, other_word in enumerate(lyrics):
            if word == other_word:
                pixels[w, o] = (255, 255, 255)

    image.save('{}.png'.format(title))

def main():
    parser = argparse.ArgumentParser(description='Create lyric repetition map.')
    parser.add_argument('file', action='store', type=str)

    args = parser.parse_args()

    try:
        lyrics = regex.sub('', open(args.file, 'r').read()).split()
    except IOError:
        print('Could not open file {}'.format(args.file))
        sys.exit(1)
    else:
        compose(args.file, lyrics)
        sys.exit(0)


if __name__ == '__main__':
    main()