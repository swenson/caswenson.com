Some rules of typesetting
=========================
Often when reading articles or books, there are several problems that can be easily corrected that detract from the work's aesthetic appeal.


<b>Don't use vertical rules.</b> In typesetting, a rule is a line.  The standard LaTeX <code>tabular</code> structure encourages us to use such monstrosities as <code>\begin{tabular}{|c|c|}</code>, putting vertical rules between every column.  This is often an amateur mistake of typesetting: seldom do professionally typeset works contain vertical rules.

<b>Use thicker rules, and vary the thickness in tables.</b> The standard size for a rule should be 1pt.  Lines that are too think just look weak.  A nice thick, but not too thick, rule will give it a more professional, feeling.  When doing tables, having even thicker rules for the top and bottom of the table, and medium thicknesses elsewhere add elegance to the table.  The LaTeX package <code>booktabs</code> gives the appropriate commands <code>\toprule</code>, <code>\midrule</code>, and <code>\bottomrule</code>.

<b>Use fixed-width fonts for code, email address, web address, and file names.</b> In books, we should never see "Email address: a@b.com" or "Open the file readme.1st".  It's infinitely better to use "Email address: <code>a@b.com</code>" and "Open the file <code>readme.1st</code>".  And while you're at it, stop saying "e-mail".  <a href="http://www-cs-faculty.stanford.edu/~knuth/email.html">There is no hyphen.  It's "email".</a>

<b>Either indent your paragraphs, or add a line space between them.</b> But please, please, you cannot have no spacing between your paragraphs, and not indent.

<br />

Therere are plenty more rules that I could write.  Once you develop an eye for this stuff, these patterns will just fall into place.  If in doubt, consult a good style manual (<a href="http://www.amazon.com/gp/product/0226104036?ie=UTF8&tag=mathfigu-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0226104036">The Chicago Manual of Style</a><img src="http://www.assoc-amazon.com/e/ir?t=mathfigu-20&l=as2&o=1&a=0226104036" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> is always my preference), or even just read through a professionally-typeset book to see how they addressed that typesetting issue.  Often, books written before digital typesetting are good for this, when professional typesetters were used to make the books.  Avoid self-published books (vanity presses) like the plague though.  I have seen these come out with the body text in Arial, and most of the diagrams drawn in MS Paint.  Although I left it unspoken before, Arial is inappropriate to use for the body text of a book or article, and MS Paint is pretty much never acceptable as a tool for creating professional graphics.