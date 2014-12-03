# So You Want To Learn Crypto, Part 2: Cyclic Groups And Short Codes

[Part 1 is here](http://www.caswenson.com/2014_11_06_so_you_want_to_learn_crypto_part_1)

## Modular arithmetic

When I first started tinkering with crypto, one thing I was confused about was modular arithmetic.
It's applications to crypto are everywhere: AES is based in part on finite field
arithmetic, for example.
However, modular arithmetic acts a little strange if you aren't used to it.
I've seen this topic confuse just about everyone at some point, so I thought
I would explore modular arithmetic a little, and show a fun application of it for generating shortened URLs (or short codes).

To start, you can think of modular arithmetic simply as: every time you do a numerical operation, like adding, subtracting, or multiplying two integers,
you also take the modulus with respect to some other number.
Like, we know that $1 + 10 = 11$, but if we are doing arithmetic modulo
$6$, then $1 + 10 \equiv 5$ (because $11 \div 6 = 1$ with remainder $5$).
We use $\equiv$ to mean "equals modulo something" or "is congruent modulo something".

Addition, subtraction, and multiplication are easy: just add, subtract, or multiply the numbers like normal, then divide by the modulus and take the remainder.

Some more examples modulo $6$: $2 + 5 \equiv 1$, $2 \cdot 5 \equiv 4$, $2 - 5 \equiv -3 \equiv 3$.

There in the last example we saw that $-3 \equiv 3$ modulo $6$.
In math, we often will use only the positive remainder (so, $3$), but
in some programming languages, negative remainders are allowed in some
cases (so you might see $-3$).
For the most part, that doesn't matter: all of the arithmetic will
still work as expected.

## Division, or, multiplicative inverses

Addition has its opposite, subtraction, that works by default.
Multiplication also works, but its opposite, division, isn't *guaranteed* to work.

For example, we might want to know, can we divide by 2?
Division is really multiplying by the inverse, so what is the inverse of 2?
Looking, again, modulo 6:

$$2 \cdot 1 \equiv 2$$
$$2 \cdot 2 \equiv 4$$
$$2 \cdot 3 \equiv 0$$
$$2 \cdot 4 \equiv 2$$
$$2 \cdot 5 \equiv 4$$

So, $2$ has no inverse modulo $6$, because nothing, when multiplied by $2$, is equal to $1$.
And if we try to divide by $2$ modulo $6$, it fails: $4 \div 2$ is still $2$, but what is $3 \div 2$? Normally, we'd just say $3/2$ or $1.5$, but we don't
have fractions or decimal points here: all we have is the integers $0--5$, and
*none* of them, when multiplied by $2$, is equal to $3$.

But, sometimes we have multiplicative inverses.
Modulo $6$, $5$ has a multiplicative inverse: it's also $5$.
This means that dividing by $5$ is the same as multiplying by it.

$$2 \cdot 5 \equiv 10$$
$$2 \div 5 \equiv 2 \cdot 5 \equiv 10$$

## Cyclic groups

Okay, so, division sometimes works. When?

Well, simply put, division is guaranteed to work, in that we will be able to find
a multiplicative inverse, if we are working modulo a prime or a prime power, e.g., modulo $7$ or $7^2 = 49$.
When we have such a case, we call the set of numbers modulo the prime (or prime
power) a *finite field*.
I won't go into the nitty gritty details on the terminology, but essentially,
a *field* is what we get when division works.
Sometimes, we call the numbers (modulo our modulus), except $0$, the
multiplicative group, or the cyclic group.

Why cyclic?
Well, when we are working modulo, say, a prime $p$, then we can
generate at least part of the group with another prime, $g < p$,
by multiplying $g$ by itself a bunch of times.

For example, modulo $11$, with $g = 2$:

$$g \equiv 2$$
$$g^2 \equiv 2 \cdot 2 \equiv 4$$
$$g^3 \equiv 4 \cdot 2 \equiv 8$$
$$g^4 \equiv 8 \cdot 2 \equiv 16 \equiv 5$$
$$g^5 \equiv 5 \cdot 2 \equiv 10$$
$$g^6 \equiv 10 \cdot 2 \equiv 20 \equiv 9$$
$$g^7 \equiv 9 \cdot 2 \equiv 18 \equiv 7$$
$$g^8 \equiv 7 \cdot 2 \equiv 14 \equiv 3$$
$$g^9 \equiv 3 \cdot 2 \equiv 6$$
$$g^{10} \equiv 6 \cdot 2 \equiv 12 \equiv 1$$
$$g^{11} \equiv 1 \cdot 2 \equiv 2$$
and we've looped back around.
Hence the term *cyclic*.

Modulo $11$, we generated the whole multiplicative group (of size $10$).
However, we won't necessarily always generate the entire group: sometimes
we get a subgroup instead.
For example, look at $g = 2, p = 7$:

$$g \equiv 2$$
$$g^2 \equiv 2 \cdot 2 \equiv 4$$
$$g^3 \equiv 4 \cdot 2 \equiv 8 \equiv 1$$
$$g^4 \equiv 1 \equiv 2 \equiv 2$$
and we've looped after only $3$ elements.

In general, for a multiplicative group defined by $q$ of size $q - 1$, then
any element will generate a subgroup that *divides* $q - 1$.
So, for $7 - 1 = 6 = 2 \cdot 3$, so an element could generate
subgroups of size $1$, $2$, $3$, or $6$.

## Crypto

So, where's the crypto?

Well, first off, we might have noticed that the operation $g^x$ seems
to have this "scrambling" effect: the numbers that you get out
are kind of random.

In fact, they're very random for large moduli $q$.
In general, it's believed to be quite hard, given $g$, $q$, and
$g^x$ (modulo $q$) to figure out $x$.
This is called the *discrete logarithm* problem,
and the fact that it is believed to be difficult means
that people have used its difficulty as the foundation
behind crypto, such as, especially:

* [Diffie&ndash;Hellman](http://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
* the [Digital Signature Algorithm](http://en.wikipedia.org/wiki/Digital_Signature_Algorithm)
* [ElGamal](http://en.wikipedia.org/wiki/ElGamal_encryption)

How large is "large"?
Large $q$ generally means hundreds or thousands of bits in size.

We'll come back to this bit in a bit, but the important part to note here is that, in general, inverting the exponentiation, or, taking the discrete logarithm,
is hard.

Also, finite field arithmetic, in particular, division in a finite field,
plays a critical part in [AES](http://en.wikipedia.org/wiki/Rijndael_S-box).

## Short codes

There's another useful thing we can use modular arithmetic and discrete logarithms for: a URL shortening scheme, like the URLs you see
starting with `g.co`, `t.co`, `bit.ly`, etc.

There are a few ways you might try to implement such a scheme.
First, we'll assume that you are just assigning each URL a number,
and then you'll use something like [Base32](http://en.wikipedia.org/wiki/Base32) to convert the number (in binary) to a string.

Then how do you assign the number?

1. Just pick a random number and store it in a database, tied to the full URL.
2. Hash the full URL, and use part of the hash as the number.
3. Use a 1-up counter and tie it to the full URL.
4. Use a 1-up counter, but try to *scramble* it, for some definition of *scramble*.

Option 1 is the simplest, and requires basically no math: just generate a random number and stick it in the database.
If there is a collision, try again.

The downside is that, for very short codes, such as for a 5-character Base32 code, the numbers will all be $< 2^{25}$, and will be very likely to collide because of the [birthday paradox](http://en.wikipedia.org/wiki/Birthday_problem).
Lots of collisions means you have to try a bunch of times to insert into the
database successfully, and that means more round trips, more chances for weird
race conditions, and more chances for bugs.

Option 2, hashing the full URL, has similar downsides for short hashes: collisions.
This case is even worse though, because you can't change the hash of the URL,
so any collisions are fatal, and mean you can't use that full URL.
So that option is not great.

Option 3, using a 1-up counter in the database, is really easy:
just use a built-in 1-up counter, or assign a bunch of numbers to
individual servers to use, and have them request new batches of numbers
occasionally.
However, this leads to undesirable URLs, like
`http://short.url/AAAAC`.
It allows users to guess what their URLs might be, and to start poking
around at other short URLs.

Option 4 is a compromise: we want the simplicity of the 1-up counter,
but we don't want users to be able to easily and meaningfully guess the short
URLs.
We just need a scrambling function.

## Scrambling a 1-up sequence

But what to choose?

Well, again, we have some options.
Some thought might lead you to think: well, we could just add a constant to the number, or multiply by a constant.
However, this will be pretty obvious to users: they'd notice that consecutive
short URLs would always differ by constant amounts.

Another line of thought: could we use the number in a random number generator
(say, as the seed), and just turn the crank and use the next number in the
sequence?
Yes, that's a great idea, as long as we're careful.
Specifically, we have to be careful about collisions.

Two common random number generators that might fit the bill are
[linear-feedback shift registers](http://en.wikipedia.org/wiki/Linear_feedback_shift_register) and
[linear congruential generators](http://en.wikipedia.org/wiki/Linear_congruential_generator).

But, we might have a problem: we might need to "unscramble" the numbers,
to tell if they might be in the database.
We might just store the scrambled versions next to the 1-up counter, but
that would require extra storage, and would probably require us to either
write complicated SQL or do an `UPDATE`, and another database round-trip, to
set the scrambled number as well.
I don't like either of those options.

So, how hard is it to unscramble those random number generators?
For linear-feedback shift registers, this is trying to count how many steps it took to get to the given output number, which is kind of difficult to do.
But, the same is true of linear congruential generators.

Let's take a closer look at the linear congruential generator.
It works by, given an number $X_i$, generating the next number by:

$$X_ {i+1} = A \cdot X_i + C$$

If we assume $C = 0$ and $X_ 0 = 1$, we can compute $X_i = A^i$: this is exactly the same thing as exponentiation, which
is how we found cyclic groups.
So, to "scramble", all we need to do is exponentiate in our cyclic group.

Oh, but wait, this sounds like bad news: we know that inverting exponentiation is the
discrete logarithm, which is hard in general.

The keywords there are "in general".
Can we make pick cyclic groups where it is easy?

Yes, we can.

## Easy discrete logarithms

If we are working in a cyclic group modulo $p$, a prime, and if
$p - 1$ is the product of a bunch of small primes or prime powers, then
computing discrete logarithms is easy.
To compute discrete logarithms in that case, we can use the
[Pohlig&ndash;Hellman algorithm](http://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm).

The Pohlig&ndash;Hellman algorithm works by taking advantage of
short cycles in the cyclic group: essentially, we can piece together the
"full" discrete logarithm by computing a bunch of "small" discrete logarithms,
and using the [Chinese remainder theorem](http://en.wikipedia.org/wiki/Chinese_remainder_theorem)
to stitch them back together.
Each of these "small" discrete logarithms are in subgroups defined by
the factors of $p - 1$: so a bunch of small factors of $p - 1$ means
a bunch of small discrete logarithms to do.
If the factors are all very small, then we can just precompute
all factors in the small subgroups.

## Putting it all together

Since we want roughly five-character codes, we need to find a large 25-bit
prime with which to make our cyclic group.
Specifically, we want a prime $p$ such that $p - 1$ is all tiny factors.
To make the math easier, it would be nice if $p - 1$ has no repeated
factors (that is, no prime powers).

In [Sage](http://www.sagemath.org) (a Python-based mathematics environment),
we can find such a prime with this code:

<pre>
smoothest = 2^30 # just something large
for p in primes(2^24, 2^25):
  smoothness = 0
  for f, e in (p - 1).factor():
    if e != 1:
        smoothness = 2^30
        break
    smoothness += f
  if smoothness < smoothest:
    smooth = p
    smoothest = smoothness
print smooth, smooth - 1, (smooth - 1).factor()
</pre>

If we run this snippet, we find the best prime is $17160991$.
We can confirm that
$17160991 - 1 = 17160990 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 17 \cdot 19 \cdot 23$.

This means that we can compute logarithms modulo $17160991$ by pre-computing
and storing just $87$ numbers (the sum of the factors of $p - 1$)
using Pohlig&ndash;Hellman.

We also need to pick a base $g$, that is, the number we are exponentiating
in our cyclic group.
We basically need a number that generates the entire multiplicative group.
We can use Sage again to find such a number:

<pre>
for q in primes(3, 1000):
  if GF(modulus)(q).multiplicative_order() == modulus - 1:
    print q
    break
</pre>

In this case, we find that $61$ is the smallest prime that generates
the full multiplicative group, so it will be our base.

So, our procedure so far to scramble an integer $x$ looks like:

$$61^x\ (\text{mod}\ 17160991)$$

However, there is one tiny problem here: for $x = 0$, we get $1$, and for
$x = 1$, we get $61$, and for $x = 2$, we get $3721$.
These values stick out a bit (they're all small and easily recognized).
To hide them, we can just add some small number to $x$, like 30, giving us

$$61^{x + 30}\ (\text{mod}\ 17160991)$$

So, for $x = 0$, we have $4244504$ and $x = 1$ gives us $1499879$.

If we want to invert a short code, we'll need to unscramble a number $y$ to find the unscrambled number, that is, to find $x$ in

$$y \equiv 61^{x+30}\ (\text{mod}\ 17160991)$$

In the first of the two examples above, we would be trying to solve:

$$4244504 \equiv 61^{x+30}\ (\text{mod}\ 17160991)$$

Using the Pohlig&ndash;Hellman algorithm, we can easily compute (with a
few modular exponentiations) the discrete logarithm of $4244504$ is $30$, which means that $x = 0$.

## Some code

I've released code for the above computations, including the
Pohlig&ndash;Hellman algorithm implementation, in Python on
[GitHub](https://github.com/swenson/shortcodes), licensed under MIT.
