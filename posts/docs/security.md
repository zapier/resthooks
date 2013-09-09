title: Security
author: Zapier
date: 2013-08-27


### [Home](/) > [Docs](/docs/) > {{ title }}

## Use Existing API Authentication

The first step to a secure REST Hook implementation is to make use of the existing authentication mechanism for the Sender's API. When setting up the subscription, the API calls to do the handshake should include the standard authentication mechanism (Basic Auth, API key, OAuth access token, etc.).

There are two broad patterns to ensure the integrity of your hooks:

1. Be very careful who is allowed to receive hooks (indentity confirmation, signatures, etc.)
2. Don't send any sensitive information at all (notification only, skinny payloads)


## Identity Confirmation

To ensure that a Receiver actually intends to receive hooks from a Sender and that the hooks are really from the Sender, it is often wise to have some checks in place to confirm both intent and legitimacy.


### Confirming Receiver's Intent to Subscribe

To ensure that a Receiver actually intends to receive hooks from a Sender, a subscription uses a temporary secret in the initial handshake.

When the Sender responds to the Receiver's first POST request, the response includes a `X-Hook-Secret` header that has a unique string as its value. A unique value should be computed for each new subscription.

Upon receiving the secret from the Sender, the Receiver needs to do one of two things:

### Option 1 (Immediate Confirmation)

![Subscription Handshake Diagram]({{STATIC_URL}}/img/subscription_handshake_diagram.png)

In this case, the Receiver returns a `200` response with the secret included in the `X-Hook-Secret` header.

### Option 2 (Delayed Confirmation)

![Delayed Subscription Handshake Diagram]({{STATIC_URL}}/img/subscription_handshake_delayed_diagram.png)

In this case, the Receiver returns a `200` response without the secret, then later sends another request to the Sender with the secret in the header.

In the first case, the Sender will activate the subscription immediately and begin sending updates. In the second case, the Sender should treat the subscription as inactive and not provide updates. Once the Receiver sends the second request to confirm the secret, the Sender can consider the subscription active.

### Confirming Hook Legitimacy

To prove the authenticity of subsequent messages, the Sender can use a shared secret (think API key or OAuth client_secret).

For each message, the Sender signs the message by computing an HMAC of the shared secret plus request body and placing the signature in the `X-Hook-Signature` header. The Receiver then verifies the signature to know that the message is authentic. Verification is as simple as computing the same HMAC and comparing it to the `X-Hook-Signature` header value.

![Example Hook with Sender Signature]({{STATIC_URL}}/img/hook_diagram.png)

## Skinny Payloads

Another way to secure messages is to replace the payload with a URL or unique ID for the resource rather than a full representation of the resource. Under this paradigm, the hook acts more like a "notification," telling the Receiver to make the necessary API calls to complete the transaction. The benefit of this approach is that the Receiver must make an authenticated API call to obtain data, so access can be regulated via normal means.

