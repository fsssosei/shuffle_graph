# shuffle_graph

![PyPI](https://img.shields.io/pypi/v/count-dict?color=red)
![PyPI - Status](https://img.shields.io/pypi/status/count-dict)
![GitHub Release Date](https://img.shields.io/github/release-date/fsssosei/count_dict)
[![Build Status](https://scrutinizer-ci.com/g/fsssosei/count_dict/badges/build.png?b=master)](https://scrutinizer-ci.com/g/fsssosei/count_dict/build-status/master)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/fsssosei/count_dict/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/fsssosei/count_dict.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/fsssosei/count_dict/context:python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bf34f8d12be84b4492a5a3709df0aae5)](https://www.codacy.com/manual/fsssosei/count_dict?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fsssosei/count_dict&amp;utm_campaign=Badge_Grade)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/fsssosei/count_dict/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/fsssosei/count_dict/?branch=master)
![PyPI - Downloads](https://img.shields.io/pypi/dw/count-dict?label=PyPI%20-%20Downloads)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/count-dict)
![PyPI - License](https://img.shields.io/pypi/l/count-dict)

*Adaptive overlapping community discovery algorithm package in python.*

*Welcome to complete the documentation.*

## Installation

Installation can be done through pip. You must have python version >= 3.6.

	pip install shuffle-graph

## Usage

The statement to import the package:

	from shuffle_graph_package import shuffle_graph

or

	from shuffle_graph_package import *
	
Example:

	>>> calculate_number_of_shuffles_required_under_default_random_function(10000)
	6


	>>> G = Graph({0: {1: {}}, 1: {0: {}, 2: {}}, 2: {1: {}, 3: {}}, 3: {2: {}, 4: {}}, 4: {3: {}}})
	>>> shuffle_graph(G, 1, 65535).adj  #Set seed to make the results repeatable.
	AdjacencyView({3: {2: {}, 4: {}}, 4: {3: {}}, 1: {0: {}, 2: {}}, 2: {3: {}, 1: {}}, 0: {1: {}}})
