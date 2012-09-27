Some scipy stuff
================
It's been quiet here lately.  I've had a lot of projects going on that occupy most of my time in the evenings and on weekends.

One of these is a new blog I will be writing for, so expect news of that in the next few days.  I've been putting together a chapter for a book, working on my dissertation, working on new web sites, and a whole slew of other activities.

Once some of this stuff starts taking off (and out of my plate), I will have more time to post.

<hr />

So, I want this post to have some meat.  Well, one of the things that has been occupying my time lately has been programming things for my dissertation, particularly in Python using <a href="http://www.scipy.org/">scipy</a>.

Scipy is great.  What is not so great about it is two-fold: everyone else uses MATLAB (or the free alternative, <a href="http://www.gnu.org/software/octave/">GNU Octave</a>), and there is practically no documentation on scipy.  Scipy has a bunch of packages that emulate various toolboxes from MATLAB, but what makes matters worse is that sometimes it doesn't implement all of a package, or it implements it strangely.

How so?  Well, MATLAB doesn't differentiate between a 1x1 matrix and a number, and you can use them interchangeably.  Scipy is much more strictly typed, and you can't just mix and match.  Nor can you mix and match complex numbers, reals, etc.  Also, MATLAB numbers all lists, matrices, etc., starting with 1, and scipy use's Python's conventions of starting with 0.  This makes a lot of MATLAB example code you for something you are doing annoying to port over to scipy.

One great resource for this is <a href="http://www.scipy.org/NumPy_for_Matlab_Users">NumPy for Matlab Users</a>.  Not only does this tell you how to convert many common MATLAB operations to scipy, but it gives you an idea of what you <em>can</em> do with scipy.

Both tools are excellent, if a little difficult to get working on Mac OS X.

<hr />

A quick tip for MATLAB users: MATLAB has a great function for <a href="http://en.wikipedia.org/wiki/Cross-correlation">cross correlation</a>, called <code>xcorr</code>.  The scipy.signal package includes a function, <code>correlate</code>, that is almost, but not quite, completely incompatible with the <code>xcorr</code> function.  So, I reimplemented the MATLAB <code>xcorr</code> in Python, as follows:

<pre name="code" class="python">
def matlab_xcorr(x, yy = None):
  # if no y, compute the autocorrelation of x
  y = yy
  if y == None:
    y = x
 
  n = len(x)
  c = zeros(2 * n - 1, complex)
  for m in range(1, 2 * n):
    c[m - 1] = cxy(x, y, m - n)
 
  return c
</pre>

Hopefully someone might find this useful, if they are suddenly frustrated by the lack of <code>xcorr</code> in scipy.

BTW, I recently switched to writing Python code <a href="http://panela.blog-city.com/python_at_google_greg_stein__sdforum.htm">Google-style</a>, and have never looked back.