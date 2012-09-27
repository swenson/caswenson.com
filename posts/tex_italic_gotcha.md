TeX Italic Gotcha
=================
As an epilogue to the previous post, there is another common gotcha of TeX (and LaTeX).  Immediately after using italic or slanted text (such as with <code>\emph</code>, <code>\it</code>, <code>\sl</code>, etc.), TeX will put in a standard space.  However, the italic or slant from the previous letter will stick out, making the next (roman, or whatever) text be too close to the previous.  The fix is to insert an italic correction space, <code>\/</code>, immediately after italic text.

To catch yourself accidentally not doing this, run the following:

<pre lang="bash">grep "\\emph{.*} " *.tex</pre>