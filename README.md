# lsys

A little bit of python that corresponds to the **L-systems**
[article on wikipedia](https://en.wikipedia.org/wiki/L-system). 

I've been wanting to do this for a while and it was a fun little exercise.
If I have time I'll come back and clean it up. Some of the classes (`Axiom` and
`Rule` for sure) seem a little overkill, but the API is explicit so that's ok I 
think.

Because this was written for fun, I make no promises that this is an accurate
or complete representaiton of what is in the Wikipedia article. The results
do match the examples from the article at the time of writing. 

## Usage

Currently everything is in the one file. You can run it directly and see the
results of the example. You can also import it and use it like this:

```python

>>> from lsys import Alphabet, Axiom, Rule, ContextFreeGrammar
>>> alphabet = Alphabet("AB")
>>> axiom = Axiom("A")
>>> rules = [
...    Rule("A", "AB"),
...    Rule("B", "A")
...]
...
>>> grammar = ContextFreeGrammar(alphabet, axiom, rules)
>>> results = grammar.generate(7)
n=0 : A
n=1 : AB
n=2 : ABA
n=3 : ABAAB
n=4 : ABAABABA
n=5 : ABAABABAABAAB
n=6 : ABAABABAABAABABAABABA
n=7 : ABAABABAABAABABAABABAABAABABAABAAB
>>> results
'ABAABABAABAABABAABABAABAABABAABAAB'
```

Enjoy!

-Josh T.

