title: How ActiveCampaign Uses REST Hooks
author: Matt Thommes
date: 2013-08-26
comments: false

### [Home](/) > {{ title }}

<br/>

<div class="quote">"We got to the point where polling would sometimes disrupt service."</div>

<iframe width="560" height="315" src="//www.youtube.com/embed/QDgcisDm9ZA" frameborder="0" allowfullscreen></iframe>

ActiveCampaign has been committed to developers from the very beginning. They built their REST API 3-5 years ago to begin fostering a developer community and since then they've grown their platform to the point where load from API polling would sometimes disrupt service.

About a year ago, ActiveCampaign implemented REST hooks. Their server load has been reduced and they get fewer support tickets regarding polling.

Let's take a look at how exactly ActiveCampaign uses REST hooks.

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

## ActiveCampaign Resources

[ActiveCampaign Home Page](http://www.activecampaign.com/)  
[API Documentation](http://www.activecampaign.com/api)  
[REST Hooks Documentation](http://www.activecampaign.com/api/webhooks.php)  

## About ActiveCampaign

ActiveCampaign is a portable, easy Email Marketing platform targeted at small and medium size businesses. Create email marketing and HTML newsletter campaigns in minutes. Powerful email marketing software features with free premium templates.