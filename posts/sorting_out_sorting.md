Sorting out sorting
===================
I <a href="http://github.com/swenson/sort">recently wrote</a> a C version of a bunch of comparison-based sorting algorithms, notably timsort and quicksort.

<a href="http://en.wikipedia.org/wiki/Timsort">Timsort</a> is a neat, unbalanced mergesort that I've been wanting to try out for the past while, and so I spent the time to write a fast C implementation of the algorithm.  My experiments on random data show about a 5-10% improvement over quicksort, which is pretty amazing.  If the data has any structure, which is extremely common, it has "superhuman" performance, as it can merge natural runs in the data in an efficient manner.

Another annoying thing I've noticed is that I've written the same sorting algorithms a ton of times, often just changing the type.  Sometimes I've used the standard C <a href="http://fxr.watson.org/fxr/source/stdlib/qsort.c?v=GLIBC27">qsort</a>, but the function-pointer comparison function causes awful performance (the version I wrote isn't even as optimized, and is still often twice as fast).  Why can't I just write a good, fast sorting algorithm?

A solution comes from a neat trick in C: <a href="http://en.wikipedia.org/wiki/C_preprocessor#Token_concatenation">token pasting</a>.  Using this, it's possible to write the function once, and just swap out the types as needed.

Using token pasting, it is also possible to implement the entire library as a single header file: no library to compile!

Sadly, sorting doesn't usually have <a href="http://www.youtube.com/watch?v=YvTW7341kpA">sound effects</a>.