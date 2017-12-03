# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from kis.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of kis.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if kis.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('kis.buildout'))

    def test_uninstall(self):
        """Test if kis.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['kis.buildout'])
        self.assertFalse(self.installer.isProductInstalled('kis.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IKisBuildoutLayer is registered."""
        from kis.buildout.interfaces import IKisBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IKisBuildoutLayer in utils.registered_layers())
