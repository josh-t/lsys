#!/usr/bin/env python

# https://en.wikipedia.org/wiki/L-system

class ContextFreeGrammar(object):

    def __init__(self, alphabet, axiom, rules):

        alphabet.validate(axiom.symbols)                

        self._rule_lookup = {}
        for rule in rules:
            alphabet.validate(rule.predecessor)
            alphabet.validate(rule.successor)

            if rule.predecessor in self._rule_lookup:
                raise ValueError(
                    "Multiple rules with predecessor '{p}'".format(
                    p=rule.predecessor)
                )
            else:
                self._rule_lookup[rule.predecessor] = rule

        self._alphabet = alphabet
        self._axiom = axiom
        self._rules = rules

    def generate(self, iterations):

        state = self.axiom.symbols
        print "n=0 : {s}".format(s=state)

        for i in range(0, iterations):
            new_state = []

            # context free (one symbol at a time)
            for symbol in state:
                
                if (self.alphabet.is_constant(symbol) or 
                    symbol not in self._rule_lookup):
                    new_state.append(symbol)
                else:
                    rule = self._rule_lookup[symbol]
                    new_state.append(rule.successor)
            
            state = "".join(new_state)
            print "n={i} : {s}".format(i=i+1, s=state)
            
        return state

    @property
    def alphabet(self):
        return self._alphabet

    @property
    def axiom(self):
        return self._axiom

    @property
    def rules(self):
        return self._rules

# prefix grammar 
# regular grammar

class Alphabet(object):
    """
    A set of symbols containing both elements that can be replaced (variables)
    and those which cannot be replaced ("constants").
    """
    
    def __init__(self, variables, constants=""):

        self._variables = "".join(set(list(variables)))
        self._constants = "".join(set(list(constants)))

    def validate(self, symbols):
        for symbol in symbols:
            if not self.contains(symbol):
                raise ValueError(
                    "Invalid symbol '{s}' not found in alphabet '{a}'.".format(
                    s=symbol, a=alphabet)
                )

    def contains(self, symbol):
        return self.is_variable(symbol) or self.is_constant(symbol)

    def is_variable(self, symbol):
        return symbol in self.variables

    def is_constant(self, symbol):
        return symbol in self.constants

    @property
    def variables(self):
        return self._variables

    @property
    def constants(self):
        return self._constants

class Axiom(object):
    """
    A string of symbols from an Alphabet defining the initial state of the
    system.
    """

    def __init__(self, symbols):

        self._symbols = symbols

    @property
    def symbols(self):
        return self._symbols

class Rule(object):
    """
    A production rule defining the way variables can be replaced with 
    combinations of constants and other variables.
    """

    def __init__(self, predecessor, successor):
        
        self._predecessor = predecessor
        self._successor = successor

    @property
    def predecessor(self):
        return self._predecessor

    @property
    def successor(self):
        return self._successor 


if __name__ == "__main__":

    # ---------------------
    # Run the examples...
    # ---------------------

    # Example 1: Algae
    alphabet = Alphabet("AB")
    axiom = Axiom("A")
    rules = [
        Rule("A", "AB"),
        Rule("B", "A")
    ]

    print "\nAlgae"
    grammar = ContextFreeGrammar(alphabet, axiom, rules)
    grammar.generate(7)

    # ---------------------

    # Example 2: Pythagoras tree
    alphabet = Alphabet("01", "[]")
    axiom = Axiom("0")
    rules = [
        Rule("1", "11"),
        Rule("0", "1[0]0")
    ]

    print "\nPythagoras tree"
    grammar = ContextFreeGrammar(alphabet, axiom, rules)
    grammar.generate(3)

    # ---------------------

    # Example 3: Cantor dust
    alphabet = Alphabet("AB")
    axiom = Axiom("A")
    rules = [
        Rule("A", "ABA"),
        Rule("B", "BBB")
    ]

    print "\nCantor dust"
    grammar = ContextFreeGrammar(alphabet, axiom, rules)
    grammar.generate(3)

    # ---------------------

    # Example 4: Koch curve
    alphabet = Alphabet("F", "+-")
    axiom = Axiom("F")
    rules = [
        Rule("F", "F+F-F-F+F"),
    ]

    print "\nKoch curve"
    grammar = ContextFreeGrammar(alphabet, axiom, rules)
    grammar.generate(3)

    # ---------------------

    # Example 5: Sierpinski triangle
    alphabet = Alphabet("AB", "+-")
    axiom = Axiom("A")
    rules = [
        Rule("A", "+B-A-B+"),
        Rule("B", "-A+B+A-"),
    ]

    print "\nSierpinski triangle"
    grammar = ContextFreeGrammar(alphabet, axiom, rules)
    grammar.generate(3)

    # Sierpinski triangle (alt)
    alphabet = Alphabet("FG", "+-")
    axiom = Axiom("F-G-G")
    rules = [
        Rule("F", "F-G+F+G-F"),
        Rule("G", "GG"),
    ]

    print "\nSierpinski triangle (alt)"
    grammar = ContextFreeGrammar(alphabet, axiom, rules)
    grammar.generate(3)

    # ---------------------

    # Example 6: Dragon curve
    alphabet = Alphabet("XY", "F+-")
    axiom = Axiom("FX")
    rules = [
        Rule("X", "X+YF+"),
        Rule("Y", "-FX-Y"),
    ]

    print "\nDragon curve"
    grammar = ContextFreeGrammar(alphabet, axiom, rules)
    grammar.generate(3)

    # ---------------------

    # Example 7: Fractal plant 
    alphabet = Alphabet("XF", "+-[]")
    axiom = Axiom("X")
    rules = [
        Rule("X", "F-[[X]+X]+F[+FX]-X"),
        Rule("F", "FF"),
    ]

    print "\nFractal plant"
    grammar = ContextFreeGrammar(alphabet, axiom, rules)
    grammar.generate(3)


# TODO
#   * stochastic grammar 
#   * context sensitive grammar

