# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from test.template.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of test.template into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if test.template is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('test.template'))

    def test_uninstall(self):
        """Test if test.template is cleanly uninstalled."""
        self.installer.uninstallProducts(['test.template'])
        self.assertFalse(self.installer.isProductInstalled('test.template'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ITestTemplateLayer is registered."""
        from test.template.interfaces import ITestTemplateLayer
        from plone.browserlayer import utils
        self.assertTrue(ITestTemplateLayer in utils.registered_layers())
