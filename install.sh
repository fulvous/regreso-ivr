#!/bin/bash

if [ "$( egrep -c 'regreso-ivr' /etc/asterisk/extensions_custom.conf)" != "2" ] ; then
  cat ./extensions_custom.conf >> /etc/asterisk/extensions_custom.conf
fi

if [ "$( egrep -c 'regreso-ivr' /etc/asterisk/extensions_override_freepbx.conf)" != "1" ] ; then
  cat ./extensions_override_freepbx.conf >> /etc/asterisk/extensions_override_freepbx.conf
fi

cp -fv ./regreso-ivr.py /var/lib/asterisk/agi-bin/regreso-ivr.py
cp -fv ./regreso-ivr.wav /var/lib/asterisk/sounds/en/custom/regreso-ivr.wav
