title: Documentation 
author: Zapier
date: 2013-08-27

## Links

1. [Security Best Practices](/docs/security/) patterns to verify intent and identity for hooks.
2. [Performance Best Practices](/docs/performance/) patterns for ensure your code is performant.
3. [Alternatives To REST Hooks](/docs/alternatives/) other real-time patterns in use around the web.


## What are REST Hooks? What are they not?

REST Hooks itself is **not** a specification, it is a **collection of patterns** that treat webhooks like subscriptions. These subscriptions are manipulated via a REST API just like any other resource. That's it. Really.

In this documentation you’ll find information on **creating the minimum implementation** as well as diving deeper into specific features that cover quite a few topics and their **best practices** within the pattern of REST Hooks. You can pick and choose from these topics and implement what makes sense for your API.

## Minimum Implementation Walkthrough

To comply with the REST Hooks pattern, there is a minimum set of pieces you’ll need to add to have a working implementation. This article will outline those minimums:

1. Mechanism to store subscriptions.
2. Mechanism to modify subscriptions via API.
3. List and implement event types.
4. Mechanism to send hooks.

Retries, intent and identity verification, batching and other components are optional and vary wildly between implementations.


### Mechanism to store subscriptions.

Highly dependent on your database selection, this first requirement is the foundation by which the subscriptions are managed. At the most basic level, a persisted subscription only really needs the following fields:

1. An event name or names the subscription includes.
2. A parent user or account relationship.
3. A target URL to send the payloads.
4. (optional) Active vs. inactive state (add link to security).

It is wise to make sure you index both the event and user relationship so subscription lookups are performant.


### Mechanism to modify subscriptions via API.

Also dependent on your API implementation, this allows anyone with normal API access to manipulate their subscriptions like any other resource on your API. For example, if you already have a REST API, the most common and logical solution is another resource:

Method  | Route                         | About
--------|-------------------------------|----------------------
GET     | /api/v1/subscription/         | list subscriptions
POST    | /api/v1/subscription/         | create a subscription
GET     | /api/v1/subscription/:id/     | get a subscription
PUT     | /api/v1/subscription/:id/     | update a subscription
DELETE  | /api/v1/subscription/:id/     | delete a subscription

These would simply manipulate the resources like any other REST endpoint, but with the added benefit that subscriptions have one side effect: their existence will cause webhooks be sent to the target URL when an event happens for that account.

This is an improvement over manually managed webhooks URLs as it gives interested third party applications the opportunity to dynamically create and update integrations that perform in near-real time functions.


### List and implement event types.

Next up would be enumerating and implementing each event type you’d like your REST Hooks subscription system to support. Each event type needs two things:

1. A name (use the noun.verb dot syntax, IE: contact.create or lead.delete).
2. A payload template (simply mirror the representation from your standard API).

For starters, we recommend create, update and delete events on your most popular resources. For example, if you had contact and deal resources, you’d define and implement contact.create, contact.update, contact.delete, deal.create, etc… events.

The payload that you build for each record in your REST API would match exactly your API’s representation of the same object. That makes it easy to map REST resources to hook resources and vice versa.


### Mechanism to send hooks.

Now that you have the all the other pieces in place, the only thing left to do is add the actual mechanism to POST or otherwise deliver the payload for each event to the proper target URL for each matching subscription. 

1. Compiling and POSTing the combined payload for the triggering resource and hook resource.
2. Handling responses like 410 Gone and optionally retrying connection or other 4xx/5xx errors. 

We generally recommend some sort of delayed task implementation (we detail more [performance considerations here](/docs/performance/)) but in its simplest form inline hook delivery will get the job done.

# Further Topical Readings