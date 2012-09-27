Creating and modifying BibTeX styles
====================================
<a href="http://en.wikipedia.org/wiki/BibTeX">BibTeX</a> is an indispensable tool when you plan to manage a large document or will use the same references again in the future.

However, creating and modifying style files for it is extremely difficult.  It's in a strange postfix language, almost, but not quite, completely different from <a href="http://en.wikipedia.org/wiki/PostScript">PostScript</a>.  Should you ever have to do this, I recommend reading the BibTeX documentation (especially <code>btxhak</code>) found on <a href="http://www.tex.ac.uk/tex-archive/biblio/bibtex/distribs/doc/">here</a> on CTAN.

What this document doesn't tell you is how most style files actually work.  There is an important thing you need to know when modifying the standard style files: at the beginning of a style FUNCTION, you normally have two literals on your stack, which are the the last two strings of your bibliography entry that have been entered at this point.  For example, if you are modifying the title style function, the first thing you would pop out would be the title, and the second thing would probably be the author.

When modifying a style function, you need to do two things: <code>write$</code> the previous string with appropriate punctuation afterwards, leave the current string on the top of the stack, and update the state (usually in a variable like <code>output.state</code>) so that the next style function will know where it is in the entry.

As a quick example, I needed to add a parenthesis to a particular section of my bibliographic entries to comply with a style guide.  So I created the following function to set up the opening paren:

<pre>
FUNCTION {output.apunc}
{
  swap$
  " " * write$
  before.all 'output.state :=
}
</pre>

This simply takes the two parts of the stack, swaps them (so that we are now working with the previously output word), adds a space after it (with the <code>*</code> concatenation operation), and writes it.  It then sets the current state toe mean that we are at the beginning of a new "sentence".  You would call this function with

<pre>
"(" output.apunc
</pre>

In case you are curious, words between double quotes are string, words that end in a <code>$</code> are calling one of the few dozen built-in functions, words that start with a single quote indicate that you are passing the variable name, and anything else is either a function call or inserts the value of that variable on the stack.  This is why the first argument of the assignment operator needs to be single-quoted, so that the interpreter doesn't simply insert the value of the variable.