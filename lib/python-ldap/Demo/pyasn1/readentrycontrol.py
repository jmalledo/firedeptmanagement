#!/usr/bin/env python
"""
This sample script demonstrates the use of the pre-read control (see RFC 4527).

Originally contributed by Andreas Hasenack <ahasenack@terra.com.br>

Requires module pyasn1 (see http://pyasn1.sourceforge.net/)
"""

import ldap,ldap.sasl

from ldap.controls.readentry import PreReadControl,PostReadControl

uri = "ldap://localhost:2389/"

l = ldap.initialize(uri,trace_level=2)
l.simple_bind_s('cn=Directory Manager','Geheimer1234')

pr = PreReadControl(criticality=True,attrList=['uidNumber','gidNumber'])

msg_id = l.modify_ext(
  "cn=uidcounter,ou=Testing,dc=example,dc=com",
  [(ldap.MOD_INCREMENT, "uidNumber", "1"),(ldap.MOD_INCREMENT, "gidNumber", "1")],
  serverctrls = [pr]
)
_,_,_,resp_ctrls = l.result3(msg_id)
print "resp_ctrls[0].dn:",resp_ctrls[0].dn
print "resp_ctrls[0].entry:",resp_ctrls[0].entry

pr = PostReadControl(criticality=True,attrList=['cn'])
msg_id = l.rename(
  "cn=uidcounter,ou=Testing,dc=example,dc=com",
  "cn=uidcounter2",
  serverctrls = [pr]
)
_,_,_,resp_ctrls = l.result3(msg_id)
print "resp_ctrls[0].dn:",resp_ctrls[0].dn
print "resp_ctrls[0].entry:",resp_ctrls[0].entry
