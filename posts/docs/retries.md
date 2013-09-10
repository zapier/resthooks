title: Delivery Failure & Retries
author: Zapier
date: 2013-08-27


### [Home](/) > [Docs](/docs/) > {{ title }}

REST Hooks alleviates consumers from having to continuously poll for changes by having REST Hook providers push new data to them when it becomes available, but what happens when those consumers themselves are unavailable?

Even the most well designed infrastructure will sooner or later experience an outage of some form and without any retry mechanism in place, consumers will miss updates they are interested in. So when providing a REST Hooks base interface we implement retries to ensure consumers get the updates they are subscribing to. 


### When Do We Retry?

There are several instances when a Sender should retry to ensure
delivery. A response status code of 2xx indicating that the action
requested by the Sender was received, understood, accepted and processed
successfully should be treated as a message delivery acknowledgment. No
need to redeliver sent messages in those cases. 

Responses in the 3xx range can be a little tricky. The Sender may
opt to dynamically update hook subscriptions based on what it may
receive along with these status codes. However, the
the Sender may decide to either retry or fail when these occur and insist that the
hook subscription be updated through the API.

When a Receiver sends a response status code in the 4xx range the Sender
should usually attempt to retry. Services can sometimes have temporary 
Not Found (404) or failed authentication errors (401), so status codes
like these shouldn't immediately mark the subscription as bad until it
can be proven that the Receiver's endpoint has a consistent 404 over
time. An exception to this could be a 410 (Gone) status code which indicates
that the Receiver should immediately cancel the subscription as the
resource is no longer available. Again, it is all up to the Sender to
decide how this is handled.

Since response status codes in the 5xx range always indicate an internal
failure some sort a retry should definitely be scheduled when they
occur. Likewise, a network issue such as a connection reset or connection
timeout fall into unforeseen circumstances and should be retried, as well.

<table>
  <tr>
    <th>Response</th>
    <th>Retry?</th>
  </tr>
  <tr>
    <td>2xx</td>
    <td><i class="icon-remove-sign"></i></td>
  </tr>
  <tr>
    <td>3xx</td>
    <td><i class="icon-remove-sign"></i></td>
  </tr>
  <tr>
    <td>4xx</td>
    <td><i class="icon-check-sign success"></i></td>
  </tr>
  <tr>
    <td>410</td>
    <td><i class="icon-remove-sign"></i></td>
  </tr>
  <tr>
    <td>5xx</td>
    <td><i class="icon-check-sign success"></i></td>
  </tr>
  <tr>
    <td>Timed Out</td>
    <td><i class="icon-check-sign success"></i></td>
  </tr>
</table>

### Exponential Back Off

We've covered when a Sender should retry, but how to we keep from
retrying indefinitely? If the Sender has hooks being sent frequently to
a Receiver and it goes dark, the retries will start building up and
expotentially increase the throughput to the Receiver. Over time the
number of requests being sent will be increase to the point that the 
Receiver might get so overwhelmed when it comes back up that
it might go down again. Ahhhh!!!

One recommended solution is to implement an exponential back off policy.
For example, hooks sent to a Receiver that begin getting failed response
status codes should trigger retries five seconds later, then thirty
seconds, five minutes, an hour and so on. The Sender keeps increasing
the interval since the last failed retry until hooks haven't been
successful for a certain period of time such as a day. Determining the
right interval to retry largely depends on the the service level
agreement between the Sender and Receiver. After a certain period of
time or maximum number of retries the subscription may be marked as inactive or removed.

This leaves a lot ambiguity. How do we let the Receiver know when the
subscription is cancelled? How do we implement the retry mechanism? Or
if hooks represent state changes for a resource on the Sender's end how
can the Receiver make sure that messages received out of order don't
lead to an invalid state?


### Ensuring Ordered Delivery

In some situations, the hooks sent to a consumer may be dependent on
some ordering. For example, what if a Sender sends hooks for several
events on the following object:

1. Create object
2. Update object
3. Update object again
4. Delete object

If the Receiver is down and misses the first create message but comes up
in time to catch the delete and then receives the retried hook for the
create event it may consider the resource as having just been created. 

One solution is to have each message include a sequence ID of some sort.
This would mean that it is up to the Receiver to implement a
[resequencer](http://www.enterpriseintegrationpatterns.com/Resequencer.html)
to put hooks received out of order back in the correct order.

### Variation: Claim Check

An alternative to the exponential back off policy is to implement a
[Claim Check pattern](http://eaipatterns.com/StoreInLibrary.html) for
messages that were not received successfully by the Receiver. In this
scenario, failed hooks are stored in a special holding area until
claimed by the Receiver. Receivers claim the hooks by fetching from a
URL specified by the Sender. 

One straightforward way to implement Claim Checks is to provide the URL
up front that Receivers can check for a log of all failed hook
notifications. This allows Receivers the freedom to retrieve this URL any time they think they have missed a hook.

Another pattern is to stop sending hook notifications to the Sender
after a certain number of failures and begin periodically sending a hook
notification with a URL that can be used to retrieve missed messages. The Sender keeps sending this hook at regular intervals until it is either claimed or expires. 

Retrieving messages with a claim check can be a manual process on the Receiver's side, or a release mechanism on the Sender's side. In the first case, the Receiver needs to go out and fetch those messages from the Sender itself. In the second instance, requesting the claim URL instructs the Sender to release the missed messages and resend them.

