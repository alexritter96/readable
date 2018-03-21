""" Readable — a CLI tool for readability text analysis
Usage:
  read <text> [--flesch-kincaid]
  read <text> [--gunning-fog]
  read <text> [--smog]
  read <text> [--automated]
  read <text> [--chars]
  read <text> [--sentences]
  read <text> [--words]
  read <text> [--syllables]
  read <text> [--avgchars]
  read <text> [--avgwords]
  read <text> [--htmltext]
  read (-h | --help)
  read --version
Options:
  -h --help           Show this screen.
  --version           Show version.
  --flesch-kincaid    Returns the Flesch-Kincaid Grade Level
  --gunning-fog       Returns the Gunning Fog Index
  --smog              Returns the Smog Index
  --automated         Returns the Automated Readability Index
  --chars             Returns the Total Number of Characters
  --sentences         Returns the Total Number of Sentences
  --words             Returns the Total Number of Words
  --syllables         Returns Average Number of Syllables per Word
  --avgchars          Returns the Average Number of Characters per Word
  --avgwords          Returns the Average Number of Words per Sentence
  --htmltext          Returns Text of HTML Document

"""

from docopt import docopt
from readlib import Readability
import crayons


def main():
    args = docopt(__doc__, version='Readable v1.0')
    text = ""
    read = Readability(text)

    if args['<text>']:
        if args['--flesch-kincaid']:
            print(crayons.red(read.flesch_kincaid()))

        if args['--gunning-fog']:
            print(crayons.blue(read.gunning_fog()))

        if args['--smog']:
            print(read.smog_index())

        if args['--automated']:
            print(read.ari())

        if args['--chars']:
            print("Characters: {}".format(read.char()))

        if args['--sentences']:
            print("Sentences: {}".format(read.sent_count()))

        if args['--words']:
            print("Words: {}".format(read.word_count()))

        if args['--avgchars']:
            print("Average Number of Characters Per Word: {}".format(read.avg_char()))

        if args['--syllables']:
            print("Syllables per word: {}".format(read.avg_syl()))

        if args['--avgwords']:
            print("Average Number of Words Per Sentence: {}".format(read.avg_words()))

        if args['--htmltext']:
            print(read.get_url('https://www.marxists.org/archive/marx/works/1844/manuscripts/hegel.htm#44H6'))


if __name__ == '__main__':

    main()





