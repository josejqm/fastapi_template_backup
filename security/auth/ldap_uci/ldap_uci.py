from ldap3 import ALL, ALL_ATTRIBUTES, Connection, Server
from security.auth.ldap_uci.schemas import UserUciOut

#######################################
#       UCI LDAP CONFIGURATION        #
#       Powered by: MacKey-255        #
#######################################
settings = {
    'LDAP_ENABLE': True,
    'LDAP_SERVER_URL': "ldap://10.0.0.3",  # Direccion del servidor ldap
    # Usuario para inicializar
    'LDAP_DN_STRING': "cn=ad search, ou=Systems, ou=UCI Domain Impersonals, dc=uci, dc=cu",
    'LDAP_PASSWORD': 'uF2SODWAHiW0eJboFFQEAvVzJ',  # Clave del usuario a inicializar
    'LDAP_CONTEXT': 'OU=uci domain users,DC=uci,DC=cu',  # CN de los usuarios en el ldap
}


class LDAPBackend:
    """Authentication by UCI LDAP"""

    def authenticate(self, username=None, password=None) -> UserUciOut | None:
        if username is not None and password is not None:
            # Check if LDAP authentication is available
            if settings.get('LDAP_ENABLE'):
                try:
                    # Try to connect to LDAP
                    server = Server(settings.get(
                        'LDAP_SERVER_URL'), get_info=ALL)
                    with Connection(server, settings.get('LDAP_DN_STRING'), settings.get('LDAP_PASSWORD'),
                                    auto_bind=True) as connection:
                        # Search user
                        if connection.search(settings.get('LDAP_CONTEXT'), attributes=ALL_ATTRIBUTES,
                                             search_filter='(samaccountname=%s)' % (username,)):
                            # dictionary with all data of LDAP
                            results = connection.entries[0]
                            user = UserUciOut(
                                email=results['mail'].values[0],
                                display_name=results['displayName'].values[0],
                                title=results['title'].values[0],
                                username=results['sAMAccountName'].values[0])
                            # Try login using ldap data with password provide
                            if connection.rebind(results['distinguishedName'].values[0], password):
                                return user  # Login is successfully
                    return None  # User not found or not login successfully
                except Exception as ex:
                    return None  # Error in LDAP Server
        return None


ldap_uci = LDAPBackend()
