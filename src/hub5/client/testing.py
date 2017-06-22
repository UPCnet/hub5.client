# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import hub5.client


class Hub5ClientLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=hub5.client)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'hub5.client:default')


HUB5_CLIENT_FIXTURE = Hub5ClientLayer()


HUB5_CLIENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(HUB5_CLIENT_FIXTURE,),
    name='Hub5ClientLayer:IntegrationTesting'
)


HUB5_CLIENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(HUB5_CLIENT_FIXTURE,),
    name='Hub5ClientLayer:FunctionalTesting'
)


HUB5_CLIENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        HUB5_CLIENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='Hub5ClientLayer:AcceptanceTesting'
)
