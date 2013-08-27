```
  _____   ______   _____  _______  _    _   ____    ____   _  __  _____    ____   _____    _____ 
 |  __ \ |  ____| / ____||__   __|| |  | | / __ \  / __ \ | |/ / / ____|  / __ \ |  __ \  / ____|
 | |__) || |__   | (___     | |   | |__| || |  | || |  | || ' / | (___   | |  | || |__) || |  __ 
 |  _  / |  __|   \___ \    | |   |  __  || |  | || |  | ||  <   \___ \  | |  | ||  _  / | | |_ |
 | | \ \ | |____  ____) |   | |   | |  | || |__| || |__| || . \  ____) |_| |__| || | \ \ | |__| |
 |_|  \_\|______||_____/    |_|   |_|  |_| \____/  \____/ |_|\_\|_____/(_)\____/ |_|  \_\ \_____|
                                                                                                 
```

REST hooks are a lightweight subscription layer on top of your existing REST API.

The real-time web is already here, but REST APIs haven't kept up. Many major players have already standardized upon subscription webhooks. REST hooks are a way to consolidate that momentum and push it to a broarder audience.

For more information, code examples, libraries, and company profiles check out [http://resthooks.org](http://resthooks.org).

[http://resthooks.org](http://resthooks.org) an initiative by [Zapier](https://zapier.com) 2013.


## How to run locally.

Clone the repo and hop into the correct directory.

```
git clone git@github.com:zapier/resthooks.git && cd resthooks
```

Next, you'll want to make a virtual environment (we recommend using
virtualenvwrapper but you could skip this) and then install dependencies:

```
mkvirtualenv resthooks
pip install -r requirements.txt
```

Now you can run the server!

```
foreman run web
# or
gunicorn resthooks:app
```
