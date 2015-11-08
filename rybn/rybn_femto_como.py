#!/usr/bin/env python
# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import json
from time import sleep
from rybn_femto_cliento import IiII1IiiIiI1
from rybn_configo import I1IiI
try :
 import req_admxi
except :
 req_admxi = None
 if 73 - 73: II111iiii
 if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
 if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
class IiiIII111iI ( object ) :
 if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . OoO0O00 - I1ii11iIi11i
 if 53 - 53: I11i / Oo0Ooo / II111iiii % Ii1I / OoOoOO00 . Oo0ooO0oo0oO
 def __init__ ( self , rybn_femto_ini ) :
  if 100 - 100: i1IIi
  if 27 - 27: O00oOoOoO0o0O * OoooooooOO + I11i * Oo0ooO0oo0oO - i11iIiiIii - iii1I1I
  if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - oO0o
  self . cf = I1IiI ( rybn_femto_ini )
  self . conf = self . cf . conf
  if 72 - 72: II111iiii - OoOoOO00
  self . pass_client = self . conf [ "rybn" ] [ "pwd" ]
  if 91 - 91: OoO0O00 . i11iIiiIii / oO0o % I11i / OoO0O00 - i11iIiiIii
  self . miskin_clt = None
  self . rybn_clt = None
  if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . O00oOoOoO0o0O / O00oOoOoO0o0O % O00oOoOoO0o0O
 def create_miskin_clt ( self ) :
  if 22 - 22: Ii1I . O00oOoOoO0o0O
  if 41 - 41: O0oo0OO0 . Oo0ooO0oo0oO * O00oOoOoO0o0O % i11iIiiIii
  if 74 - 74: iii1I1I * O00oOoOoO0o0O
  if not self . miskin_clt :
   if 82 - 82: iIii1I11I1II1 % O00oOoOoO0o0O
   oOo0oooo00o = self . conf [ "miskin" ] [ "host" ]
   oO0o0o0ooO0oO = self . conf [ "miskin" ] [ "port" ]
   self . miskin_clt = Client ( oOo0oooo00o , oO0o0o0ooO0oO )
   if 52 - 52: II111iiii - i11iIiiIii % O0oo0OO0
 def create_rybn_clt ( self ) :
  if 54 - 54: OOooOOo % O0 + I1IiiI - iii1I1I / I11i
  if 31 - 31: OoO0O00 + II111iiii
  if 13 - 13: OOooOOo * oO0o * I1IiiI
  if not self . rybn_clt :
   if 55 - 55: II111iiii
   IIIiI11ii = self . conf [ "rybn" ] [ "host" ]
   O000oo = self . conf [ "rybn" ] [ "port" ]
   self . rybn_clt = Client ( IIIiI11ii , O000oo )
   if 3 - 3: iii1I1I + O0
 def send_to_rybn ( self , order_dict ) :
  if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
  if 78 - 78: OoO0O00
  if 18 - 18: O0 - iii1I1I / iii1I1I + Oo0ooO0oo0oO % Oo0ooO0oo0oO - O00oOoOoO0o0O
  if not self . rybn_clt :
   self . create_rybn_clt ( )
   if 62 - 62: iii1I1I - O00oOoOoO0o0O - OoOoOO00 % i1IIi / oO0o
  self . rybn_clt . send ( order_dict )
  if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
  self . send_to_miskin ( order_dict )
  self . rybn_clt . close ( )
  self . rybn_clt = None
  if 14 - 14: I11i % O0
 def send_to_miskin ( self , order_dict ) :
  if 41 - 41: i1IIi + O0oo0OO0 + OOooOOo - O00oOoOoO0o0O
  if 77 - 77: Oo0Ooo . O00oOoOoO0o0O % Oo0ooO0oo0oO
  if not self . miskin_clt :
   self . create_miskin_clt ( )
   if 42 - 42: oO0o - i1IIi / i11iIiiIii + OOooOOo + OoO0O00
   if 17 - 17: oO0o . Oo0Ooo . I1ii11iIi11i
   if 3 - 3: OoOoOO00 . Oo0Ooo . I1IiiI / Ii1I
  if "pass_client" in order_dict :
   del order_dict [ "pass_client" ]
   if 38 - 38: II111iiii % i11iIiiIii . Oo0ooO0oo0oO - OOooOOo + Ii1I
  self . miskin_clt . send ( order_dict )
  if 66 - 66: OoooooooOO * OoooooooOO . OOooOOo . i1IIi - OOooOOo
  if 77 - 77: I11i - iIii1I11I1II1
  Ooo , O0o0Oo , Oo00OOOOO , O0O , O00o0OO = 0 , 0 , 0 , 0 , 0
  if req_admxi :
   Ooo = req_admxi . get_cash ( 'femto' )
   O0o0Oo = req_admxi . get_portfolio ( 'femto' )
   Oo00OOOOO = req_admxi . get_orders ( 'femto' )
   O0O = req_admxi . get_historicals ( 'femto' )
   O00o0OO = req_admxi . get_open_market ( )
   if 44 - 44: O00oOoOoO0o0O / O0 % i1IIi * oO0o + Oo0Ooo
  Ii1IOo0o0 = { "Admxi Info" : { "cash" : Ooo ,
 "portfolio" : O0o0Oo ,
 "orders" : Oo00OOOOO ,
 "histo" : O0O ,
 "market" : O00o0OO } }
  if 49 - 49: oO0o % Ii1I + i1IIi . I1IiiI % I1ii11iIi11i
  I1i1iii = json . dumps ( Ii1IOo0o0 , ensure_ascii = False )
  self . miskin_clt . send ( I1i1iii )
  self . miskin_clt . close ( )
  self . miskin_clt = None
  if 20 - 20: o0oOOo0O0Ooo
  if 77 - 77: OoOoOO00 / I11i
  if 98 - 98: iIii1I11I1II1 / i1IIi / i11iIiiIii / o0oOOo0O0Ooo
def I1i1I1II ( symbol , sec_type , exch , prim_exch , curr ) :
 i1 = Contract ( )
 if 48 - 48: O0 + O0 - I1ii11iIi11i . Oo0ooO0oo0oO / iIii1I11I1II1
 if 77 - 77: i1IIi % OoOoOO00 - O00oOoOoO0o0O + Oo0ooO0oo0oO
 if 31 - 31: I11i - i1IIi * OOooOOo / OoooooooOO
 if 18 - 18: i11iIiiIii
 if 46 - 46: i1IIi / I11i % OOooOOo + O0oo0OO0
 if 79 - 79: O0oo0OO0 - o0oOOo0O0Ooo + O0oo0OO0 - iii1I1I
 if 8 - 8: I1IiiI
 if 75 - 75: iIii1I11I1II1 / OOooOOo % o0oOOo0O0Ooo * OoOoOO00
 if 9 - 9: OoO0O00
 if 33 - 33: Oo0ooO0oo0oO . iii1I1I
 if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % O0oo0OO0 - I1ii11iIi11i / oO0o
 i1 . m_symbol = symbol
 i1 . m_secType = sec_type
 i1 . m_exchange = exch
 i1 . m_primaryExch = prim_exch
 i1 . m_currency = curr
 return i1
 if 50 - 50: I1IiiI
def Ii1i11IIii1I ( order_type , quantity , action ) :
 OOOoO0O0o = Order ( )
 if 55 - 55: OOooOOo + Oo0ooO0oo0oO . i1IIi - I1ii11iIi11i . O0 - Oo0ooO0oo0oO
 if 92 - 92: iii1I1I . I11i + o0oOOo0O0Ooo
 if 28 - 28: i1IIi * Oo0Ooo - o0oOOo0O0Ooo * O00oOoOoO0o0O * Ii1I / OoO0O00
 if 94 - 94: II111iiii % I1ii11iIi11i / OoOoOO00 * iIii1I11I1II1
 if 54 - 54: o0oOOo0O0Ooo - I1IiiI + OoooooooOO
 if 70 - 70: Ii1I / I11i . iii1I1I % Oo0Ooo
 if 67 - 67: OoOoOO00 * o0oOOo0O0Ooo . O00oOoOoO0o0O - OoO0O00 * o0oOOo0O0Ooo
 if 46 - 46: OOooOOo + OoOoOO00 . I1IiiI * oO0o % O00oOoOoO0o0O
 if 86 - 86: I1IiiI + Ii1I % i11iIiiIii * oO0o . Oo0ooO0oo0oO * I11i
 if 44 - 44: oO0o
 OOOoO0O0o . m_orderType = order_type
 OOOoO0O0o . m_totalQuantity = quantity
 OOOoO0O0o . m_action = action
 return OOOoO0O0o
 if 88 - 88: O0oo0OO0 % Ii1I . II111iiii
 if 38 - 38: o0oOOo0O0Ooo
 if 57 - 57: O0 / oO0o * O0oo0OO0 / OoOoOO00 . II111iiii
if __name__ == "__main__" :
 if 26 - 26: iii1I1I
 OOO = IiiIII111iI ( "rybn_femto.ini" )
 if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
 Oo0OoO00oOO0o = { "pass_client" : "xxxxxxxxxxxxxxx" ,
 "contract" : { "m_symbol" : "GOOG" ,
 "m_secType" : "STK" ,
 "m_primExch" : "SMART" ,
 "m_exchange" : "SMART" ,
 "m_currency" : "USD" } ,
 "order" : { "m_action" : "BUY" ,
 "m_totalQuantity" : 5 ,
 "m_orderType" : "MKT" ,
 "m_lmtPrice" : 600 ,
 "m_tif" : "DAY" ,
 "m_goodAfterTime" : "" ,
 "m_goodTillDate" : "" } }
 if 80 - 80: oO0o + OOooOOo - OOooOOo % iii1I1I
 OoOO0oo0o = { "pass_client" : "xxxxxxxxxxxxxxx" ,
 "contract" : { "m_symbol" : "GOOG" ,
 "m_secType" : "STK" ,
 "m_primExch" : "SMART" ,
 "m_exchange" : "SMART" ,
 "m_currency" : "USD" } ,
 "order" : { "m_action" : "SELL" ,
 "m_totalQuantity" : 5 ,
 "m_orderType" : "MKT" ,
 "m_lmtPrice" : 600 ,
 "m_tif" : "DAY" ,
 "m_goodAfterTime" : "" ,
 "m_goodTillDate" : "" } }
 if 14 - 14: o0oOOo0O0Ooo * iii1I1I * iii1I1I / OoOoOO00
 for Oo0o00 in [ Oo0OoO00oOO0o , OoOO0oo0o ] :
  OOO . send_to_rybn ( Oo0o00 )
  OOO . send_to_miskin ( Oo0o00 )
  sleep ( 5 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
