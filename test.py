import time
import requests
import os
from ldap3 import Server, Connection, ALL, SIMPLE
import ssl


def ldap_tls_bind(directory_host, ssl_port, dn_user, auth_key, query_base, query_filter):


    tls_context = ssl.create_default_context()
    server = Server(directory_host, port=ssl_port, use_ssl=True, tls=tls_context)
    conn = Connection(server, user=dn_user, password=auth_key, authentication=SIMPLE)


    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException("Failed to bind to LDAP server")

        conn.search(query_base, query_filter, attributes=['*'])
        return conn.entries

    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f"LDAP error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        conn.unbind()

params = {'directory_host': 'ipa.demo1.freeipa.org', 'ssl_port': 636, 'dn_user': 'cn=admin,dc=example,dc=com', 'auth_key': 'password123', 'query_base': 'dc=example,dc=com', 'query_filter': '(objectClass=*)'}
ldap_tls_bind(**params)