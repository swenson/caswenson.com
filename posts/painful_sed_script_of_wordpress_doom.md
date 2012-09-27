Painful sed script of Wordpress doom
====================================
So, I figured out most of the problems, and how to solve them.

Problem one: pasting text from Word stores the document in <a href="http://en.wikipedia.org/wiki/Windows-1252">Windows-1252</a> encoding.

Problem two: this is stored in MySQL, by default, in the deceptively-similar-to-but-incompatible-with-1252 <a href="http://en.wikipedia.org/wiki/ISO/IEC_8859-1">ISO-8859-1</a> encoding.

Problem three: Wordpress is smart, and automatically converts 1252 into HTML entities, which hides the problem until you dump the database.

Problem four: <a href="http://en.wikipedia.org/wiki/Utf-8">UTF-8</a> is freely intermingled with 1252 text in the entries.

Problem five: Windows does really weird things to encode non-1252 characters (like <a href="http://en.wikipedia.org/wiki/Smart_quotes">smart quotes</a>) in a 1252 character stream.

Problem six: Some piece of software went wrong at some point (probably PHP or phpMyAdmin) , and converted the 1252, non-1252 weird smart quotes, ISO-8859-1, and UTF-8 codes to UTF-8 (by converting the byte literal values instead of the underlying characters, which for UTF-8 codes means that you have to decode twice to get the real answer), but MySQL keeps the text marked as ISO-8859-1.

Problem seven: you are me, and you have 2,300 of these invalid characters in a MySQL dump that needs to be imported.

Problem eight: Mac OS X, by default, uses a sub-standard version of <a href="http://www.gnu.org/software/sed/">sed</a> that does not support replacement of literal values (<code>"\xC2"</code>, for example), making it impossible to replace any non-ASCII characters.

Solution: install sed from <a href="http://finkproject.org/">Fink</a>, and run the following sed script on your MySQL dump:

<pre>
s/DEFAULT CHARSET=latin1/DEFAULT CHARSET=utf8/g
s/\xc3\xa2\xe2\x82\xac\xe2\x84\xa2/\&amp;rsquo;/g
s/\xc3\xa2\xe2\x82\xac\xe2\x80\x9d/\&amp;mdash;/g
s/\xE2\x80\x9C/\&amp;ndash;/g
s/\xc3\xa2\xe2\x82\xac\xc2\xa2/\&amp;bull;/g
s/\xC3\xA2\xE2\x82\xAC\xC5\x93/\&amp;ldquo;/g
s/\xC3\xA2\xE2\x82\xAC\xC2\x9D/\&amp;rdquo;/g
s/\xC3\xA2\xE2\x82\xAC\xC2\x9C/\&amp;lsquo;/g
s/\xC3\xA2\xE2\x82\xAC/\&amp;rdquo;/g
s/\xC3\x85\xE2\x80\x99/\&amp;lsquo;/g
s/\xc3\x82\xc2\xba/\&amp;deg;/g
s/\xC3\x82\xC2\xA9/\&amp;copy;/g
s/\xc3\xa2\xC2\xA6/\&amp;hellip;/g
s/\xC3\x82\xC2\xA3/\&amp;pound;/g
s/\xC3\x83\xC2\xA3/\&amp;aacute;/g
s/\xc3\x83\xc2\xa1/\&amp;aacute;/g
s/\xC3\x83\xC2\xA8/\&amp;egrave;/g
s/\xC3\x83\xC2\xA9/\&amp;eacute;/g
s/\xC3\x83\xC2\xA7/\&amp;ccedil;/g
s/\xc3\x82\xc2\xae/\&amp;reg;/g
s/\xc3\x83\xc2\x81/\&amp;Aacute;/g
s/\xc3\x83\xc2\xab/\&amp;euml;/g
s/\xc3\x82\xc2\xbd/\&amp;frac12;/g
s/\xc3\x82\xc2\xbc/\&amp;frac14;/g
s/\xc3\xa2\xe2\x80\x9e\xc2\xa2/\&amp;trade;/g
s/\xc2\xbf//g
s/\xc2\xa0/\&amp;nbsp;/g
s/\xc3\x82\xc2\xb9/\&amp;#185;/g
s/\xc3\x82\xc2\xb0/\&amp;deg;/g
s/\xc3\x82\xc2\xab/\&amp;laquo;/g
s/\xc3\x83\xc2\xb6/\&amp;ouml;/g
</pre>

This removes all but 30 of my invalid characters, and those remaining ones appear to be pretty much broke (viewing the original articles shows garbage, and there is no logical character that would fit in those places).  Good enough.