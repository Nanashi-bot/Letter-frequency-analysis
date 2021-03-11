# from scrape_letter import letter_frequency
from pathlib import Path

letter_frequency = {'E': 12.02, 'T': 9.1, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88,
                    'C': 2.71, 'M': 2.61, 'F': 2.3, 'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.1, 'Z': 0.07}

monogram = letter_frequency
monogram = dict(sorted(monogram.items()))
bigram = {}
trigram = {}
quadgram = {}

txt = Path(
    'harry-potter-and-the-philosophers-stone-extract.txt').read_text().replace("\n", "").replace(",", '').replace("'", '').replace("/", '').replace(":", '').replace("!", '').replace(".", '').replace('"', '').replace("‘", "").replace("–", "").replace("…", "").replace("’", "").replace("?", "").replace("indb", "").replace(" ", "")
res = ''.join([i for i in txt if not i.isdigit()])


print(res)

test = "A short story is a piece of prose fiction that typically can be read in one sitting and focuses on a self contained incident or series of linked incidents, with the intent of evoking a single effect or mood. The short story is one of the oldest types of literature and has existed in the form of legends, mythic tales, folk tales, fairy tales, fables and anecdotes in various ancient communities across the world. The modern short story developed in the early nineteenth century."
