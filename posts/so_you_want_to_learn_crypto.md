# So You Want To Learn Crypto, Part 1

Cryptography and cryptanalysis are topics that fascinate many people, but it's a tricky area to get into.
For instance, knowing the difference between a [hash function](http://en.wikipedia.org/wiki/Hash_function) and a [cryptographically strong hash function](http://en.wikipedia.org/wiki/Cryptographic_hash_function) is critical, but extremely easy to mix up due to confusing terminology.
In general, there's heavy jargon that takes serious studying to get a grasp on.

Cryptography is also almost entirely a self-taught discipline: even today, there are few college and graduate courses on cryptography, and most of those only cover the basics. (Indeed, this is why I wrote my book on cryptanalysis: I wanted to teach a class on the topic, and there was no suitable text, so I wrote my own.)
This means that it is reasonable, even necessary, to learn a great deal of crypto on your own.

With that in mind, I'm going list a few resources, recommendations, and maybe even explain a little bit myself to help get you started.


## Some resources to get you started

* [lvh](https://twitter.com/lvh) has a video from PyCon 2013 called [Crypto 101](http://pyvideo.org/video/1778/crypto-101).
I'm not the biggest fan of this video, as it goes through too much material in too short an amount of time, but it does give you a quick look at many different areas of cryptography.
Since it does cover so much, don't worry if not everything clicks.
Instead, I'd pick something that interests you, like hash functions or AES, and dive further into that one topic.
If you try to tackle too many subjects at once, it might be overwhelming.
* Once you've figured out some areas you actually like, you can start digging in in that particular field.
* There are some great books on cryptography that you'll probably want to read eventually, so I'll go ahead and list some of them here:
   * [Modern Cryptanlysis](http://www.amazon.com/gp/product/047013593X/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=047013593X&linkCode=as2&tag=mathfigu-20&linkId=T5SNSQXDSP6LHEER) by Christopher Swenson. Obviously, I'm a bit biased here, but I wrote some decent introduction sections to many areas of cryptography and cryptanalysis with lots of examples in Python, and there are far worse places to start. I focus primarily on block ciphers (like AES) and public key cryptography (like RSA).
   * [Applied Cryptography](http://www.amazon.com/gp/product/0471117099/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0471117099&linkCode=as2&tag=mathfigu-20&linkId=CBNLGUN6PZETLFCV) by Bruce Schneier. Extremely dated, but still has some useful stuff. A lot of block and stream cipher stuff.
   * [Practical Cryptography](http://www.amazon.com/gp/product/0471223573/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0471223573&linkCode=as2&tag=mathfigu-20&linkId=6ZT4U6PDRCMS4V3V) by Bruce Schneier. A good companion to Applied Cryptography that is a bit more updated, with lots of focus on understanding and correctly using cryptography.
   * [Algorithmic Cryptanalysis](http://www.amazon.com/gp/product/1420070029/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1420070029&linkCode=as2&tag=mathfigu-20&linkId=CNJQJOUTTRFOKRBH) by Antoine Joux. One of the newest books, and chock full of good stuff, with a focus on public key cryptography, stream ciphers, and lattices. This one's probably one of the most advanced cryptography books on the market.
   * [Handbook for Applied Cryptography](http://cacr.uwaterloo.ca/hac/) by Alfred Menezes, Paul van Oorschot and Scott Vanstone. This book covers a lot of material, but I find it a little terse at times. It is free though, which is a big plus.

This list is not comprehensive: it's probably best to just look at all of the available books, glance through some of the pages and the table of contents, and see if the style, approach, and depth meet your interests. In general, there are two kinds of crypto books you'll see on the market: academic ones and practical ones. When you start out learning, you'll definitely want to focus on the more practical tomes (Schneier and Swenson, for example), and start reading academic books (Joux's book, and many published by academic publishers like Springer) as you get more comfortable.

## I know the basics, what next?

Once you know Crypto 101 and you want to dive into Crypto 201, where do you go?

One great next step is to work on [The Matasano Crypto Challenges](http://cryptopals.com/).
Not only will you have to learn a lot to complete them, but you'll have real experience making and breaking codes.
I think this is a great next-step for a would-be crypto enthusiast.
(And this is even a great step for cryptographers on any level — I certainly had fun doing them.)

There are some Coursera courses on Cryptography taught by Dan Boneh ([Cryptography I](https://www.coursera.org/course/crypto) and [Cryptography II](https://www.coursera.org/course/crypto2)).
I haven't taken them, but the instructor is top-notch, and the syllabi are solid.

As you progress further in your knowledge, you should start reading recent research papers in cryptography.
One great place to keep track of is the IACR [Cryptology ePrint Archive](http://eprint.iacr.org/).
These are the cutting edge of cryptography and cryptanalysis, and they range from beginner-friendly to extremely deep, specialist literature.
The writing and publication quality of the cutting-edge papers also has a wide range.
And even though it is possible to learn almost everything about cryptography and cryptanalysis for free from these papers, the books in the previous section are often much easier to learn from since they have consistent writing style, terminology, notation, and editing.

## This part confuses me. Help!

I'm going to have some more blog posts in the near future clearing up some areas that I've seen be particularly sticky for some people.
In particular, I know that there are some sticky points in finite fields, RSA, and hashing that I think I can help clarify.

Check back next week for part 2 of *So You Want To Learn Crypto*.
