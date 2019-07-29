.. _api:

Developer Interface
===================

This page of the documentation will cover all methods and classes available to the developer.

The api currently has two main interfaces:

- `App API`_
    - :class:`instascrape.Client`
    - :class:`instascrape.ClientCompatPatch`
    - :class:`instascrape.ClientError`
    - :class:`instascrape.ClientLoginError`
    - :class:`instascrape.ClientLoginRequiredError`
    - :class:`instascrape.ClientCookieExpiredError`
    - :class:`instascrape.ClientThrottledError`
    - :class:`instascrape.ClientReqHeadersTooLargeError`
    - :class:`instascrape.ClientConnectionError`
    - :class:`instascrape.ClientCheckpointRequiredError`
    - :class:`instascrape.ClientChallengeRequiredError`
    - :class:`instascrape.ClientSentryBlockError`
    - :class:`instascrape.MediaRatios`
    - :class:`instascrape.MediaTypes`

- `Web API`_
    - :class:`instascrape.web.Client`
    - :class:`instascrape.web.ClientCompatPatch`
    - :class:`instascrape.web.ClientError`
    - :class:`instascrape.web.ClientCookieExpiredError`
    - :class:`instascrape.web.ClientConnectionError`
    - :class:`instascrape.web.ClientBadRequestError`
    - :class:`instascrape.web.ClientForbiddenError`
    - :class:`instascrape.web.ClientThrottledError`


App API
-----------

.. automodule:: instascrape

.. autoclass:: Client
   :special-members: __init__
   :inherited-members:

.. autoclass:: ClientCompatPatch
   :special-members: __init__
   :inherited-members:

.. autoexception:: ClientError
.. autoexception:: ClientLoginError
.. autoexception:: ClientLoginRequiredError
.. autoexception:: ClientCookieExpiredError

.. autoclass:: MediaRatios
   :members:

.. autoclass:: MediaTypes
   :members:

Web API
-------------------

.. automodule:: instascrape.web

.. autoclass:: Client
   :special-members: __init__
   :inherited-members:

.. autoclass:: ClientCompatPatch
   :special-members: __init__
   :inherited-members:

.. autoexception:: ClientError
.. autoexception:: ClientLoginError
.. autoexception:: ClientCookieExpiredError
