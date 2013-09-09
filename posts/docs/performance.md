title: Performance
author: Zapier
date: 2013-08-27


### [Home](/) > [Docs](/docs/) > {{ title }}

Properly implemented and adopted, REST Hooks can result in 66x load reduction on API servers (based on comparing polling vs. webhook implementations within Zapier).

The architecture required to run REST Hooks, however, can break away from a standard setup for a simple CRUD app, which can have only HTTP and database servers. This article will cover basic patterns to work within this architecture and ways to extend architecture to better suit hook delivery.

You have three options (all outlined below in more details)

1. Easy but Inefficient (Using Inline HTTP Requests)
2. Cheap Hack (Using a SQL-based Queue)
3. Elegant and Scalable (Using a Proper Queue)

The primary consideration is the hook delivery mechanism. This encapsulates both the query for existing subscriptions for an event and user as well as the actual HTTP call to deliver the hook payload itself (as well as handle any logic surrounding failures, retries or security).


### Easy but Inefficient (Using Inline HTTP Requests)

A simplistic implementation might just do the following any time an event might be triggered:

1. An event is triggered by a user
2. Look up any existing subscriptions for the particular event and user
3. Loop over existing subscriptions and POST the payload (very slow)
4. Perform any cleanup, failure, or retry logic
5. Return a response to the user

If you are using a synchronous programming language like PHP, Python, Ruby, etc. these actions can block. If your user is saving a form to edit the underlying record triggering the event and has a handful of subscriptions, this can delay the response by several seconds or more!

However, if you are using a language with asynchronous capabilities like Javascript, Go, etc. these actions can be pushed off onto the event loop or into a coroutine, which can be a great way to get non-blocking performance.

The same can be done (with care) for other languages using threads (Zapier's django-rest-hooks implementation does this by default in Python). But, you should probably look into using a message queue under these circumstances.


### Cheap Hack (Using a SQL-based Queue) or Elegant and Scalable (Using a Proper Queue)

Depending on your existing architecture, adding a delayed task execution for delivering hooks could be as simple as defining a new task for whatever queueing system you already have in place. On the other hand, it may require additional infrastructure (like adding Redis, ActiveMQ, RabbitMQ, or Gearman). If adding another piece of tech isn't an option, you could always implement a queue via a database table and some cron jobs (this doesn't scale very well, but does work!).

Most languages have libraries to handle task queues making this very easy (besides, task queues themselves are good practices).

The basic idea is:

1. An event is triggered by a user
2. Insert a task to deliver hooks for the event and user (very fast)
3. Return a response to the user
4. (Inside the task) Look up any existing subscriptions for the particular event and user
5. (Inside the task) Loop over existing subscriptions and POST the payload (very slow)
6. (Inside the task) Perform any cleanup, failure, or retry logic

Because step 4 and 5 are moved into a task that is running in the background, it no longer blocks our response to the user. This maintains a high level of responsiveness for the user, increases likeliness of task success (especially when isolating and fanning out new tasks for each event and subscription) and parallelizes tasks, delivering them faster.


## Batching

Sending a large number of hooks at the same time for very similar or duplicate events is a behavior that may be unwanted. For example, if a user makes a dozen fast edits to a single record, a naive implementation would send a dozen "item updated" event hooks. This example also illustrates the importance of delivery order: if the most recent event isn't the last one received, the client's state will be incorrect.

Another example is when a user does a mass edit or import task that touches hundreds, thousands or even *millions* of records. A naive implementation would simply attempt to do an equal number of hooks.

There are a few ways to handle this:

1. Debouncing or deduplicating update events: only send the most recent event hook instead of several events of very similar type.
2. Batching massive jobs: instead of sending thousands of individual hooks, bundle them up into a single hook.

Both options can add quite a bit of overhead due to the nature of event aggregation and delayed releasing. For example, #1 would have to hold all update events for some time period (maybe 15 seconds or so) to give the user a chance to edit and issue another update event to delay it once again. Once the delay expires, the hook is delivered for the most recent event.


## Skinny Payloads

Another option (especially within the context of massive batching or special systems like file syncing) would be sending more lightweight payloads. The most extreme would be the unique ID for the changed resource, on the other end of the spectrum, you'd send an entire snapshot of the newly changed resource.

A skinny payload has two general benefits for performance:

1. Less outbound bandwidth consumed for delivering payloads
2. Less internal resources consumed to process payloads
