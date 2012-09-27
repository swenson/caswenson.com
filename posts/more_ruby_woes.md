More Ruby Woes
==============
I have been giving Ruby the old college try.  I was running into some strange difficulties with a minimax function in Ruby that at first I thought were more scoping oddities.

It turns out that the <code>clone</code> and <code>dup</code> operators on Arrays in Ruby only perform shallow copying, which will pretty much not work on multidimensional arrays.  Oh well, I guess I would have to write my own, or copy someone else's, right?  Maybe something like:

<pre lang="ruby">def deepcopy(x)
  if x.kind_of? Array
    copy = []
    x.each { |y|  copy += [deepcopy(y)] }
    return copy
  else
    return x.dup
  end
end</pre>

<strong>Wrong</strong>.  Ruby's almost-but-not-quite pure-OO nature actually makes it nearly impossible to create a generic deep copy function.  The problem is that integers, floats, and so forth are not the complete objects we thought they were, because you can't <code>dup</code> them:

<pre>>> x = 1.dup
TypeError: can't dup Fixnum
	from (irb):1:in `dup'
	from (irb):1</pre>

So much for pure OO.

The best solution I could come up with for a two-deep copy is (knowing ahead of time that it is a matrix):

<pre lang="ruby">def copy2(b)
	newb = []
	b.each { |r|  newb += [r.dup] }
	return newb
end</pre>

This, along with the odd scoping rules and counter-intuitive syntax are making me seriously consider ending my Ruby experiment.  And I so wanted to love Ruby.