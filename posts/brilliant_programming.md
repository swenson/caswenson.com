Brilliant programming
=====================
Often, I like to read articles on particularly insightful programming techniques or algorithms.  Sometimes these algorithms are for some fairly mundane things, like searching and sorting.  (So mundane, of course, that Knuth wrote a <a href="http://www.amazon.com/gp/product/0201896850?ie=UTF8&tag=mathfigu-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0201896850">whole book</a><img src="http://www.assoc-amazon.com/e/ir?t=mathfigu-20&l=as2&o=1&a=0201896850" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> about it.)

Two pieces I have enjoyed recently.

First, <a href="http://bugs.python.org/file4451/timsort.txt">timsort</a> &ndash; the sorting algorithm used by Python.  It describes an interesting approach to mergesort that is stable and incredibly fast, especially for "almost" sorted arrays.

Second is a class: <tt><a href="http://sources.redhat.com/cgi-bin/cvsweb.cgi/libc/string/strlen.c?cvsroot=glibc&rev=1.1.2.1">strlen()</a></tt>, from glibc.  <tt>strlen()</tt>, for you non-C programmers, finds the length of a null-terminated string.  So, simply, given a location in memory, it finds the next zero byte.  Sounds easy?  Well, it is, but there are several tricks you can to do speed up the search by quite a bit.

Any other favorite snippets of code out there?