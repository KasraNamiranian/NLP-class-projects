import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.stem import StemmerI,PorterStemmer,WordNetLemmatizer,LancasterStemmer,SnowballStemmer,RegexpStemmer
from nltk.tokenize import word_tokenize,sent_tokenize,regexp_tokenize,WhitespaceTokenizer,SpaceTokenizer,TreebankWordTokenizer
from nltk.corpus import stopwords

text = "Technology is advancing rapidly, changing the way we communicate, work, and live. Many companies are adopting new strategies to improve efficiency and reduce costs. Employees are encouraged to develop their skills and adapt to evolving roles. Innovations such as artificial intelligence and machine learning are transforming industries. However, some challenges remain. Workers are sometimes worried about job security, as automation can replace certain tasks. Ultimately, adapting to these changes is crucial for personal and professional growth."

stop = set(stopwords.words("english"))

# tokenization

# word_tokenizer
word_tokenizer = word_tokenize(text=text)
print(f'\nword tokenizer: {word_tokenizer}\n\n')

# sentence_tokenizer
sent_tokenizer = sent_tokenize(text=text)
print(f'sentence tokenizer: {sent_tokenizer}\n\n')

#treebank
treebank = TreebankWordTokenizer()
tree_tokenizer = treebank.tokenize(text=text)
print(f'treebank tokenizer: {tree_tokenizer}\n\n')
#space
space = SpaceTokenizer()
space_tokenizer = space.tokenize(text)
print(f'space tokenizer: {space_tokenizer}\n\n')
#whitespace
whitespace = WhitespaceTokenizer()
white_space_tokenizer = whitespace.tokenize(text=text)
print(f'whitespace tokenizer: {white_space_tokenizer}\n\n')

# delete stopwords
word_filter = [w for w in word_tokenizer if w not in stop]
word_filter = [word.lower() for word in word_filter]
print(f'word filter: {word_filter}\n\n')

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in word_filter]
print(f'lemmatized words: {lemmatized_words}\n\n')

#porterStemmer was better so i used porterstemmer.
# lcs = LancasterStemmer()
ps = PorterStemmer()
# snow = SnowballStemmer("english")
# reg = RegexpStemmer("english")

# lcs_stem = [lcs.stem(word) for word in word_filter]
ps_stem =  [ps.stem(word) for word in word_filter]
# snow_stem =[snow.stem(word) for word in word_filter]
# print(f'lcs: {lcs_stem}\n')
print(f'ps: {ps_stem}\n')
# print(f'snow: {snow_stem}\n' )
