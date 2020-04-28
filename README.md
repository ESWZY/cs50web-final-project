# Final-Project ![Django CI](https://github.com/ESWZY/cs50web-final-project/workflows/Django%20CI/badge.svg) [![Travis](https://img.shields.io/travis/com/ESWZY/cs50web-final-project/master?label=Travis%20CI&logo=travis)](https://travis-ci.com/ESWZY/cs50web-final-project)

Web Programming with Python and JavaScript

# Introduction

[This website](http://eswzy.pythonanywhere.com/) is a news article subscribe platform powered by [Django](https://www.djangoproject.com/). In this platform, readers can search for articles arbitrarily or browse the latest articles in the article plaza. 

For editors, they can upload articles in a format of HTML, and also can set a paywall for any article. And readers can donate to become a subscriber to browse the full article section.

# Project Structure

## Main Page

In the [main page](http://eswzy.pythonanywhere.com/), you can search text in any part of articles by input any words in the center input box, and click "Search" button. 

Besides, if you just want to read something new, just click "Article Plaza" button on the top, and you will get some articles randomly. Additionally, you don't need to log in for those actions.

![main page](/screenshot/index.png) 

## Result Page

In the result page, you can get articles with title, a simple brief and its author(s). If you don't satisfied with those results, you can continue to search in the top search bar.

If are are interested in some articles, you can click the title of the card, and you will be redirected to the full article page.

![Result page](/screenshot/search_results.png)

## Discovery Page

Additionally, the [discovery page](http://eswzy.pythonanywhere.com/articles/discovery) is as same as result page, except the article list.

![Discovery page](/screenshot/discovery.png)

## Article Page

In the [article page](http://eswzy.pythonanywhere.com/articles/South-Korea-Told-to-Do-More-to-Stop-Public-Officials-From-Laundering-Bribes), the detail of one article will be displayed, such as the title, author(s), publish date, and the most important part, the full text. 

If the article has the subscriber-only part, there will leave a subscribe prompt.

![Article sample1](/screenshot/article_sample1.png)

Besides, if you are not logging in, it will also display a login prompt.

![Article sample2](/screenshot/article_sample2.png)

But, how to read the full article? Don't worry, let's move on!

## Login Page

Before becoming a subscriber, you need to [login](http://eswzy.pythonanywhere.com/login) to allow the platform to remember you. Just input the username and password in the form below.

![Login page](/screenshot/login.png)

Don't have an account? I have 100 pre-registered accounts! They are "user1" to "user100". And the default password are all "user"!

## Shop Page

After logging in, you can click the "Become Subscriber" button in the top navigation bar to go into the [shop page](http://eswzy.pythonanywhere.com/shop). In this page, you will bind credit card to this account. (It will not debit your actual account)

You can input your credit card number and the money you want to recharge to the account. The phone field is reserved for further extend.

![Shop page](/screenshot/shop.png)

## Subscribe Page

After recharging to your account, you can become a subscriber [here](http://eswzy.pythonanywhere.com/subscribe). You can donate any number of money to become a subscriber so far.

![Subscribe Page](/screenshot/subscribe.png)

Maybe you are confused why don't donate directly. Hmmm, this can be regarded as a reserved function. (Such as having a VVIP or evolving to a finance management platform.╰(￣▽￣)╮)

Then you have the authority to read the full article.

![Full article with dividing line](/screenshot/article_sample3.png)

For the display reason, the paywall dividing line is displayed, you can close it by yourself.

![Full article](/screenshot/article_sample4.png)

# Back End

## Super User

Super user is a feature provided by Django. The super user can manipulate all data in the [backend management dashboard](http://eswzy.pythonanywhere.com/admin/), just like God.

![Admin](/screenshot/admin.png)

Super user can also have a [view](http://eswzy.pythonanywhere.com/admin/auth/user/) of all users.

![Users](/screenshot/users.png)

## Editor

Editor or author is the person who can upload articles. They are in a "group" named "[Editors](http://eswzy.pythonanywhere.com/admin/auth/group/1/change/)", which only has the authority to add/change/delete/view articles in the backend dashboard.

![Editors group](/screenshot/editors_group.png)

Comparing with super user, editor can only access article data.

![Editors can do](/screenshot/editor.png)

The example editor account is: username: "editor", password: "123editor123".

## Article

[Article](http://eswzy.pythonanywhere.com/admin/articles/article/) is one of the most important entities of the platform. Article has fields like title, author, publish date, brief, free part and full part. 

Editor can only manipulate articles. If editors want the article to be totally free, they can set the "Full part" as None, literally.

![Add article](/screenshot/add_article.png)

And then, the article will be stored and become visitable.

![Added article](/screenshot/added_article.png)

# Setup

```shell script
git clone https://github.com/ESWZY/cs50web-final-project.git
cd cs50web-final-project
pip install -r requirements.txt
```

When the dependent packages are installed, you can run this command to run your server.

```shell script
python manage.py runserver
```

Run those following commands to migrate database.

```shell script
python manage.py makemigrations
python manage.py migrate
```

Or you can run this command to shell window.

```shell script
python manage.py shell
```

# Deploy to Heroku

[Heroku's filesystem is ephemeral](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem), any changes you make to files will be lost the next time your dyno restarts, which happens frequently (<b>at least once per day</b>). 

Since SQLite is a file-based database it is incompatible with Heroku.

Forget it!

# Deploy to PythonAnywhere

It's possible to deploy on PythonAnywhere! 

Tutorial article: 

<https://www.dj4e.com/assn/dj4e_install.md>

<https://help.pythonanywhere.com/pages/DeployExistingDjangoProject>

and 

<https://help.pythonanywhere.com/pages/DjangoStaticFiles>

The link is here: [http://eswzy.pythonanywhere.com/](http://eswzy.pythonanywhere.com/)

The final website looks like:

![Deployed](/screenshot/deployed.png)

# Finally

Thanks for all people make [CS50's Web Programming with Python and JavaScript](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript) possible. Especially, thanks for [Brain Yu](https://www.edx.org/bio/brian-yu)'s excellent lecture and his "great question", which motivate me to finish the course study.

April 28, 2020
