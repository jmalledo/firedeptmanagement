#!/usr/bin/env python
"""
ldap.controls.readentry - classes for the Read Entry controls
(see RFC 4527)

See http://www.python-ldap.org/ for project details.

$Id: readentry.py,v 1.1 2011/04/07 21:45:16 stroeder Exp $
"""

import ldap

from pyasn1.codec.ber import encoder,decoder
from ldap.controls import LDAPControl,KNOWN_RESPONSE_CONTROLS

from pyasn1_modules.rfc2251 import AttributeDescriptionList,SearchResultEntry


class ReadEntryControl(LDAPControl):
  """
  Base class for control described in RFC 4527
  """

  def __init__(self,criticality=False,attrList=None):
    self.criticality,self.attrList,self.entry = criticality,attrList or [],None

  def encodeControlValue(self):
    attributeSelection = AttributeDescriptionList()
    for i in range(len(self.attrList)):
      attributeSelection.setComponentByPosition(i,self.attrList[i])
    return encoder.encode(attributeSelection)

  def decodeControlValue(self,encodedControlValue):
    decodedEntry,_ = decoder.decode(encodedControlValue,asn1Spec=SearchResultEntry())
    self.dn = str(decodedEntry[0])
    self.entry = {}
    for attr in decodedEntry[1]:
      self.entry[str(attr[0])] = [ str(attr_value) for attr_value in attr[1] ]


class PreReadControl(ReadEntryControl):
  controlType = ldap.CONTROL_PRE_READ

KNOWN_RESPONSE_CONTROLS[PreReadControl.controlType] = PreReadControl


class PostReadControl(ReadEntryControl):
  controlType = ldap.CONTROL_POST_READ

KNOWN_RESPONSE_CONTROLS[PostReadControl.controlType] = PostReadControl
