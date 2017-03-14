This repo contains Python ports of the code listings from [Clever
Algorithms](http://www.cleveralgorithms.com). It is one of those rare books
which tackle theory and yet present the reader with working code. How I wish
more books were written like this.

The book has its own [GitHub
repo](https://github.com/jbrownlee/CleverAlgorithms), utilizing Ruby.

# Status

This is pretty much a **work-in-progress**. What I'm currently working on is
verifying that the Ruby and the Python code listings encode the same algorithms.
I may add new listings here and there but coming up with a framework to verify
this is my main concern right now.

# File Organization

First of all, note that this repository
isn't synchronized with [the main Clever Algorithms
repository](https://github.com/jbrownlee/CleverAlgorithms). My main purpose
is in learning the algorithms in the book and transcribing them to Python;
I've come to believe that implementing algorithms on your own is a good
learning exercise. I'm taking the Ruby listings as pseudocode that is also
the reference implementation. In the process, I hope to familiarize myself
with the algorithms and Ruby.

So, all directories, save for `python`, are not to be taken as updated.

Under the `python` directory, the code listings are sorted by chapter and are
named after the name used by the book (e.g., Random Search of Chapter 2 is
`python/2_Stochastic_Algorithms/random_search.py`). At the beginning of each
file, I note the chapter and section in the book in which the algorithm can
be found (e.g., Random Search is noted as 2.2). The docstring also contains
a description the algorithm and some notes on the code listing itself. These
were taken directly from the book, unless noted.

# Technical Specs

All Python codes will be for (plain) Python 3.

# Miscellaneous

There are [Python versions](http://code.google.com/p/aima-python/) of
the pseudocodes in Russel and Norvig's _Artificial Intelligence: A Modern
Approach_. There are also listings for other languages as well as a standard
data set at the [book's official site](http://aima.cs.berkeley.edu/code.html).
