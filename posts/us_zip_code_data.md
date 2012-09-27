US ZIP Code Data
================
Recently, I was thinking to myself, "Where do all of these wonderful sites on the web get information to map cities, towns, and <a href="http://en.wikipedia.org/wiki/ZIP_code">US ZIP codes</a> to actual locations?"  I then though, "How much do they pay?"  In reality, I don't know the answer, though there seem to be many companies you can pay for the information.

The best data I could find easily was from the <a href="http://www.census.gov/geo/www/gazetteer/places2k.html">US Census</a>, though it is in a terse, fixed-column format.  Clearly then, the next step is to read it into a database.

So, naturally, I created a small Ruby script to do just that.  If you are interested in such things, you can view it <a href="http://github.com/swenson/rubyzipload">over at github</a>.

The next question I am curious about is calculating the distance between two points on the Earth's surface given their latitude and longitude pairs.  This isn't <a href="http://en.wikipedia.org/wiki/Geographic_coordinate_system">trivial</a>, but it shouldn't be too hard to get a rough estimate.