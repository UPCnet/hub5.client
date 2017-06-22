from collections import OrderedDict

ROUTES = OrderedDict()

ROUTES['users'] = dict(route='/people', category='User', name='Users', traverse='/people', actor_not_required=['POST'])

ROUTES['domains'] = dict(route='/domains', traverse='/domains')
ROUTES['domain'] = dict(route='/domains/{domain}', traverse='/domains/{domain}')

ROUTES['domain_users'] = dict(route='/domains/{domain}/users', traverse='/domains/{domain}')
ROUTES['domain_user'] = dict(route='/domains/{domain}/users/{username}', traverse='/domains/{domain}')
ROUTES['domain_contexts'] = dict(route='/domains/{domain}/contexts', traverse='/domains/{domain}')
ROUTES['domain_components'] = dict(route='/domains/{domain}/components', traverse='/domains/{domain}')

ROUTES['info'] = dict(route='info', traverse='/domains')

# DEPLOYMENT ENDPOINTS
ROUTES['api_deployments'] = dict(route='/api/deployments', traverse='/deployments')
ROUTES['api_deployment'] = dict(route='/api/deployments/{deployment}', traverse='/deployments/{deployment}')
ROUTES['api_deployment_components'] = dict(route='/api/deployments/{deployment}/components', traverse='/deployments/{deployment}')
ROUTES['api_deployment_component'] = dict(route='/api/deployments/{deployment}/components/{component}', traverse='/deployments/{deployment}')

# DOMAIN ENDPOINTS
ROUTES['api_domains'] = dict(route='/api/domains', traverse='/domains')
ROUTES['api_domain'] = dict(route='/api/domains/{domain}', traverse='/domains/{domain}')
ROUTES['api_domain_components'] = dict(route='/api/domains/{domain}/components', traverse='/domains/{domain}')

# SERVICES ENDPOINTS
ROUTES['api_domain_services'] = dict(route='/api/domains/{domain}/services', traverse='/domains/{domain}')
ROUTES['api_domain_service'] = dict(route='/api/domains/{domain}/services/{service}', traverse='/domains/{domain}')
