import nltk, re, pprint
from nltk import *

text = word_tokenize("And now for something completely different")
nltk.pos_tag(text)
text = word_tokenize("They refuse to permit us to obtain the refuse permit")

nltk.pos_tag(text)


text = word_tokenize("We are going to ski")
nltk.pos_tag(text)
text = word_tokenize("We just bought a ski")
nltk.pos_tag(text)



text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')
text.similar('bought')
text.similar('over')
text.similar('the')


sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"),
            ("cat", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar) 
result = cp.parse(sentence)
print(result)
#result.draw requires more library installs
#it draws a tree of the noun phrases
#result.draw()


cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')

brown = nltk.corpus.brown
for sent in brown.tagged_sents():
    tree = cp.parse(sent)
    for subtree in tree.subtrees():
        if subtree.label() == 'CHUNK': print(subtree)

"""two bad examples below"""
grammar = r"""
 NP: {<DT|JJ|NN.*>+} # Chunk sequences of DT, JJ, NN
 PP: {<IN><NP>} # Chunk prepositions followed by NP
 VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
 CLAUSE: {<NP><VP>} # Chunk NP, VP
 """



cp = nltk.RegexpParser(grammar)

sentence = [("Mary", "NN"), ("saw", "VBD"), ("the", "DT"), ("cat",
"NN"),
 ("sit", "VB"), ("on", "IN"), ("the", "DT"), ("mat", "NN")]

print(cp.parse(sentence))



sentence = [("John", "NNP"), ("thinks", "VBZ"), ("Mary", "NN"), ("saw", "VBD"),
             ("the", "DT"), ("cat", "NN"), ("sit", "VB"),
             ("on", "IN"), ("the", "DT"), ("mat", "NN")]
print(cp.parse(sentence))



"""correct solution to above"""
cp = nltk.RegexpParser(grammar, loop=2)
print(cp.parse(sentence))


sent = nltk.corpus.treebank.tagged_sents()[22]
print(nltk.ne_chunk(sent, binary=True))
print(nltk.ne_chunk(sent))

IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc,
                                     corpus='ieer', pattern = IN):
        print(nltk.sem.rtuple(rel))




from nltk.corpus import conll2002


vnv = """( is/V| # 3rd sing present and was/V|
# past forms of the verb zijn ('be') werd/V|
# and also present wordt/V
# past of worden ('become)
)* # followed by anything van/Prep # followed by van ('of') """
VAN = re.compile(vnv, re.VERBOSE)
for doc in conll2002.chunked_sents('ned.train'):
    for r in nltk.sem.extract_rels('PER', 'ORG',
                                   doc,
                                   corpus='conll2002',
                                   pattern=VAN):
        print(rtuple(rel, lcon=True, rcon=True))
VAN("cornet_d'elzius", 'buitenlandse_handel')
VAN('johan_rottiers', 'kardinaal_van_roey_instituut')
VAN('annie_lennox', 'eurythmics')



locs = [('Omnicom', 'IN', 'New York'),
        ('DDB Needham', 'IN', 'New York'),
        ('Kaplan Thaler Group', 'IN', 'New York'),
        ('BBDO South', 'IN', 'Atlanta'),
        ('Georgia-Pacific', 'IN', 'Atlanta')]

"""Which organizations operate in Atlanta?"""
query = [e1 for (e1, rel, e2) in locs if e2=='Atlanta']
print(query)
