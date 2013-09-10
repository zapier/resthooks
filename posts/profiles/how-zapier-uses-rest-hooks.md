title: How Zapier Uses REST Hooks
author: Mike Knoop
date: 2013-09-09
comments: false

### [Home](/) > {{ title }}

<div class="quote">Stop the Polling Madness!</div>

## About Zapier

Zapier enables you to automate tasks between other online services,
such as Salesforce, Basecamp and Gmail.

Imagine capturing Wufoo form leads automatically into Salesforce or displaying new Paypal sales in your Campfire team chat room. In all, more than 235 apps are connected through its web automation platform.

## Case Study

Zapier is a bit unique as it integrate with other APIs instead of
hosting its own. While Zapier does not formally have an API, their developer platform enables developers to add APIs to Zapier through a UI. If an API does not conform precisely to the standard Zapier expects, there is a Scripting API available which developer can use to transform requests and responses to conform.

REST Hooks are a large part of Zapier's developer platform. Instead of needing to constantly poll other APIs looking for changes, REST Hooks enable huge performance optimizations.

You can find the full published spec about [how Zapier uses REST Hooks here](https://zapier.com/developer/reference/#rest-hooks).

## Zapier Resources

[Zapier Home Page](http://www.zapier.com/)  
[API Documentation](https://zapier.com/developer/)  
[REST Hooks Documentation](https://zapier.com/developer/reference/#rest-hooks)  
