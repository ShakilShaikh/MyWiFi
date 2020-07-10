# -*- coding: utf-8 -*-

"""
MyWiFi.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.
"""

class RequestException(Exception):
    """There was an ambiguous exception that occurred while handling your
    request.
    """

    def __init__(self, *args, **kwargs):
        """Initialize RequestException with `request` and `response` objects."""
        response = kwargs.pop('response', None)
        self.response = response
        self.request = kwargs.pop('request', None)
        if (response is not None and not self.request and
                hasattr(response, 'request')):
            self.request = self.response.request
        super(RequestException, self).__init__(*args, **kwargs)


class DefaultKeyError(RequestException):
    """ Missing Default Network Name """


class WiFiConnectionError(RequestException):
    """Failed to connect for driver"""

class WiFiScanningError(RequestException):
    """Error While Scan maybe for driver"""

class AuthenticationError(RequestException):
    """When a WiFi profile is not saved"""

class WiFiOutOfRange(RequestException):
    """If the network is down or out of range"""
class DriverError(RequestException):
    """When WLAN driver not found"""

Exname = __name__
