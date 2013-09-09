title: Retries
author: Zapier
date: 2013-08-27


### [Home](/) > [Docs](/docs/) > {{ title }}

REST Hooks alleviate service consumers from having to continuously poll for changes by having senders push new data to consumers when it becomes available, but what happens when those consumers are unavailable?

Even the most well designed infrastructure will sooner or later experience an outage of some form and without any retry mechanism in place, consumers will miss updates they are interested in. So when providing a REST Hooks base interface we implement retries to ensure consumers get the updates they are subscribing to. 


### When Do We Retry?

There are several instances where a sender should retry to ensure delivery. A response status code of 2xx indicating that the action requested by the sender was received, understood, accepted and processed successfully should be treated as a message delivery acknowledgment. No need to redeliver sent messages in that case.

Whenever there is a network issue such as a connection reset or timeout, the Sender should attempt redelivery as network related problems are completely unexpected behavior. Additionally, anytime a server returns a response status code in the 5xx range redelivery should be attempted as these indicate a server error on the receiver's side.

Likewise, whenever a response status code in the 4xx range is returned by a Receiver, a retry should be scheduled. Services can sometimes have temporary not found (404) or failed authentication errors (401), so this shouldn't immediately mark the subscription as bad. The only immediate exceptions are gone (410) and similar response codes that should immediately cancel the subscription.


### Exponential Back Off

Retries should implement an exponential back off policy. For example, hooks sent to subscribed URLs that are failures should trigger retries 5 seconds later, then 30 seconds, 5 minutes, an hour and so on. The Sender keeps increasing the interval since the last retry until hooks haven't been successful for a day. Determining the right interval to retry largely depends on the demands of your application. After a certain period of time or maximum number of retries the subscription should be marked as inactive or removed.

Even this leaves a lot ambiguity. How do we let the receiver know when the subscription is cancelled? How do we implement the retry mechanism? Or the most difficult question of all, if hooks represent state changes for a resource how can the receiver make sure that messages received out of order don't lead to invalid state?


### Ensuring Ordered Delivery

In some situations, the hooks sent to a consumer may be dependent on some ordering. For example, what if a sender sends hooks for a single object:

1. create object
2. update object
3. update object again
4. delete object

If the receiver is down and misses the first create message, receiving the update or delete hooks is unexpected behavior. Additionally, the delayed arrival of the create hook after the delivery of the delete hook will cause even more havoc.

One solution is to have each message include a sequence ID of some sort. This would mean it is up to the receiver to implement a [resequencer](http://www.enterpriseintegrationpatterns.com/Resequencer.html) to put hooks received out of order back in order and reduces the overhead on the sender'''s side.

Another solution is to not include a full representation, but instead a single unique ID for the underlying resource. In this scenario, the receiver can make the assumption that it can manually fetch the most recent version of the resource, making the actual event type or payload content of lesser importance (IE: an "item created" hook with an ID that gives a 404 when fetched indicates to the Receiver the item was later deleted).


## Variation: Claim Check

An alternative to the exponential back off pattern is the [Claim Check pattern](http://eaipatterns.com/StoreInLibrary.html). In this scenario, failed hooks are stored in a special holding area until claimed by the Receiver. Receivers claim the hooks by fetching a sender-specified URL.

One straightforward way to implement Claim Checks is to provide the URL up front that receivers can check for a log of all sent (and failed) hooks. This allows receivers the freedom to retrieve this url any time they think they have missed a hook.

Another pattern is to, while the receiver is down, periodically send a hook with a URL that can be used to retrieve missed messages. The sender keeps sending this hook at regular intervals until  it is either claimed or expires. 

Retrieving messages with a claim check can be a manual process on the receiver's side, or a release mechanism on the sender's side. In the first case, the receiver needs to go out and fetch those messages from the sender itself. In the second instance, requesting the claim url instructs the sender to release the missed messages and resend them.

