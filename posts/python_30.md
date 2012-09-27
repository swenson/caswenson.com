Python 3.0
==========
There are lots of things I dislike about Python 3.0.  I dislike the removal of the <code>print</code> statement (I would have much preferred allowing Ruby-like function calling without parenthesis, and transparently changing the statement to a function).  I dislike the fact that <code>map</code> and friends return iterators instead of, you know, mapping things.

And why don't they include a Mac OS X installer?

Well, for you Mac OS X users, it's still pretty easy to install from source.  Merely download the source, and run a series of commands like so:

<pre>tar xvjf Python-3.0.tar.bz2
cd Python-3.0
./configure --enable-framework --enable-shared
make
sudo make install
</pre>

Be a little careful, though, as it will will overwrite <code>/Library/Frameworks/Python.framework/Versions/Current</code> with 3.0, so you may need to take some measures to use your older versions of Python (though you should hopefully be able to execute them by just calling them with a version number, like <code>python2.5</code>).  YMMV.



Also, I really hate the name "Python 3000".