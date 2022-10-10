from .project_data import *
from cryptography import x509
from cryptography.x509.oid import NameOID
import idna
from socket import socket
from OpenSSL import SSL

# this 4 functions are used fot the ssl certificate

def getSSL(siteUrl, index):
    print('\n--', siteUrl, 'getSSL---IN\n')
    hostinfo = get_certificate(siteUrl, 443)
    string = print_basic_info(hostinfo)
    string.replace("'", "")
    if (CurrentDate > hostinfo.cert.not_valid_after):
        c.execute(
            "UPDATE urls SET SSL_EXPIRED = '{}' WHERE domain = '{}' and date_id={}".format("True", siteUrl, date_id))

    else:
        c.execute(
            "UPDATE urls SET SSL_EXPIRED = '{}' WHERE domain = '{}' and date_id={}".format("False", siteUrl, date_id))

    c.execute("UPDATE urls SET SSL = '{}' WHERE domain = '{}' and date_id={}".format(string, siteUrl, date_id))
    print('\n--', siteUrl, 'getSSL---OUT\n')
#    conn.commit()

def get_issuer(cert):
    try:
        names = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
        return (names[0].value).replace("'", "")
    except x509.ExtensionNotFound:
        return None


def get_certificate(hostname, port):
    hostname_idna = idna.encode(hostname)
    sock = socket()

    sock.connect((hostname, port))
    peername = sock.getpeername()
    ctx = SSL.Context(SSL.SSLv23_METHOD)  # most compatible
    ctx.check_hostname = False
    ctx.verify_mode = SSL.VERIFY_NONE

    sock_ssl = SSL.Connection(ctx, sock)
    sock_ssl.set_connect_state()
    sock_ssl.set_tlsext_host_name(hostname_idna)
    sock_ssl.do_handshake()
    cert = sock_ssl.get_peer_certificate()
    crypto_cert = cert.to_cryptography()
    sock_ssl.close()
    sock.close()

    return HostInfo(cert=crypto_cert, peername=peername, hostname=hostname)


def print_basic_info(hostinfo):
    s = '''issuer: {issuer}, notBefore: {notbefore}, notAfter:  {notafter}
    '''.format(
        issuer=get_issuer(hostinfo.cert),
        notbefore=hostinfo.cert.not_valid_before,
        notafter=hostinfo.cert.not_valid_after
    )
    return (s)

