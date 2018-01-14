# Friendship API

This weekend, I wrote a quick email application called [Friendship API](http://friendshipapi.com).
It solves a problem that I have: I am just terrible at staying in touch with my friends via email.
This is a shame: email is really a great tool for keeping in touch.

Friendship API works like this: it uses ContextIO to look at people you interact with, filter out what looks like spam and business email, and send you a weekly email reminding you that you owe a person an email.

There's no account or password to manage: the weekly emails contain action links to ignore certain people in the future, generate another reminder, and cancel your subscription.
Hence, I use the term "email application".

There's also very little storage we have to do: basically, we keep track of email addresses of people who sign up, their ContextIO tokens, what recommendations we send out, and a list of email addresses that the people want to ignore.
If they cancel their subscription, we revoke our ContextIO tokens.

## Why Python? The Stack
It's all built on Python 2.7. Why Python? Because there are a lot of great libraries and utilities that I can leverage to help me write the app quickly (over the weekend).
Sadly, some of the stack was still not ready for Python 3+.

* [ContextIO](http://context.io): to do the extremely hard work of connecting to people's email accounts. Plus, they have a great 	[Python API](https://github.com/contextio/Python-ContextIO).
* [Mailgun](http://mailgun.com): to send emails, which has a dead-simple RESTful API.
* [Flask](http://flask.pocoo.org/): a straightforward way to build simple web APIs.
* [Celery](http://www.celeryproject.org/): a wonderful Python-based task queue system.
* [SQLAlchemy](http://www.sqlalchemy.org/): a robust way to deal with SQL databases.
* [Heroku](http://heroku.com): an easy way to host the email application.
* [Amazon S3](https://aws.amazon.com/s3/): an easy way to host a simple static website.
* [ThemeForest](http://themeforest.net/?ref=swenson): a cheap way to get an website theme that looks good.
* [Diet Dr Pepper](http://www.amazon.com/gp/product/B003I81BW2/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B003I81BW2&linkCode=as2&tag=mathfigu-20&linkId=KN3HZJLTADLF6DFJ): my choice of caffeine to keep me typing throughout the weekend. :)

Massive thanks to the hard work of those who wrote the stack I stand on.

## The Process

How does one go about writing an app like this after getting the idea and setting
aside a spare weekend? Well, here's the process I followed at least:

1. Outline in your head (or write down) the features that you need to launch with.
2. Talk it over with someone.
3. Sign up for all of the accounts you might need and don't already have (in this case, the ContextIO developer account).
4. Write a simple program to prove that the hard things are possible: in this case, that is reasonable to use ContextIO to get the data we need, and then to generate sensible recommendations.
5. Use Celery to make the program calls asynchronous.
6. Write a simple Flask app that calls into that program.
8. Use [RequestBin](http://requestb.in/) to capture the ContextIO callback, so you know how to capture the authentication token when someone signs in.
8. Write the Flask endpoints to generate a ContextIO signup session, and the Flask endpoint to capture the ContextIO callback information, and process based on that.
9. Hook up the recommendation function to send out an email.
10. Write a barebones web page that calls out to your web site.
11. Setup hosting for everything.
12. Have someone who isn't you test out the flow.
13. Write the rest of the functions for your bare minimum features.
14. Theme the static site.

That was fun!

# Future Improvements

There are a few more things that would be nice to do for the application.

* Better recommendations. There's still a lot of work that could be done to improve recommendations:
   * Using past recommendations to influence future recommendations.
   * Adjusting the metric used to pick who to recommend.
	* More advanced filters to differentiate business, spam, and friendship conversations.
* Adjusting the frequency of recommendations. It's currently hardcoded to one week per email.
* Better-looking recommendation emails.
* Suggest topics of conversation. We could pick topics randomly, or we could try to analyze past emails, perhaps.
* Handle people with multiple email addresses. Currently, the application keys off of email
  addresses alone, so it can suggest someone whom you might be corresponding with regularly
  if you are doing so with a different email address.
