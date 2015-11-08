#! /usr/bin/env python
# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import os
import ast
from ConfigParser import SafeConfigParser
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
class I1IiI ( ) :
 if 73 - 73: OOooOOo / ii11ii1ii
 if 94 - 94: OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo
 if 97 - 97: oO0o0ooO0 - IIII / o0oOOo0O0Ooo - oO0o0ooO0
 if 21 - 21: Oo0Ooo / II111iiii % OoOO0ooOOoo0O / OoOoOO00 . IIII
 def __init__ ( self , ini_file ) :
  self . conf = { }
  if 100 - 100: i1IIi
  self . femto_dir = os . getcwd ( )
  self . ini = self . femto_dir + "/" + ini_file
  self . load_config ( )
  if 27 - 27: o00O0oo * OoooooooOO + OoOO * IIII - i11iIiiIii - o0000oOoOoO0o
 def load_config ( self ) :
  if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - OOooOOo
  if 72 - 72: II111iiii - OoOoOO00
  OOo = SafeConfigParser ( )
  OOo . read ( self . ini )
  if 1 - 1: II111iiii - I1ii11iIi11i % i11iIiiIii + o00O0oo . oO0o0ooO0
  if 55 - 55: iIii1I11I1II1 - I1IiiI . OoOO0ooOOoo0O * o00O0oo * i1IIi / iIii1I11I1II1
  for OOo000 in OOo . sections ( ) :
   self . conf [ OOo000 ] = { }
   for O0I11i1i11i1I , Iiii in OOo . items ( OOo000 ) :
    self . conf [ OOo000 ] [ O0I11i1i11i1I ] = ast . literal_eval ( Iiii )
    if 87 - 87: OOooOOo / IIII + oO0o0ooO0 - IIII . IIII / II111iiii
  print ( "\nConfiguration chargée depuis {}" . format ( self . ini ) )
  if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
 def save_config ( self , section , key , value ) :
  if isinstance ( value , int ) :
   if 58 - 58: i11iIiiIii % oO0o0ooO0
   O0OoOoo00o = str ( value )
  if isinstance ( value , float ) :
   O0OoOoo00o = str ( value )
  if isinstance ( value , str ) :
   O0OoOoo00o = '"' + value + '"'
   if 31 - 31: II111iiii + OoO0O00 . oO0o0ooO0
  OoOooOOOO = SafeConfigParser ( )
  OoOooOOOO . read ( self . ini )
  OoOooOOOO . set ( section , key , O0OoOoo00o )
  with open ( self . ini , 'w' ) as i11iiII :
   OoOooOOOO . write ( i11iiII )
  i11iiII . close ( )
  print ( "{1} = {2} saved in {3} in section {0}\n" . format ( section , key , O0OoOoo00o , self . ini ) )
  if 34 - 34: ii11ii1ii % OoooooooOO / i1IIi . o0000oOoOoO0o + O0
  if 42 - 42: ii11ii1ii / i1IIi + i11iIiiIii - OoOO0ooOOoo0O
if __name__ == '__main__' :
 if 78 - 78: OoO0O00
 Iii1I111 = I1IiI ( "rybn_femto.ini" )
 if 60 - 60: OOooOOo * o0oOOo0O0Ooo % o0oOOo0O0Ooo % OoOO * II111iiii + i1IIi
 if 64 - 64: OOooOOo - O0 / II111iiii / o0oOOo0O0Ooo / iIii1I11I1II1
 print ( Iii1I111 . conf )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
