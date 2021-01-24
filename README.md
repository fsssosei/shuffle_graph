# shuffle_graph

![PyPI](https://img.shields.io/pypi/v/shuffle_graph?color=red)
![PyPI - Status](https://img.shields.io/pypi/status/shuffle_graph)
![GitHub Release Date](https://img.shields.io/github/release-date/fsssosei/shuffle_graph)
[![Build Status](https://scrutinizer-ci.com/g/fsssosei/shuffle_graph/badges/build.png?b=master)](https://scrutinizer-ci.com/g/fsssosei/shuffle_graph/build-status/master)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/fsssosei/shuffle_graph/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/fsssosei/shuffle_graph.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/fsssosei/shuffle_graph/context:python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/eee9f9c7d45a49808774f88351942b7b)](https://www.codacy.com/manual/fsssosei/shuffle_graph?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fsssosei/shuffle_graph&amp;utm_campaign=Badge_Grade)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/fsssosei/shuffle_graph/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/fsssosei/shuffle_graph/?branch=master)
![PyPI - Downloads](https://img.shields.io/pypi/dw/shuffle_graph?label=PyPI%20-%20Downloads)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/shuffle_graph)
![PyPI - License](https://img.shields.io/pypi/l/shuffle_graph)

*Graph shuffling package in python.*

## Installation

Installation can be done through pip. You must have python version >= 3.8

	pip install shuffle-graph

## Usage

The statement to import the package:

	from shuffle_graph_package import *
	
Example:

	>>> from networkx.classes.graph import Graph
	>>> G = Graph({0: {1: {}}, 1: {0: {}, 2: {}}, 2: {1: {}, 3: {}}, 3: {2: {}, 4: {}}, 4: {3: {}}})
	>>> seed = 170141183460469231731687303715884105727
	>>> shuffle_graph(G, seed).adj  #Set seed to make the results repeatable.
	AdjacencyView({1: {0: {}, 2: {}}, 2: {1: {}, 3: {}}, 3: {2: {}, 4: {}}, 4: {3: {}}, 0: {1: {}}})
