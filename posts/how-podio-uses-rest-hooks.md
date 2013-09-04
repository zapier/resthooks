title: How Podio Uses REST Hooks
author: Andreas Pedersen
date: 2013-09-03
comments: false

<div class="quote">"Our partners can provision new customers much more efficiently. That's something our partners are very very happy about."</div>

<iframe width="560" height="315" src="//www.youtube.com/embed/uHfvAtUdrAo" frameborder="0" allowfullscreen></iframe>

Podio built their original REST API right along side their product. Following modern product techniques, their frontend, iOS and Android apps all consume the exact same API that is exposed to 3rd party developers.

Even at the beginning, Podio was looking to scale: they implemented REST hooks and rate limitting with an eye towards the future.

Some of Podio's most useful endpoints are those with filters which also happen to be the most expensive to generate. REST hooks workaround this limitation. They enable both the data developers want as well as lighter server load.

REST hooks (subscription webhooks) actually happened accidentally. Because all of Podio's frontends consume the same API, REST hooks were a necessity for dogfooding.

In time they learned this was a great decision after hearing from elated partners and 3rd party developers.

Let's take a look at the details about how Podio uses REST hooks.

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
    <td><i class="icon-check-sign"></i></td>
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
    <td><i class="icon-check-sign"></i></td>
  </tr>
  <tr>
    <td><a href="/">Batching</a></td>
    <td></td>
  </tr>
  <tr>
    <td><a href="/">Order of delivery</a></td>
    <td><i class="icon-check-sign"></i></td>
  </tr>
</table>

## REST Hooks

Podio REST hooks can actually be created in one of two ways. They can be created as classic REST hooks programatically via the REST API or the user can define webhooks within Podio's developer tools.

Following Podio's flexible model, there are several "nouns" and "verbs" you can subscribe to which are documented [here](https://developers.podio.com/doc/hooks).

## Intent Verifications

Podio enforces intent when subscribing to new hook endpoints. Every new hook must be verified. A notification will be send to the new hook URL and it is expected to return a special `code` along with a 2xx response.

Over time, hooks must continually respond with 2xx. If there are 50 consecutive non-2xx responses, the hook will become inactive and have to be re-activated either by the user or by the application via a teardown/setup cycle.

## Skinny Payloads

Podio only sends along a lightweight payload that contains the `id` of the item in question and a webhook `id`. Developers should turn around and call the Podio API to access the full data set. This is a security feature which enforced that developers have valid access tokens to consume hook based content.


## Order of Delivery

Podio sends along a webhook `id` which can be used to order incoming requests. Even though order is specified, it's really not required because Podio has skinny payloads. You'll always need to fetch the most recently resprentation of a resource after receiving a hook, making ordering implications moot.

## Podio Resources

[Podio Home Page](http://podio.com/)  
[API Documentation](https://developers.podio.com/doc)  
[REST Hooks Documentation](https://developers.podio.com/doc/hooks)  

## About Podio

Online work platform for collaboration and project management in one central place with tasks, calendar, contacts, activity stream and the ability to build business apps.