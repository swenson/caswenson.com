sliderepl for Sage
==================
<a href="http://discorporate.us/projects/sliderepl/">sliderepl</a> is a really neat Python presentation tool for demonstrating code, live, in a slide-like format.  Essentially, you organize your code into "slides", which you can then scroll through (though you can't go back, really).  The tool was written originally by <a href="http://discorporate.us/jek/">Jason Kirtland</a>.

I wanted to see if I could use it for <a href="http://www.sagemath.org">Sage</a> code as sort of a GUI-less notebook thing.  Kind of.  Unfortunately, sliderepl is full of hacky magic, involving embedding an interpreter and introspection.  Sage is too, and so they don't like each other very much.

Through some more magic, I figured out how to get them to work together anyway, and released the code on Github as <a href="http://github.com/swenson/sage_sliderepl">sage_sliderepl</a>.