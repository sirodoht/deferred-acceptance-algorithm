# Deferred Acceptance algorithm

> The deferred acceptance algorithm, also known as the Gale–Shapley algorithm or
propose-and-reject algorithm, is an algorithm for finding a solution to the
[stable matching problem](https://en.wikipedia.org/wiki/Stable_marriage_problem),
named for David Gale and Lloyd Shapley.

> It takes polynomial time, and the time is linear in the size of the input to
the algorithm. It is a truthful
([strategyproof](https://en.wikipedia.org/wiki/Strategyproofness))
mechanism from the point of view of the proposing participants (women in our
example), for whom the solution will always be optimal (but not from the point
of view of the accepting/rejecting participants (men in our example).

— Wikipedia: https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm

[deferred-acceptance.ipynb](deferred-acceptance.ipynb) is a Jupyter notebook,
which goes through a non-optimised and easy to reason implementation of the
algorithm, with 8+8 men and women as a demo application.

[simple_implementation.py](simple_implementation.py) is the same implementation
from the jupyter notebook but with a 3+3 persons demo application, easier to
reason about when implementing it.

[library_implementation.py](library_implementation.py) is a demo application
using the [matching](https://daffidwilde.github.io/matching/) Python library,
which implements the deferred acceptance algorithm.

[optimised_implementation.py](optimised_implementation.py) is the implementation
that the matching library uses but made easier to understand when reading it,
with an example application of 3+3 persons.

## License

MIT
