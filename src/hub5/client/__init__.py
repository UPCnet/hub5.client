# -*- coding: utf-8 -*-
from max5.client.client import get_max_info
from max5.client.client import get_max_url_from_hub_domain
from max5.client.rest import MaxClient
from hub5.client.routes import ROUTES


class HubClient(MaxClient):
    __routes__ = ROUTES
    __defaults__ = {}

    def __init__(self, domain, hub, max_server=None, **kwargs):
        self.__max_server__ = max_server
        self.domain = domain
        kwargs['oauth_server'] = None
        super(HubClient, self).__init__(hub, **kwargs)

    @property
    def max_server(self):
        if self.__max_server__ is None:
            self.__max_server__ = get_max_url_from_hub_domain(self.url, self.domain)
        return self.__max_server__

    @property
    def oauth_server(self):
        if self.__oauth_server__ is None:
            max_info = get_max_info(self.max_server)
            self.__oauth_server__ = max_info['max.oauth_server']
        return self.__oauth_server__.rstrip('/')

    def OAuth2AuthHeaders(self):
        """
        """
        headers = {

            'X-Oauth-Token': str(self.token),
            'X-Oauth-Username': str(self.actor['username']),
            'X-Oauth-Scope': str(self.scope),
            'X-Oauth-Domain': str(self.domain),

        }
        return headers
