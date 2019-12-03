LRU-cache was realized on Python 3.8 with two different approaches:
1. By using `OrderedDict` from standard library `collections` is in folder _OrderedDict_. 
This solution is shorter and simpler for reading and maintaining.
2. By using standard Python dictionary is in folder _Dict_.
This solution does not depend on any library and can be used in a limited environment without extra libraries.  

Both solutions:
- Have comparable complexity, runtime and usage of memory.
- Designed as a child of `dict`/`OrderedDict` and can use methods of parent class.
- Do not use third-party libraries.
- Covered by unit-tests. 
Tests are developed with standard library `unittest` as a common tool for simple tests. 
Tests are located in the same folder as a solution does.   
Tests can be run with installed python-3 from command line  
`python -m unittest test_LRUCache_Dict.py` from folder _Dict_  
or  
`python -m unittest test_LRUCache_OrderedDict.py` from folder _OrderedDict_  
