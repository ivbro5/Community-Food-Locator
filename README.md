# Flask App Template

1. [Quick Setup for Replit](#setup)
2. [Running the App](#run)
3. [Anatomy of the App](#anatomy)

## Quick Setup for Replit<a id="setup"></a>

Fork this template and create your own copy - feel free to ask a peer or instructor if you have trouble with this, as it's a feature that changes somewhat frequently. 

## Running the App<a id="run"></a>

If you're using Replit, just press the "RUN" button. Use the "open in new tab" button to get a full-sized preview. 


## Anatomy of the app<a id="anatomy"></a>

Here's everything inside our Flask template. A first-time learner should really only start by looking at the **app.py**, the **model.py**, the **templates** folder, and the **static** folder. Almost everything else operates more behind the scenes, and can be a later focus. 

<pre>
flaskproject
├── app.py - This is the main file for our app.
├── model.py - This is where we will write the logic of our app.
├── readme.md - That's this file!
├── static - This is where we house assets like images and stylesheets.
│   ├── css - Put stylesheets here.
│   │   └── style.css
│   └── images - Put images here.
│       └── micropig.jpg
└── templates - Put templates (views) in this folder.
    └── index.html - This will be the first template we render.
</pre>

If you want a more detailed explanation, keep reading.

### Files you WILL need to know about / focus on:

#### The `app.py`

This is the most important part of your Flask application - it's the code that tells your application how to respond to the requests your users make when they visit your page, and it's really the main thing separating our web application from a standard website. For example, with a webSITE, if we went to `petespizza.com/myaccount`, it would display the same information for every user. With a webAPP, we can make sure `petespizza.com/myaccount` is unique to each user by coding out some behavior in our `app.py`.

#### The `model.py`

The `app.py` is really just meant to be air-traffic control for our web application's visitors - the complex logic should live here in `model.py`. 

#### The `templates` folder

We're upgrading from HTML pages to HTML templates - the big difference here is that templates can be injected with Python to generate new content. Instead of needing to code out 100 `myaccount` for 100 users, you can code just 1 page, and use template logic to provide each user with a customized experience. 

#### The `static` folder

Images and CSS files are generally items we want our user to be able to access easily and directly - that doesn't need to come through the application. The `static` folder is also sometimes called the "public" folder for that exact reason. This template uses it for images and for CSS, which are two of the most common things you'll encounter in a web application's public folder no matter what language the app itself is written in. 
