#!/usr/bin/python
# -*- coding: UTF-8 -*-
if 64 - 64: i11iIiiIii
import socket
import json
from time import sleep
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
class IiII1IiiIiI1 ( object ) :
 if 40 - 40: oo * OoO0O00
 if 2 - 2: ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o . oOoO0oo0OOOo + iiiiIi11i
 def __init__ ( self , ip , port ) :
  self . ip = ip
  self . port = port
  self . data = None
  self . sock = None
  self . create_socket ( )
  if 24 - 24: II11iiII / OoOO0ooOOoo0O + o0000oOoOoO0o * i1I1ii1II1iII % oooO0oo0oOOOO
 def create_socket ( self ) :
  while not self . sock :
   if 53 - 53: o0oo0o / Oo + o0oo0o / oooO0oo0oOOOO * OoooooooOO + i1I1ii1II1iII
   try :
    self . sock = socket . socket ( socket . AF_INET , socket . SOCK_STREAM )
    OOo0oO0oooOoO = ( self . ip , self . port )
    if 72 - 72: II111iiii - oOo0O0Ooo
    self . sock . setblocking ( 0.3 )
    if 91 - 91: ooOO00oOo . i11iIiiIii / iiiiIi11i % OoOO0ooOOoo0O / ooOO00oOo - i11iIiiIii
    if 8 - 8: Ooo00oOo00o * oOoO0oo0OOOo * iIii1I11I1II1 . oooO0oo0oOOOO / oooO0oo0oOOOO % oooO0oo0oOOOO
    self . sock . connect ( OOo0oO0oooOoO )
   except :
    pass
    if 22 - 22: o0000oOoOoO0o . oooO0oo0oOOOO
    if 41 - 41: o0oo0o . Oo * oooO0oo0oOOOO % i11iIiiIii
   sleep ( 0.1 )
   if 74 - 74: i1I1ii1II1iII * oooO0oo0oOOOO
   if 82 - 82: iIii1I11I1II1 % oooO0oo0oOOOO
 def send ( self , msg ) :
  if 86 - 86: oOo0O0Ooo % oo
  if 80 - 80: OoooooooOO . oo
  if 87 - 87: iiiiIi11i / Oo + o0oo0o - Oo . Oo / II111iiii
  if 11 - 11: oo % Ooo00oOo00o - OoO0O00
  if 58 - 58: i11iIiiIii % o0oo0o
  if 54 - 54: II11iiII % O0 + oo - i1I1ii1II1iII / OoOO0ooOOoo0O
  if 31 - 31: ooOO00oOo + II111iiii
  if isinstance ( msg , int ) :
   i11IiIiiIIIII = json . dumps ( msg )
  elif isinstance ( msg , float ) :
   i11IiIiiIIIII = json . dumps ( msg )
  elif isinstance ( msg , str ) :
   i11IiIiiIIIII = json . dumps ( msg , ensure_ascii = False )
  elif isinstance ( msg , dict ) :
   i11IiIiiIIIII = json . dumps ( msg , ensure_ascii = False )
  elif isinstance ( msg , list ) :
   i11IiIiiIIIII = json . dumps ( msg , ensure_ascii = False )
  else :
   print "Le message ne peut pas être envoyé"
   i11IiIiiIIIII = "Erreur client"
   if 22 - 22: o0000oOoOoO0o * O0 / Ooo00oOo00o
  try :
   self . sock . send ( i11IiIiiIIIII + "\n" )
   if 64 - 64: o0000oOoOoO0o % i1IIi % OoooooooOO
   if 3 - 3: i1I1ii1II1iII + O0
  except :
   print "Envoi par femto_client.py raté"
   self . reconnect ( )
   if 42 - 42: II11iiII / i1IIi + i11iIiiIii - o0000oOoOoO0o
 def reconnect ( self ) :
  self . sock = None
  self . create_socket ( )
  if 78 - 78: ooOO00oOo
 def close ( self ) :
  self . sock . close ( )
  self . sock = None
  if 18 - 18: O0 - i1I1ii1II1iII / i1I1ii1II1iII + Oo % Oo - oooO0oo0oOOOO
 def listen ( self ) :
  O0O00Ooo = None
  if 64 - 64: iiiiIi11i - O0 / II111iiii / Ooo00oOo00o / iIii1I11I1II1
  try :
   O0O00Ooo = self . sock . recv ( )
  except :
   print ( "Je n'ai rien reçu" )
  return O0O00Ooo
  if 24 - 24: O0 % Ooo00oOo00o + i1IIi + o0oo0o + oOoO0oo0OOOo
  if 70 - 70: OoO0O00 % OoO0O00 . oooO0oo0oOOOO % ooOO00oOo * Ooo00oOo00o % iiiiIi11i
if __name__ == "__main__" :
 if 23 - 23: i11iIiiIii + oo
 import default_order_dict as dod
 if 68 - 68: oOo0O0Ooo . iiiiIi11i . i11iIiiIii
 if 40 - 40: iiiiIi11i . oOo0O0Ooo . OoO0O00 . i1IIi
 I11iii = 2
 if 54 - 54: II11iiII + II11iiII % o0oo0o % i11iIiiIii / iIii1I11I1II1 . II11iiII
 if 57 - 57: o0000oOoOoO0o % OoooooooOO
 for O00 in [ 5 ] :
  if 11 - 11: oo
  if O00 == 5 :
   O0o0Oo = "193.248.161.88"
   Oo00OOOOO = 6666
   O0O = IiII1IiiIiI1 ( O0o0Oo , Oo00OOOOO )
   if 83 - 83: OoOO0ooOOoo0O + II111iiii * Ooo00oOo00o % ooOO00oOo + OoOO0ooOOoo0O
   for Ii1iIIIi1ii in range ( 1 ) :
    for o0oo0o0O00OO in range ( 2 ) :
     i11IiIiiIIIII = [ [ "achat" , o0oo0o0O00OO , 500.0 ] ]
     if 80 - 80: i1IIi
     for oOOO0o0o in i11IiIiiIIIII :
      iiI1 = { "tausendblum" : oOOO0o0o }
      O0O . send ( iiI1 )
      sleep ( I11iii )
   O0O . close ( )
   if 19 - 19: OoOO0ooOOoo0O + Oo
   if 53 - 53: OoooooooOO . i1IIi
  if O00 == 4 :
   O0o0Oo = "127.0.0.1"
   Oo00OOOOO = 8000
   O0O = IiII1IiiIiI1 ( O0o0Oo , Oo00OOOOO )
   if 18 - 18: Ooo00oOo00o
   iiI1 = '''{"Passe cet ordre 1:":{{"pass_client": "xxxxxxxxxxxxxxx",
            "order": {"m_orderType": "MKT", "m_goodTillDate": "", "m_action": "SELL", "m_tif": "DAY", "m_totalQuantity": 5, "m_goodAfterTime": "", "m_lmtPrice": 600},
            "contract": {"m_primExch": "SMART", "m_currency": "USD", "m_symbol": "GOOG", "m_exchange": "SMART", "m_secType": "STK"}}}
        {"Passe cet ordre 2:":{"pass_client": "xxxxxxxxxxxxxxx",
        "order": {"m_orderType": "MKT", "m_goodTillDate": "", "m_action": "BUY", "m_tif": "DAY", "m_totalQuantity": 5, "m_goodAfterTime": "", "m_lmtPrice": 33.2},
        "contract": {"m_primExch": "SMART", "m_currency": "USD", "m_symbol": "YHOO", "m_exchange": "SMART", "m_secType": "STK"}}}}'''
   for o0oo0o0O00OO in range ( 3 ) :
    sleep ( I11iii )
    O0O . send ( iiI1 )
   O0O . close ( )
   if 28 - 28: II11iiII - oooO0oo0oOOOO . oooO0oo0oOOOO + oOo0O0Ooo - OoooooooOO + O0
   if 95 - 95: ooOO00oOo % iiiiIi11i . O0
  if O00 == 0 :
   O0o0Oo = "127.0.0.1"
   Oo00OOOOO = 6666
   O0O = IiII1IiiIiI1 ( O0o0Oo , Oo00OOOOO )
   for o0oo0o0O00OO in range ( 10000 ) :
    for I1i1I in [ dod . benj ] :
     iiI1 = { "Ordre pour test" : I1i1I }
     O0O . send ( iiI1 )
     sleep ( I11iii )
    oOO00oOO = { "Retour info" : [ 0 , 0 ] }
    i11IiIiiIIIII = json . dumps ( oOO00oOO , ensure_ascii = False )
    O0O . send ( i11IiIiiIIIII )
   O0O . close ( )
   if 75 - 75: i1IIi / OoooooooOO - O0 / oOo0O0Ooo . II111iiii - i1IIi
   if 71 - 71: II11iiII + o0000oOoOoO0o * II11iiII - ooOO00oOo * Ooo00oOo00o
  if O00 == 1 :
   O0o0Oo = "127.0.0.1"
   Oo00OOOOO = 8000
   O0O = IiII1IiiIiI1 ( O0o0Oo , Oo00OOOOO )
   for o0oo0o0O00OO in range ( 20 ) :
    Oooo0Ooo000 = dod . yhoo_1
    iiI1 = { "Ordre pour test" : Oooo0Ooo000 }
    O0O . send ( iiI1 )
    print
    sleep ( I11iii )
   O0O . close ( )
   if 51 - 51: i11iIiiIii . oo + II111iiii
   if 10 - 10: oOoO0oo0OOOo * Oo * II111iiii % o0000oOoOoO0o . II11iiII + o0oo0o
  if O00 == 3 :
   O0o0Oo = "127.0.0.1"
   Oo00OOOOO = 8888
   O0O = IiII1IiiIiI1 ( O0o0Oo , Oo00OOOOO )
   if 19 - 19: oOo0O0Ooo - oo . II11iiII / oooO0oo0oOOOO
   for o0oo0o0O00OO in range ( 1 ) :
    for iiI1 in [ "toto" , 1 , 1.23 , { "question" : "réponds moi !" , "dict" : "test" } ] :
     O0O . send ( iiI1 )
     sleep ( 0.1 )
     O0O00Ooo = O0O . listen ( )
     print "Réception de" , O0O00Ooo
    sleep ( I11iii )
    if 33 - 33: o0oo0o / oOoO0oo0OOOo % oo + Oo / ooOO00oOo
    O0O . send ( "toto" )
    sleep ( 0.1 )
    O0O00Ooo = O0O . listen ( )
    print "Réception de" , O0O00Ooo
    if 52 - 52: Ooo00oOo00o - OoooooooOO + o0000oOoOoO0o + o0000oOoOoO0o - Ooo00oOo00o / o0oo0o
    O0O . send ( "éèàôê" )
    sleep ( I11iii )
    O0O00Ooo = O0O . listen ( )
    print "Réception de" , O0O00Ooo
    if 44 - 44: Oo . i1IIi - oOoO0oo0OOOo . O0 - Oo
    O0O . send ( 1.23 )
    sleep ( I11iii )
    O0O00Ooo = O0O . listen ( )
    print "Réception de" , O0O00Ooo
    if 92 - 92: i1I1ii1II1iII . OoOO0ooOOoo0O + Ooo00oOo00o
    O0O . send ( { "question" : "réponds moi !" } )
    sleep ( I11iii )
    O0O00Ooo = O0O . listen ( )
    print "Réception de" , O0O00Ooo
    if 28 - 28: i1IIi * OoO0O00 - Ooo00oOo00o * oooO0oo0oOOOO * o0000oOoOoO0o / ooOO00oOo
    O0O . send ( [ 1 , 1.23 , "titi" , "éè" , { "who" : "éèà" } ] )
    sleep ( I11iii )
    O0O00Ooo = O0O . listen ( )
    print "Réception de" , O0O00Ooo
    if 94 - 94: II111iiii % oOoO0oo0OOOo / oOo0O0Ooo * iIii1I11I1II1
   for o0oo0o0O00OO in range ( 1 ) :
    for iiI1 in [ "toto" , 1 , 1.23 , { "question" : "réponds moi !" , "dict" : "test" } ] :
     O0O . send_all ( iiI1 )
     sleep ( I11iii )
     O0O00Ooo = O0O . listen ( )
     print "Réception de" , O0O00Ooo
     if 54 - 54: Ooo00oOo00o - oo + OoooooooOO
    O0O . send_all ( "toto" )
    sleep ( I11iii )
    O0O00Ooo = O0O . listen ( )
    print "Réception de" , O0O00Ooo
    if 70 - 70: o0000oOoOoO0o / OoOO0ooOOoo0O . i1I1ii1II1iII % OoO0O00
    O0O . send_all ( "éèàôê" )
    sleep ( I11iii )
    O0O00Ooo = O0O . listen ( )
    print "Réception de" , O0O00Ooo
    if 67 - 67: oOo0O0Ooo * Ooo00oOo00o . oooO0oo0oOOOO - ooOO00oOo * Ooo00oOo00o
    O0O . send_all ( 1.23 )
    sleep ( I11iii )
    O0O00Ooo = O0O . listen ( )
    print "Réception de" , O0O00Ooo
    if 46 - 46: II11iiII + oOo0O0Ooo . oo * iiiiIi11i % oooO0oo0oOOOO
    O0O . send_all ( { "question" : "réponds moi !" } )
    sleep ( I11iii )
    O0O00Ooo = O0O . listen ( )
    print "Réception de" , O0O00Ooo
    if 86 - 86: oo + o0000oOoOoO0o % i11iIiiIii * iiiiIi11i . Oo * OoOO0ooOOoo0O
    O0O . send_all ( [ 1 , 1.23 , "titi" , "éè" , { "who" : "éèà" } ] )
    sleep ( I11iii )
    O0O00Ooo = O0O . listen ( )
    print "Réception de" , O0O00Ooo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
