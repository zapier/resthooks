title: How Formstack Uses REST Hooks
author: Brandon Peters
date: 2013-08-27
comments: false

<div class="quote">"We did notice a huge drop in the amount of server resources dedicated towards our API."</div>

<iframe width="560" height="315" src="//www.youtube.com/embed/vtHPK9k_UDk" frameborder="0" allowfullscreen></iframe>

While refreshing their API to be more usable about a year ago, the Formstack team made sure to include REST Hooks support.  Not only did it provide a much better user experience for those consuming the API, but it also gave an outlet for them to reference for all the potential integrations users wanted, but Formstack did not have native support for.

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

## REST Hooks

ActiveCampaign's REST API supports several methods for interacting with webhooks. They offer an endpoint to create, list, delete, and review specific hooks. Hooks can be triggered <a href="http://www.activecampaign.com/api/webhooks.php">by several things</a> including:

1. Changes to a contact (subscribe, bounce, etc.)
2. Changes by an admin user (adding a contact manually)
3. Events by the system (automated emails, etc.)
4. Events through the API (adding a contact via the API)

## Fat Payloads

ActiveCampaign sends all their hooks over the wire with full API responses, meaning you do not need to perform another API call in order to get usable data.

## Retries

While ActiveCampaign's API does not retry failed hooks, they will store a delivered status which you can request specifically by hitting their hook list endpoint. This could be used to periodically verify you've received all hooks or to access old hooks.

## Inline Unsubscribe

If your hook endpoint returns a `410` response, then ActiveCampaign will automatically delete and clean-up the hook for you.

## Formstack Resources

[Formstack Home Page](http://www.Formstack.com/)  
[API Documentation](https://www.formstack.com/developers/api)  
[REST Hooks Documentation](https://www.formstack.com/developers/webhooks)  

## About ActiveCampaign

Formstack is an Online HTML Form Builder that lets you create all types of online forms. Build order forms, contact forms, registration forms, & online surveys.
