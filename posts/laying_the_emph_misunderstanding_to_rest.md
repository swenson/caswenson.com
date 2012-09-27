Laying the \emph misunderstanding to rest
=========================================
As a response to <a href="http://www.caswenson.com/?p=18">a previous post</a> regarding LaTeX's <code>\emph</code> command: I was under the impression that you need to still use the <code>\/</code> command afterward to do an italic correction: it turns out that you do <strong>not</strong> need to.

I verified this using the wonderul <code>\showbox</code> command in LaTeX: this spits out the contents of a box, including all characters and kerns.

Note: in order to use this command in LaTeX, you need to reset the <code>\showboxdepth</code> and <code>\showboxbreadth</code> counters, which are reset for some reason.  This can be done like so:

<pre lang="tex">\showboxdepth=100
\showboxbreadth=100</pre>

Thanks to <a href="http://uucode.com/blog/2006/02/26/showbox-in-latex/">Oleg</a> for this tip.

After I did this, I threw the following code in a LaTeX document (it has to be inside of a document, not the preamble, otherwise it won't load the fonts properly):

<pre lang="tex">\setbox122=\hbox{{\it i}i}
\showbox122
\setbox123=\hbox{\emph{i}i}
\showbox123</pre>

Then, checking the log file gave me:

<pre>> \box122=
\hbox(6.67859+0.0)x5.84444
.\OT1/cmr/m/it/10 i
.\OT1/cmr/m/n/10 i
 
 
! OK.
l.7 \showbox122
               
? 
> \box123=
\hbox(6.67859+0.0)x6.86339
.\OT1/cmr/m/it/10 i
.\kern 1.01895
.\OT1/cmr/m/n/10 i
 
! OK.
l.9 \showbox123</pre>

So, the <code>\emph</code> command automatically puts in the <code>\/</code> as necessary.  (I verified that it doesn't seem to insert this when it isn't needed.)