# make interpreter logo tokens using parsley
# http://parsley.readthedocs.org/en/latest/
import parsley
from parsley import makeGrammar

grammar = r"""
    punctuation = :x ?(x in "+-*/!'#$%&\,.:<=>?@^_`;" '"') -> x
    float = <'-'{0, 1} digit* '.' digit+>:ds -> float(ds)
    integer = <'-'{0, 1} digit+>:ds -> int(ds)
    number = float | integer
    parens = '(' ws expr:e ws ')' -> e
    value = (number:n ->n) | (parens:p -> p)
    
    term = value:v ws (punctuation:p ws value:v ws -> (p, v))*
    expr = term:t ws (punctuation:p ws term:t ws -> (p, t))*
    start = expr:e -> e
    """

g = parsley.makeGrammar(grammar, {})
print(g("+").punctuation())