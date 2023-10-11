#Importing libraries
from collections import Counter, defaultdict
from transformers import AutoTokenizer
import os
​
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
/kaggle/input/wiki-corpus-txt-data/wiki_corpus.txt
add Codeadd Markdown
Loading the data
add Codeadd Markdown
with open('/kaggle/input/wiki-corpus-txt-data/wiki_corpus.txt', encoding = 'utf8') as f:
    corpus = f.readlines()
    print(corpus[:5])
['YMCA in South Australia\n', "South Australia (SA) \xa0has a unique position in Australia's history as, unlike the other states which were founded as colonies, South Australia began as a self governing province Many were attracted to this and Adelaide and SA developed as an independent and free thinking state.\n", 'The compound of philosophical radicalism, evangelical religion and self reliant ability typical of its founders had given an equalitarian flavour to South Australian thinking from the beginning.\n', 'It was into this social setting that in February 1850 a meeting was called primarily for the formation of an Association (apparently meaning a Y.M.C.A.)\n', "for apprentices and others, after their day's work, to enjoy books, lectures, discussions, readings, friendly relief and recreation for a leisure hour.\n"]
add Codeadd Markdown
Setting up parameters
add Codeadd Markdown
vocab_size = 1000
add Codeadd Markdown
Creating class for the BPE
add Codeadd Markdown
n
class BPE():
    def __init__(self, corpus, vocab_size):
        self.corpus = corpus
        self.vocab_size = vocab_size
        #Pre-tokenize the corpus into words, BERT pre-tokenizer is used here
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.word_freqs = defaultdict(int)
        self.splits = {}
        self.merges = {}
    
    def train(self):
        #Compute the frequencies of each word in the corpus
        for text in self.corpus: 
            words_with_offsets = self.tokenizer.backend_tokenizer.pre_tokenizer.pre_tokenize_str(text)
            new_words = [word for word, offset in words_with_offsets]
            for word in new_words:
                self.word_freqs[word] += 1
        #Compute the base vocabulary of all characters in the corpus 
        alphabet = []
        for word in self.word_freqs.keys():
            for letter in word:
                if letter not in alphabet:
                    alphabet.append(letter)
        alphabet.sort()
        #Add the special token </w> at the beginning of the vocabulary
        vocab = ['</w>'] + alphabet.copy()
        #Split each word into individual characters before training
        self.splits = {word: [c for c in word] for word in self.word_freqs.keys()}
        #Merge the most frequent pair iteratively until the vocabulary size is reached
        while len(vocab) < self.vocab_size:
            #Compute the frequency of each pair
            pair_freqs = self.compute_pair_freqs()
            #Find the most frequent pair
            best_pair = ""
            max_freq = None
            for pair, freq in pair_freqs.items():
                if max_freq is None or max_freq < freq:
                    best_pair = pair
                    max_freq = freq
            #Merge the most frequent pair
            self.splits = self.merge_pair(*best_pair)
            self.merges[best_pair] = best_pair[0] + best_pair[1]
            vocab.append(best_pair[0] + best_pair[1])
        return self.merges
    
    def compute_pair_freqs(self):
        #Compute the frequency of each pair
        pair_freqs = defaultdict(int)
        for word, freq in self.word_freqs.items():
            split = self.splits[word]
            if len(split) == 1:
                continue
            for i in range(len(split) - 1):
                pair = (split[i], split[i + 1])
                pair_freqs[pair] += freq
        return pair_freqs
    
    def merge_pair(self, a, b):
        #Merge the given pair
        for word in self.word_freqs:
            split = self.splits[word]
            if len(split) == 1:
                continue
            i = 0
            while i < len(split) - 1:
                if split[i] == a and split[i + 1] == b:
                    split = split[:i] + [a + b] + split[i + 2:]
                else:
                    i += 1
            self.splits[word] = split
        return self.splits
    
    def tokenize(self, text):
        #Tokenize a given text with trained BPE Tokenizer (including pre-tokenization, split, and merge)
        pre_tokenize_result = self.tokenizer._tokenizer.pre_tokenizer.pre_tokenize_str(text)
        pre_tokenized_text = [word for word, offset in pre_tokenize_result]
        splits_text = [[l for l in word] for word in pre_tokenized_text]
        for pair, merge in self.merges.items():
            for idx, split in enumerate(splits_text):
                i = 0
                while i < len(split) - 1:
                    if split[i] == pair[0] and split[i + 1] == pair[1]:
                        split = split[:i] + [merge] + split[i+2:]
                    else:
                        i += 1
                splits_text[idx] = split
        result = sum(splits_text, [])
        return result
add Codeadd Markdown
Testing
add Codeadd Markdown
bpe = BPE(corpus = corpus, vocab_size = vocab_size)
bpe.train()
text = "Love, hate, or feel meh about Harry Potter, it’s hard to argue that J.K. Rowling filled the books with intentional writing choices. From made up words to the meanings of names to the well-scripted first and last lines of each novel, Rowling wanted to the writing to match the intricate fantasy world she created for the now-iconic boy wizard. To examine a few of these choices, I’ll be taking a closer look at the first line of Harry Potter, as well as the last lines, from all of the Harry Potter novels."
print(f"\nBPE tokenization result of text \n'{text}'")
print(bpe.tokenize(text))
