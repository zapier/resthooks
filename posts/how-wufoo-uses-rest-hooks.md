title: How Wufoo Uses REST Hooks
author: Mike Knoop
date: 2013-08-26

<table>
  <tr>
    <th>REST hook feature</th>
    <th>Implemented?</th>
  </tr>
  <tr>
    <td><a href="/">Webhooks</a></td>
    <td><i class="icon-check-sign"></i></td>
  </tr>
  <tr>
    <td><a href="/">Subscription based</a></td>
    <td><i class="icon-check-sign"></i></td>
  </tr>
  <tr>
    <td><a href="/">Intent verification</a> <i class="icon-shield" title="Security feature"></i></td>
    <td></td>
  </tr>
  <tr>
    <td><a href="/">Identitiy verification</a> <i class="icon-shield" title="Security feature"></i></td>
    <td></td>
  </tr>
  <tr>
    <td><a href="/">Skinny payloads</a> <i class="icon-shield" title="Security feature"></i></td>
    <td></td>
  </tr>
  <tr>
    <td><a href="/">Retries</a></td>
    <td></td>
  </tr>
  <tr>
    <td><a href="/">Batching</a></td>
    <td></td>
  </tr>
  <tr>
    <td><a href="/">Order of delivery</a></td>
    <td></td>
  </tr>
</table>

Even if your blog only gets 10 hits a day, there are plenty of reasons to keep it in good condition, search wise, if you'd like to see your traffic grow. We're talking about making your site or blog more visible to searches engines like Google and co.

## 1. HTML Titles and Descriptions

Generally, hosted blogs (like wordpress.com and tumblr.com) do a pretty good job about this ([not always, though](http://wadefoster.net/post/43633476838/three-quick-wins-for-boosting-tumblr-search-traffic)). If you're throwing together your own blog from scratch or hosting your own blogging software, it's worth double checking you got your HTML header title and description tags correct.

Generally, it's best to have the title and description match the content of the page and vary from page to page. Search engines are more likely to show it than the same content that never changes. The title should be short, less than 10 words whereas a good description reads more like a sentence.

In blog terms, the title can match the title of the post (with some prefix or suffix describing the blog) and the description can match an excerpt of the post. Check out the example I'm running on this blog below.

```php
<?php $blog = true; // only set on blog pages ?>
<?php if (have_posts()) : ?>
<?php while (have_posts()) : the_post(); ?>
<?php
  $title = "Mike Knoop | Founder, Web Developer, and Mechanical Engineer";
  $description = "Personal archive and blog for all the awesome stuff I work on, including my current startup Zapier. Connect with me on Twitter and Google+.";
  if ($blog) {
    $title = "Blog | Mike Knoop";
    if (!$all_posts) {
      $title = get_post()->post_title . " | Mike Knoop";
      $description = strip_tags(get_the_excerpt());
    }
  }
?>
<?php endwhile; endif; ?>
      
<meta name="description" content="<?php echo $description; ?>">
<title><?php echo $title; ?></title>
```

## 2. Google Webmaster Tools

This is a [must-use tool](https://www.google.com/webmasters/tools/home?hl=en) (from Google itself!) if you're rolling your own site. It'll verify you as the owner of the site, suggest ways to improve it for speed and search, and even email you when there are outstanding problems (like available Wordpress updates).

Google Webmaster Tools are also really useful when migrating from one domain to another, such as going from a hosted blog to your own domain.

## 3. Google Authorship

A new trend that is growing in popularity is linking your content to your Google+ profile through Authorship. This is a simple way to tell Google who is writing what content.

[You can get started here](https://plus.google.com/authorship).

You'll need to verify and link your Google+ profile to your site via an anchor tag:

```html
<a href="https://plus.google.com/u/1/{{id}}?rel=author">Google</a>
```

And be sure to replace **{{id}}** with your own Google+ ID from your profile. Pretty soon you'll start to see your blog posts appearing in Google results like this:

![Google Authoriship](http://beta.mikeknoop.com/static/img/upload/0b93aa4ff26411e2a8f628cfe91e44cb.png)

## 4. Share Liberally on Social Media

After putting all the effort into writing great content, don't forget to share it! Not only will it help grow your audience (through re-shares) but you'll also feel more motivated with inbound feedback.

I'll thank my co-founder, Wade, for [reminding me](http://wadefoster.net/post/43633476838/three-quick-wins-for-boosting-tumblr-search-traffic) about some of these dead-simple todos.