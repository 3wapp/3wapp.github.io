---
title: "Iterators"
date: 2016-04-19 19:13
---

## 0x01 Itertools

[PYTHON进阶 ITERTOOLS模块小结][1]

[python docs itertools][2]

### Infinite Iterators

无限迭代

```
count(10, 1) --> 10 11 12 13 14 ...
cycle('ABCD') --> A B C D A B C D ...
repeat(3) --> 3 3 3 3 ...   repeat(4, 3) --> 3 3 3
```

### Iterators terminating on the shortest input sequence

处理输入迭代

```python
chain('ABC', 'DEF') --> A B C D E F
compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1         # 跳过头部符合条件的元素
takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4           # 保留头部符合条件的元素
groupby(['aa', 'abc', 'abcd', 'ab', 'ccf'], len) --> ['aa', 'ab'] ['abc', 'ccf'] ['abcd']	 
ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
islice('ABCDEFG', 2, None) --> C D E F G
imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
tee()	it, n	it1, it2, ... itn splits one iterator into n	 
izip('ABCD', 'xy') --> Ax By
izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
```

### Combinatoric generators

组合生成

```
product('ABCD', repeat=2)	AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2)	 	AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2)	 	AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2) --> AA AB AC AD BB BC BD CC CD DD
```

* chain

> chain(*iterables) --> chain object

Return a chain object whose .next() method returns elements from the
first iterable until it is exhausted, then elements from the next
iterable, until all of the iterables are exhausted.

* combinations

> combinations(iterable, r) --> combinations object

Return successive r-length combinations of elements in the iterable.

```
combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
```

* combinations_with_replacement

> combinations_with_replacement(iterable, r) --> combinations_with_replacement object

Return successive r-length combinations of elements in the iterable
allowing individual elements to have successive repeats.

```
combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
```

* compress

> compress(data, selectors) --> iterator over selected data

Return data elements corresponding to true selector elements.
Forms a shorter iterator from selected data elements using the
selectors to choose the data elements.

* count

> count(start=0, step=1) --> count object

Return a count object whose .next() method returns consecutive values.

Equivalent to:

```
    def count(firstval=0, step=1):
        x = firstval
        while 1:
            yield x
            x += step
```

* cycle

> cycle(iterable) --> cycle object

Return elements from the iterable until it is exhausted.
Then repeat the sequence indefinitely.

* dropwhile

> dropwhile(predicate, iterable) --> dropwhile object

Drop items from the iterable while predicate(item) is true.
Afterwards, return every element until the iterable is exhausted.

* groupby

> groupby(iterable[, keyfunc]) -> create an iterator which returns
> (key, sub-iterator) grouped by each value of key(value).

* ifilter

> ifilter(function or None, sequence) --> ifilter object

Return those items of sequence for which function(item) is true.
If function is None, return the items that are true.

* ifilterfalse

> ifilterfalse(function or None, sequence) --> ifilterfalse object

Return those items of sequence for which function(item) is false.
If function is None, return the items that are false.

* imap

> imap(func, *iterables) --> imap object

Make an iterator that computes the function using arguments from
each of the iterables.  Like map() except that it returns
an iterator instead of a list and that it stops when the shortest
iterable is exhausted instead of filling in None for shorter
iterables.

* islice

> islice(iterable, [start,] stop [, step]) --> islice object

Return an iterator whose next() method returns selected values from an
iterable.  If start is specified, will skip all preceding elements;
otherwise, start defaults to zero.  Step defaults to one.  If
specified as another value, step determines how many values are 
skipped between successive calls.  Works like a slice() on a list
but returns an iterator.

* izip

> izip(iter1 [,iter2 [...]]) --> izip object

Return a izip object whose .next() method returns a tuple where
the i-th element comes from the i-th iterable argument.  The .next()
method continues until the shortest iterable in the argument sequence
is exhausted and then it raises StopIteration.  Works like the zip()
function but consumes less memory by returning an iterator instead of
a list.

* izip_longest

> izip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> izip_longest object

Return an izip_longest object whose .next() method returns a tuple where
the i-th element comes from the i-th iterable argument.  The .next()
method continues until the longest iterable in the argument sequence
is exhausted and then it raises StopIteration.  When the shorter iterables
are exhausted, the fillvalue is substituted in their place.  The fillvalue
defaults to None or can be specified by a keyword argument.

* permutations

> permutations(iterable[, r]) --> permutations object

Return successive r-length permutations of elements in the iterable.

```
permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)
```

* product

> product(*iterables) --> product object

Cartesian product of input iterables.  Equivalent to nested for-loops.

For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
The leftmost iterators are in the outermost for-loop, so the output tuples
cycle in a manner similar to an odometer (with the rightmost element changing
on every iteration).

To compute the product of an iterable with itself, specify the number
of repetitions with the optional repeat keyword argument. For example,
product(A, repeat=4) means the same as product(A, A, A, A).

```
product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...
```

* repeat

> repeat(object [,times]) -> create an iterator which returns the object

for the specified number of times.  If not specified, returns the object
endlessly.

* starmap

> starmap(function, sequence) --> starmap object

Return an iterator whose values are returned from the function evaluated
with an argument tuple taken from the given sequence.

* takewhile

> takewhile(predicate, iterable) --> takewhile object

Return successive entries from an iterable as long as the 
predicate evaluates to true for each entry.

* tee 

> tee(iterable, n=2) --> tuple of n independent iterators.

[1]: http://www.wklken.me/posts/2013/08/20/python-extra-itertools.html
[2]: https://docs.python.org/2/library/itertools.html
 
