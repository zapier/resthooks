title: How Shopify Uses REST Hooks
author: Interview with David Underwood
date: 2013-09-18
comments: false

### [Home](/) > {{ title }}

<div class="quote">We were seeing really complex Shopify add-on setup intructions and our hook subscription mechanism solved that.</div>

<iframe width="853" height="480" src="//www.youtube.com/embed/0Vi7n31_pRM?rel=0" frameborder="0" allowfullscreen></iframe>

## About Shopfy

Shopify is a powerful ecommerce website solution that allows you to sell online by providing everything you need to create an online store.

## Case Study

Shopify launches their original API in 2006 in response to developers wanting to integrate with their Shopify online stores. Shopify is a Ruby on Rails shop which made it easy to spin up their original API.

REST Hooks were added after the original launch. Ecommerce is very real-time so an API that developers had to poll against was a serious drawback. Additionally, because so many Shopify customers are not developers, it had to be very user friendly to set up hook subscriptions. This is what REST Hooks offers.

In addition to the user-facing benefits, Shopify was able to reduce their server load dramatically.

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
    <td><a href="/">Identity verification</a> <i class="icon-shield" title="Security feature"></i></td>
    <td><i class="icon-check-sign"></i></td>
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

Shopify offers the full gamut of hook subscription management. They have about 12 different hooks developers [can subscribe to](http://docs.shopify.com/api/webhook). They offer endpoints on their REST API to list hook subscriptions, receive counts (useful for verification), and create new webhook subscriptions.

Additionally, Shopify still lets developers and users create REST Hook subscriptions via their user intercace -- an increasingly common pattern for services with large user bases.

## Retries

Shopify has implemented a 10-second timeout period and a retry period for subscriptions. They wait 10 seconds for a response to each request, and if there isn't one or they get an error, they will retry the connection to a total of 19 times over the next 48 hours. A webhook will be deleted if there are 19 consecutive failures for the exact same webhook.

## Fat Payloads

Shopify sends all their hooks over the wire with full API responses, meaning you do not need to perform another API call in order to get usable data.

## Identity Verification

Webhooks created through the API by a Shopify App can be verified by calculating a digital signature. The digital signature is an HMAC SHA256 hash. Webhooks created manually through the Shopify UI cannot be verified.

You can read more about the verification procedure (and find sample code) [here](http://docs.shopify.com/api/tutorials/using-webhooks#verify-webhook).


## Shopify Resources

[Shopify Home Page](http://shopify.com)  
[API Documentation](http://docs.shopify.com/api/)  
[REST Hooks Documentation](http://docs.shopify.com/api/webhook)  