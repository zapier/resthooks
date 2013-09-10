title: How Emma Uses REST Hooks
author: Interview with Alex Ezell
date: 2013-08-26
comments: false

### [Home](/) > {{ title }}

<div class="quote">Web services would just come to a crawl because [partners] were doing 1000 requests per second.</div>

<iframe width="560" height="315" src="//www.youtube.com/embed/ZmLeOGDrwmU?color=white&theme=light&rel=0" frameborder="0" allowfullscreen></iframe>

## About Emma

Emma is an email marketing platform. With Emma you can design stylish email campaigns with easy-to-use features, send those campaigns to customers and collect statistics about how well they perform.

## Case Study

Emma got into the API space early. They've had some version of their API for almost 7 or 8 years now. Since then, the API landscape has changed dramatically.

Their original SOAP version was replaced a few years ago with a modern REST API. Only a few months after launching their REST API, they added REST hook support based on initial feedback.

Over the last year or so, they've expanded their webhook coverage significantly. The biggest advantages of REST Hooks for Emma is how granular and simple they are.

Hooks allow Emma to avoid complex integrations with partners. Before, integrations with partners would take months and Emma would spend a lot of time guiding developers through setting up polling infrastructure and other details.

With REST Hooks, Emma can point to their lighter weight, more granular hook based system for getting at very specific information, like email bounces.

Emma targets small and medium size companies which often don't have dedicated IT teams or people with domain knowledge about APIs. REST Hooks dramatically simplify how much time and effort they need to put into 3rd party developer support.

Let's take a look at how Emma uses REST Hooks.

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
    <td><i class="icon-check-sign"></i></td>
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
    <td><i class="icon-check-sign"></i></td>
  </tr>
</table>

## REST Hooks

Emma's REST API supports several methods for interacting with webhooks. Classically, you can create, update, view, and delete hooks through their REST API. Additionally, there is an endpoint to access a list of available events which the user could choose from.

## Skinny Payloads

Emma sends all their hooks as skinny payloads. This means the hook payload itself simply contains IDs and references back to their REST API. This is a useful security mechanism because it guarentees that the receiver of the hook has a valid API key before allowing access to any sensitive business data.

## Emma Resources

[Emma Home Page](http://www.myemma.com/)  
[API Documentation](http://api.myemma.com/api/)  
[REST Hooks Documentation](http://api.myemma.com/api/external/webhooks.html)  