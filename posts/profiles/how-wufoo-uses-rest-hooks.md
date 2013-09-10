title: How Wufoo Uses REST Hooks
author: Interview with Timothy Sabat
date: 2013-08-26
comments: false

### [Home](/) > {{ title }}

<div class="quote">We were having trouble with people who were basically calling this API ... every minute or even every 30 seconds.</div>

<iframe width="560" height="315" src="//www.youtube.com/embed/Gg1qmDY2RBg?color=white&theme=light&rel=0" frameborder="0" allowfullscreen></iframe>

## About Wufoo

Wufoo's HTML form builder helps you create online web forms to power your contact forms, online surveys, event registrations, accept payments and more.

## Case Study

Wufoo, like many others, has been in the API space a long time. They implemented their original non-REST APIs in 2008 and added their modern REST API about 3 years ago.

REST Hooks were added to the Wufoo API as part of an integrations push once they realized there was a lot of value for them to "cut out the polling middle man."

Wufoo is form software and the most common integration is putting the form data into another system. Classically, the only way to detect new form submissions was through polling.

Additionally, MySQL counts were a very expensive of generating an API response. Developers were polling the API every minute or even every 30 seconds looking for new responses in order to provide real-time-like experiences.

Wufoo had a "huge offenders list" and had to implement more strict API rate limitting so their level of service wouldn't be degraded across the board. But they didn't want to just take something away. Wufoo decided to offer hooks as the obvious alternative for developers who were overloading their servers via polling.

The other big part of REST Hooks is the subscription mechanism. Wufoo had a lot of big partners telling them they wanted to see their logo listed inside Wufoo's API. But Wufoo did not want to build one-off integrations with all these various services. So they built the subscription mechanism such that when developers registered a REST hook, their app's logo was automatically shown inside Wufoo as an available service to send data to.

Let's take a look at the details about how Wufoo uses REST Hooks.

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
    <td></td>
  </tr>
</table>

## REST Hooks

Wufoo originally offers hooks in several areas of their product. They have a user-facing interface to define hook callbacks and they also have a REST API which can be used to programmatically subscribe (ie. REST Hooks).

Once a hook has been subscribed to a specific form or user, the user can log in to Wufoo and choose more forms to send to the service that subscribed. This is one of the unique things about Wufoo's REST Hooks.

## Identitiy Verifications

Wufoo optionally allows a handshake key to be sent along with the hook subscription. This allows the receiver to define a secret word or phrase that will always exist inside any POST from Wufoo to the receiver. This can be used to verify the identity of the sender.

## Fat Payloads

Wufoo sends along the entire form response inline inside the hook payload. Optionally, Wufoo can also send along information about the exact field structure of the form that was submitted.

## Retries

Wufoo checks the response for non-200 and retries 3 times before the web hook is dropped off the queue. A back off mechanism is in place, to retry in roughly 5, 10, and 15 min increments.

## Order of Delivery

Wufoo does not have any hook identifiers but they do include a timestamp. Additionally, order of delivery is less important for Wufoo because their forms are atomic and 1-to-1 with each hook. A form can never be sumitted twice and can't be updated by the end user.

## Wufoo Resources

[Wufoo Home Page](http://wufoo.com/)  
[API Documentation](http://www.wufoo.com/docs/api/v3/)  
[REST Hooks Documentation](http://www.wufoo.com/docs/api/v3/webhooks/)  