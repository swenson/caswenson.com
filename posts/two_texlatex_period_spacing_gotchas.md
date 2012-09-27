Two TeX/LaTeX period spacing gotchas
====================================
An easy thing to forget about TeX is that it tries to guess what you mean, and can get it wrong.  In this case, I am talking about periods.

TeX interprets a period based on the previous letter.  If the previous letter is a capital, like "D. Knuth", it puts a normal space in, thinking that you are giving an initial.  If it is lowercase, like "I went to the store.  It was nice", it assumes you meant a period that ends a sentence, which has about 1 to 1.5 spaces after it (depending on the justification needs and the style settings you prefer).

But what if you have a sentence that ends with, say, "which is why I like NINJAS."  Here, the period ends a sentence.  Or how about, "all of the misc. tools", where the period doesn't?

A quick way to check to see if you made an oops doing this in your source file is to run the two scripts:

<pre lang="bash">grep "[A-Z]\. " *.tex</pre>
This checks for the first case, while this:
<pre lang="bash">grep "[a-z]\. [a-z]" *.tex</pre>
checks for the second case.

To fix the case with the capital and the period, change "<code>NINJAS. </code>" to "<code>NINJAS\@. </code>", to tell TeX to treat the period as a sentence stopper.

For the other case, with the lowercase and the period, change "<code>misc. tools</code>" to "<code>misc.\ tools</code>", to tell TeX to treat it as a normal space.

I strongly recommend that anyone who uses TeX or LaTeX should, at some point, read <a href="http://www.amazon.com/gp/product/0201134489?ie=UTF8&tag=mathfigu-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0201134489">The TeXbook</a><img src="http://www.assoc-amazon.com/e/ir?t=mathfigu-20&l=as2&o=1&a=0201134489" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />, by Donald Knuth, and find out what really goes on under the hood.

Thanks to <a href="http://john.regehr.org/latex/">John</a> for giving one of the scripts and reminding me of this.