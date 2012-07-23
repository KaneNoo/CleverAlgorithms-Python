**Status:** Work-in-progress

This repo contains Python ports of the code listings from [Clever Algorithms](www.cleveralgorithms.com). It is one of those rare books which tackle theory and yet present the reader with working code. How I wish more books were written like this.

The book has its own [GitHub repo](https://github.com/jbrownlee/CleverAlgorithms), utilizing Ruby.

# File Organization

First of all, note that this repository isn't synchronized with [the main Clever Algorithms repository](https://github.com/jbrownlee/CleverAlgorithms). My main purpose is in learning the algorithms in the book and transcribing them to Python; I've come to believe that implementing algorithms on your own is a good learning exercise. I'm taking the Ruby listings as pseudocode that is also the reference implementation.

So, all directories, save for `python`, are not to be taken as updated.

Under the `python` directory, the code listings are sorted by chapter and are named after the name used by the book (e.g., Random Search of Chapter 2 is `python/2 Stochastic Algorithms/random_search.py`). At the beginning of each file is a docstring describing the algorithm and some notes on the code listing itself. These were taken directly from the book, unless noted.

# Technical Specs

All Python codes will be for (plain) Python 3.1.2 .

# Miscellaneous

There are [Python versions](http://code.google.com/p/aima-python/) of the pseudocodes in Russel and Norvig's _Artificial Intelligence: A Modern Approach_. There are also listings for other languages as well as a standard data set at the [book's official site](http://aima.cs.berkeley.edu/code.html).
