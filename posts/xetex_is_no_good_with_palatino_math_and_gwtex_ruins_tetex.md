XeTeX is no good with Palatino math, and gwTeX ruins teTeX.
===========================================================
So I determined, after several hours over the last few days, that <a href="http://scripts.sil.org/XeTeX">XeTeX</a> just <strong>will not</strong> have anything to do with Palatino math fonts.  I even tried an experimental <code>unicode-math</code> package.  Absolutely nothing seems to be able to get the two to work together: the <code>fontspec</code> package seems to make it ignore the <code>mathpazo</code> and <code>pxfonts</code> package, no matter where they come in the preamble.

I decided to give up, and go back to plain LaTeX with the <code>pxfonts</code> package.  This stinks, because I really like the Unicode support and the hassle-free way of selecting text fonts.

There is also another lesson I learned: having Fink teTeX, the old MacTeX teTeX, as well as the new LiveCD 2007 version of gwTeX installed on the same Mac will cause great confusion, and many lost fonts.  I decided to wipe all three installations, and install the actual full MacTeX 2007 distribution, which cleaned up some of the mess going on.