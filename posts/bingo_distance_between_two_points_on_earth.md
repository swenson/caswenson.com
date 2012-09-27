Bingo!  Distance between two points on Earth
============================================
As a follow-up to my previous post, I have found two ways of finding the distance between two cities in the US.  One is slow and more correct, one is less slow and less correct.

First, the slow one.  You can take the third formula from the Wikipedia entry for <a href="http://en.wikipedia.org/wiki/Great-circle_distance#Formulas">finding the great-circle distance</a>.  It translates pretty naturally into any language, but involves many trigonometric functions, squares, square roots, etc.  It's quite ugly an inelegant in code, and quite slow.

In Ruby, it looks something like this (the <code>lat</code> and <code>rlat</code> accessors return the latitude in degrees and radians, respectively, and similarly for longitude with <code>lon</code> and <code>rlon</code>).

<pre name="code" class="ruby">  def distance_miles_slow(other)
    3956.54938 * Math.atan2(Math.sqrt((Math.cos(other.rlat) *
        Math.sin(other.rlon - rlon)) ** 2 +
      (Math.cos(rlat) * Math.sin(other.rlat) - Math.sin(rlat) *
        Math.cos(other.rlat) * Math.cos(other.rlon - rlon)) ** 2),
      (Math.sin(rlat) * Math.sin(other.rlat) + Math.cos(rlat) *
        Math.cos(other.rlat) * Math.cos(other.rlon - rlon)))
  end</pre>

Ugh.

It turns out that my naïve method of simply using the Pythagorean theorem after finding the "linear" distance in latitude and longitude (from <a href="http://en.wikipedia.org/wiki/Geographic_coordinate_system#Expressing_latitude_and_longitude_as_linear_units">here</a>) is actually pretty good.  Not as accurate, as the rougher figures seem to be off by about 2% at moderate distances (less than 1,000 miles), which is good enough for me at the moment.

Here's what the Ruby for that look like:

<pre name="code" class="ruby">  def distance_miles_fast(other)
    dlat = lat - other.lat
    drlon = rlon - other.rlon
    Math.sqrt((68.9100652 * dlat)**2 +
      (drlon * 3956.54938 * Math.cos(rlat))**2)
  end</pre>

A little bit better, and at least a bit faster.