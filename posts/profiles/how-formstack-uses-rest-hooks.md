title: How Formstack Uses REST Hooks
author: Interview with Brandon Peters
date: 2013-08-27
comments: false

### [Home](/) > {{ title }}

<div class="quote">We did notice a huge drop in the amount of server resources dedicated towards our API.</div>

<iframe width="560" height="315" src="//www.youtube.com/embed/vtHPK9k_UDk?color=white&theme=light&rel=0" frameborder="0" allowfullscreen></iframe>

## About Formstack

Formstack is an Online HTML Form Builder that lets you create all types of online forms. Build order forms, contact forms, registration forms, & online surveys.

## Case Study

Formstack built their original API when their product launched but adoption was so-so and lots of developers were hitting rate-limits.

While refreshing their API to be more usable about a year ago, the Formstack team made sure to include REST Hooks support. Not only did it provide a much better user experience for those consuming the API, but it also gave an outlet for users demanding more integrations.

Even better, after adopting REST Hooks they saw a significant drop in the amount of server resources needed to power their API, giving them improved performance to go with the improved user experience.

Let's take a look at how exactly Formstack uses REST hooks.

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

Formstack is a classic example of REST hooks. They have a REST componenet to subscibe, access and unsubscribe from hooks. Addionally, they offer many toggles which can be used to make REST hooks more secure from the receiver's point of view.

## Identity Verification

Formstack uses a handshake key to identify they are a verified sender. This handshake key is set up specified by the receiver when the subscription is set up for the first time.

## Skinny Payloads

Formstack requires you to specify wether you'd like skinny or fat payloads when you subscribe to receive hooks. You can send along a true of false value for `append_data` when subscribing.

## Formstack Resources

[Formstack Home Page](http://www.Formstack.com/)  
[API Documentation](https://www.formstack.com/developers/api)  
[REST Hooks Documentation](https://www.formstack.com/developers/webhooks)  