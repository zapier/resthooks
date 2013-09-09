title: Alternatives
author: Zapier
date: 2013-08-27


### [Home](/) > [Docs](/docs/) > {{ title }}

When it comes to real time communication, the collection of patterns surrounding REST Hooks do not stand alone. There are other options, many of them quite mature and are in production across a handful of vendors. 


## Long-polling or Comet

Long-polling is a bit of a clever hack on normal polling. It is more efficient than repeatedly asking "any new data? any new data?" every couple minutes with a brand new GET request because it just leaves the first GET request open until there is new data. After receiving that new data and closing the original connection, the client initiates another connection for the next bit of information.

Long polling between servers generally requires a daemon that monitors and manages long lived connections and processes. Languages that are inherently asynchronous (like Javascript or Go) make this easier, but it is still quite a bit of state to manage on both client and server. Unfortunately, long polling isn't *much* of an improvement over regular polling. However, long polling is used in production in a few places on the web and most existing infrastructures have quite a bit of common ground.

Comet is a loose collection of patterns around long-polling and other browser workarounds (for example, hidden iframes long polling for changes, passing them to the parent). Now that browsers mostly support websockets, Comet is becoming less and less common.

The use of long-polling and Comet is discouraged, existing implementations at Facebook, Twitter and elsewhere are already deprecated and pending removal.


## Websockets

Websockets are extremely flexible and create a persistent connection ready for full two way communication. They are fairly lightweight and have mature libraries in most languages.

However, like long polling, they require another piece of infrastructure that monitors and manages these long lived connections and processes. Languages that aren't inherently asynchronous will need specialized libraries to deal with threads and extra processes. It's also not very common today and doesn't share a lot of common ground with existing infrastructure.

Websockets also require a minimum level of resources at scale. Websocket connections that are hibernating or otherwise silent still need to be maintained which require at least a small portion of resources.

Websockets and similar constructs are wonderful for APIs where real-time is business critical (perhaps for real-time stock updates), websockets are the best choice. For the average CRUD style web application, webhooks are a more natural way to approximate less chatty communications.


## Classic webhooks

Classic, or user managed, webhooks get closer to the ideal event notification system. The server POSTs a payload to some user defined URL. There is almost zero overhead on the client side; they just handle the POST requests like normal.

Webhooks reuse tons of existing architecture: all notifications are HTTP based and most web services have quite a bit of expertise making and handling such requests. However, they have one big drawback: they are a very poor experience for the user. Copy-pasting obscure URLs between two services' settings pages is a major hurdle.


## XMPP

The Extensible Messaging and Presence Protocol (XMPP) is one popular protocol that while originally developed and used as part of jabber for chat-based applications, it is also used for bidirectional communication between servers. The binding method, [Bidirectional-streams Over Synchronous HTTP (BOSH)](http://xmpp.org/extensions/xep-0124.html), allows for messages to be pushed to subscribers as soon as they become available by emulating persistent, long lived connections while under the hood they still use HTTP polling but in an optimized manner. 

Messages sent between XMPP aware nodes are in xml although they may additionally include different data formats embedded within them (such is the case with the `<json:json>` node). A major strength that users gain by using XMPP is that they can rely on its long history and well defined open standard when building XMPP aware applications. This also means several good libraries exist for it and consumer applications that may not have a public address or are behind a firewall can still communicate with other servers.

On the downside, users might be a little overwhelmed with the complexities involved with implementing the specification and may find the protocol, while lightweight, simply not well suited to their needs. Also, unlike REST Hooks where HTTP traffic only occurs when notifications are sent, XMPP has ongoing traffic to maintain the connection (albeit lightweight).


## New protocol or specification

There have been proposals for extending the HTTP specification itself with SUBSCRIBE and UNSUBSCRIBE methods (via WebDAV). Partially due to the fact that it wasn't adopted into the core specifications, they have not caught on and only a handful of services implement it. Unfortunately, the red tape and bureaucracy involved to officially include subscription HTTP methods are prohibitive.

There have also been a handful of HTTP Subscription specifications that live within the existing HTTP specification itself. For example, using an X-Callback header to define callbacks during a POST to an /api/subscription endpoint. This closely approximates the REST Hooks ethos, with the minor variation in that the request body should define the subscription resource (just like the rest of your REST API).

