# JSON API Design

There are a few points I've learned about designing JSON APIs over the years, and I've had a hard time finding articles that pinned down this advice. So, here are a couple of design tips for JSON.

## Don't give semantic meaning to object keys

The keys themselves in a JSON object should not give signifiant information.

What do I mean? Here is a JSON object whose keys have semantic meaning from an endpoint that is meant to give a list of movements and actions for a robot to take.

<pre>
{
    "left": "5m",
    "forward": "10m",
    "grab": "left"
}
</pre>

At a glance, this seems nice and compact. However, ask yourself: are these actions ordered? Do I need to move left, then forward, then grab? What if I want to repeat an action, like left, forward, left?

While it is technically valid for JSON to contain such repetitions and ordering, such as in:
<pre>
{
    "left": "5m",
    "forward": "10m",
    "left": "6m",
    "grab": "left"
}
</pre>

To parse this correctly will be tricky and non-standard in every language.
Most parsers will treat this object as identical to:

<pre>
{
  "forward": "10m",
  "grab": "left",
  "left": "6m"
}
</pre>

(although it is not clear which of the `left` actions will "win").

In addition, it can be more difficult to parse such an object. In many languages, you might be forced to deserialize the object into a generic `map` or `dict`, which can lead to more error-prone code.

Instead of assigning semantic meaning to the keys, it is better to use an array with all of the objects being of the same type. This way you can enforce ordering, can have duplicates, and make it easier to parse.

Also, what if you wanted to have two arguments to an action, like specifying which arm to `grab` with and how much pressure? Wit the above format's compactness, it might be difficult to extend in a backwards-compatible way.

**🚫 NO**

<pre>
{
    "left": "5m",
    "forward": "10m",
    "left": "6m",
    "grab": "left"
}
</pre>

**✅ YES.**

<pre>
{
    "actions": [
        { "action": "left", "argument": "5m" },
        { "action": "forward", "argument": "10m" },
        { "action": "left", "argument": "6m" },
        { "action": "grab", "argument": "left" }
    ]
}
</pre>

It may be more verbose and larger, but it is more extensible, easier to parse, and can preserve order without relying on tricky JSON parsing.

## Your top-level response should always be an object

You may be tempted to make the top-level response for a list operation be an array, but it is critical that it always be an object.

This is because, in the future, you may want to return additional information about the list itself: paging information, the kinds of things in the list, dates, etc.

It is always safer to add additional keys to an object than to fundamentally change an endpoint from an array to an object.

**🚫 NO**

<pre>
[
    { "a": "b"},
    { "a": "c"}
]
</pre>

**✅ YES.**

<pre>
{
    "values": [
        { "a": "b"},
        { "a": "c"}
    ]
}
</pre>

<hr />