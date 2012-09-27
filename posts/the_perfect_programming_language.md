The perfect programming language
================================
I've been doing a lot of programming lately, and in a multitude of different languages.  For the most part, these are pretty "decent" languages: C, Python, Ruby, etc.  However, none of the languages really makes me happy.

It's hard to define exactly what I mean by "happy".  They're all, for the most part, <a href="http://xkcd.com/353/">fun</a> to program in to various degrees.  But I don't really feel like I have all of the power at my fingertips in any of them.  For example:

<ul>
<li>Python is used for general purpose whatever.  It's powerful, easy to read, easy to write, and fast.</li>
<li>C is used for speed.  When I need to be screaming down the highway, I break down and code in C (perhaps callable in a higher-level language).</li>
<li>Ruby is used for much of my web development.</li>
</ul>

I don't really find Python that well-suited for web development, although I use it that way quite often, just as much as I find Ruby to be a bit odd at general purpose computing (say, doing a <a href="http://projecteuler.net/">Project Euler</a> problem).  And I don't really break out the C unless I have to.  It makes a two-week-long Python program turn into a three-month adventure in passing structs around.

Some people have commented that maybe what I need is C++, especially with the Boost libraries.  It's not as easy as Python, but not as ridiculous as C all the time.  And they may be right, but I'm not quite sold yet.

The primary reason for my displeasure with C++ is primarily two things.  First, it's syntax is stuck back <a href="http://en.wikipedia.org/wiki/B_(programming_language)">in 1969</a>.  Why do we need so many braces, so many semi-colons?  The overused and overloaded <tt>&</tt>, <tt>*</tt>, <tt>^</tt>, etc. operators really bother me, as they make things just so terse and ugly.  I mean, if I wanted to see a statement that looked like line noise, I'd use Perl or <a href="http://en.wikipedia.org/wiki/APL_(programming_language)#Examples">APL</a>.

Second, related to the above, C++ is extremely powerful and large, and it takes a long time to master.  I don't believe that languages should take a long time to master.

Which brings me to Ruby.  Ruby is not quite as bad as C++ in the long time to master, though it's still a far cry from Python.  And Ruby is <em>almost</em> what I need (I think it has some of the best syntax of any language ever), but it's still not quite there.

<ul>
<li>Ruby is <em>slow</em>.  I can't really compile it, and it has so many language features that really bog it down, not all of which I feel are necessary (see next bullet).</li>
<li>Ruby is weird.  Most people who have been exposed to OOP know what a class variable and an instance variable is, but what the hell is a <a href="http://railstips.org/2006/11/18/class-and-instance-variables-in-ruby">class instance</a> variable?  Reading through <a href="http://www.amazon.com/gp/product/0596516177?ie=UTF8&tag=mathfigu-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0596516177">The Ruby Programming Language</a><img src="http://www.assoc-amazon.com/e/ir?t=mathfigu-20&l=as2&o=1&a=0596516177" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> (which is a great book, btw), Ruby has a lot of really complicated things going on when doing variable and method name resolution involved with the myriad of different ways things are inherited.  It bothers me a lot.</li>
<li>Ruby makes it worse by attempting to explicitly declare the scope of a variable with var, $var, @var, @@var.  Often, this just makes things worse.</li>
</ul>

So, Ruby isn't quite there.

Python?  Well, it's much faster (an order of magnitude or thereabouts).  It doesn't have a lot of weird inheritance issues (only some).

My biggest problem is the direction that Python is taking with Python 3.0.  Changing <tt>map()</tt> and friends to return iterators?  Making <tt>print</tt> a function?  Further confusing me regard to <a href="http://docs.python.org/dev/3.0/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit">text vs. unicode vs. data vs. bytes vs. strings vs. regular expressions</a>?   <a href="http://docs.python.org/dev/3.0/whatsnew/3.0.html">And so forth.</a>

And even syntactically there are problems: Why are there colons at the end of def/if/for/... statements?  And is it really necessary to have syntactically important whitespace?  I don't mind it, but a lot of people hate this with a passion.

So, what I need is a language that can be compiled (and run at great speeds), with Ruby-like syntax, and a Python-like typing and object model.

That would be nice, thank you.

<hr />

<small>And yes, if I get some time, I might consider forking a project related to one of the above to get what I want.</small>