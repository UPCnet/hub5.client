# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from hub5.client.testing import HUB5_CLIENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that hub5.client is properly installed."""

    layer = HUB5_CLIENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if hub5.client is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'hub5.client'))

    def test_browserlayer(self):
        """Test that IHub5ClientLayer is registered."""
        from hub5.client.interfaces import (
            IHub5ClientLayer)
        from plone.browserlayer import utils
        self.assertIn(IHub5ClientLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = HUB5_CLIENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['hub5.client'])

    def test_product_uninstalled(self):
        """Test if hub5.client is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'hub5.client'))

    def test_browserlayer_removed(self):
        """Test that IHub5ClientLayer is removed."""
        from hub5.client.interfaces import \
            IHub5ClientLayer
        from plone.browserlayer import utils
        self.assertNotIn(IHub5ClientLayer, utils.registered_layers())
