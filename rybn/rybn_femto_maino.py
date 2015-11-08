#!/usr/bin/env python
# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
import sys
import json
import ast
from twisted . internet import reactor
from twisted . internet . protocol import Protocol , Factory , ServerFactory
from rybn_femto_como import IiiIII111iI
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
print "Script principal de La Labomedia chez rybn"
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
if 94 - 94: i1IIi % Oo0Ooo
o0oO0 = IiiIII111iI ( "rybn_femto.ini" )
oo00 = o0oO0 . conf
if 88 - 88: iII111i . oO0o % ooOoO0o
if 66 - 66: iII111i
if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - oO0o
class ooO00oOoo ( Protocol ) :
 if 78 - 78: I11i / OoO0O00 - O0 . IiII
 def __init__ ( self , factory ) :
  if 91 - 91: I1ii11iIi11i * iIii1I11I1II1 . IiII / Ii1I
  self . factory = factory
  if 87 - 87: i1IIi / Ii1I . OoO0O00 * OoooooooOO - IiII * ooOoO0o
  self . debug = False
  if 82 - 82: I11i . I1Ii111 / IiII % II111iiii % iIii1I11I1II1 % IiII
 def connectionMade ( self ) :
  if 86 - 86: OoOoOO00 % I1IiiI
  self . factory . numProtocols = self . factory . numProtocols + 1
  if 80 - 80: OoooooooOO . I1IiiI
  if 87 - 87: oO0o / ooOoO0o + I1Ii111 - ooOoO0o . ooOoO0o / II111iiii
 def connectionLost ( self , reason ) :
  self . factory . numProtocols = self . factory . numProtocols - 1
  if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
 def dataReceived ( self , data ) :
  if 58 - 58: i11iIiiIii % I1Ii111
  if self . debug :
   print ( "Raw data = {}" . format ( data ) )
   if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
  try :
   iIiiI1 = data . decode ( "utf-8" )
  except :
   iIiiI1 = data
   print "Error sur decode"
   if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
   if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
  try :
   i1iIIi1 = ast . literal_eval ( iIiiI1 )
  except :
   i1iIIi1 = iIiiI1
   if 50 - 50: i11iIiiIii - Ii1I
   if 78 - 78: OoO0O00
   if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
  self . message_sorting ( i1iIIi1 )
  if 62 - 62: iII111i - IiII - OoOoOO00 % i1IIi / oO0o
 def message_sorting ( self , msg ) :
  global mymoney
  if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
  if 14 - 14: I11i % O0
  if "Ordre" in msg :
   if isinstance ( msg , dict ) :
    IiI1I1 = msg [ "Ordre" ]
   else :
    IiI1I1 = msg
   print ( "\nMessage reçu de miskin = {}\n" . format ( IiI1I1 ) )
   o0oO0 . send_to_rybn ( IiI1I1 )
   if 86 - 86: i11iIiiIii + Ii1I + ooOoO0o * I11i + o0oOOo0O0Ooo
   if 61 - 61: OoO0O00 / i11iIiiIii
  if "Retour info" in msg :
   o0oO0 . send_info_to_labomedia ( )
   if 34 - 34: OoooooooOO + iIii1I11I1II1 + i11iIiiIii - I1ii11iIi11i + i11iIiiIii
   if 65 - 65: OoOoOO00
  if "quit" in msg :
   sys . exit ( )
   if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
   if 84 - 84: i11iIiiIii . o0oOOo0O0Ooo
class o0O00oooo ( Factory ) :
 def __init__ ( self ) :
  self . numProtocols = 0
  if 67 - 67: OOooOOo / OoooooooOO % I11i - iIii1I11I1II1
 def buildProtocol ( self , addr ) :
  return ooO00oOoo ( self )
  if 82 - 82: i11iIiiIii . OOooOOo / Oo0Ooo * O0 % oO0o % iIii1I11I1II1
  if 78 - 78: iIii1I11I1II1 - Ii1I * OoO0O00 + o0oOOo0O0Ooo + iII111i + iII111i
  if 11 - 11: iII111i - OoO0O00 % ooOoO0o % iII111i / OoOoOO00 - OoO0O00
def o0o0oOOOo0oo ( ) :
 global oo00
 if 80 - 80: I11i * i11iIiiIii / I1Ii111
 I11II1i = oo00 [ "network_in" ] [ "port" ]
 print ( "   Réception sur le port {}\n" . format ( I11II1i ) )
 if 23 - 23: I1ii11iIi11i / o0oOOo0O0Ooo + I11i + I11i / II111iiii
 reactor . listenTCP ( I11II1i , o0O00oooo ( ) )
 reactor . run ( )
 if 26 - 26: OoooooooOO
 if 12 - 12: OoooooooOO % OoOoOO00 / ooOoO0o % o0oOOo0O0Ooo
if __name__ == '__main__' :
 o0o0oOOOo0oo ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
