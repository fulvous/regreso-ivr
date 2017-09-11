#!/usr/bin/python
import sys
from asterisk.agi import *
import re

operator_ext = '1102@Bosch'
operator_tech = 'PJSIP'
callerid_override = 'Devol. puesto'
calling_retries = '3'


agi = AGI()
agi.verbose("=========================")
agi.verbose("IVR de regreso de llamada")
agi.verbose("    Leon Ramos - 2017")
agi.verbose("leon.ramos@meganucleo.mx")
agi.verbose("=========================")

cnum = agi.get_variable('CALLERID(num)')
cname = agi.get_variable('CALLERID(name)')
channel = agi.get_variable('CHANNEL')
m = re.search('(?<=/)\w+',channel)
chandest = m.group(0)
m = re.search('\w+/\w+',channel)
chancalled = m.group(0)
dnid = agi.get_variable('DNID')
uniqueid = agi.get_variable('UNIQUEID')
dnum = agi.get_variable('EXTTOCALL')
did = agi.get_variable('CDR(did)')
m = re.search('^\w+',channel)
tech = m.group(0)
retries = agi.get_variable('REGRESO_RETRIES')

if len(retries) > 0 :
  retries = str(int(retries) + 1)
else :
  retries = '1'

agi.set_variable('REGRESO_RETRIES',retries)

agi.verbose("")
agi.verbose("=========================")
agi.verbose("Variables de llamada")
agi.verbose("cnum: " + cnum)
agi.verbose("cname: " + cname)
agi.verbose("channel: " + channel)
agi.verbose("chandest: " + chandest)
agi.verbose("dnid: " + dnid)
agi.verbose("uniqueid: " + uniqueid)
agi.verbose("chancalled: " + chancalled)
agi.verbose("did: " + did)
agi.verbose("tech: " + tech)
agi.verbose("dnum: " + dnum)
agi.verbose("retries: " + retries)
agi.verbose("=========================")
agi.verbose("")

while True:
  agi.exec_command('Read','digit','custom/regreso-ims','1','','1','3')
  result = agi.get_variable('digit')
  if result.isdigit():
    agi.verbose("Digito: %s" % result)
    if result == '1' :
      agi.set_variable('CALLERID(name)',callerid_override)
      agi.set_variable('CALLERID(num)',cnum)
      agi.exec_command('dial',tech + '/' + operator_ext )
      #agi.exec_command('goto','from-internal-xfer', operator_ext, 1)
      sys.exit()
  else:
    if retries == str( int(calling_retries) + 1 ) :
      agi.hangup()
    else :
      agi.verbose("Remarcando destino!!!")
      agi.exec_command('goto','ext-local', dnum, 1)
    sys.exit()
