#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Frank@Villaro-Dixon.eu - DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE, etc.

from daikin_altherma import DaikinAltherma
from opentsdb import TSDBClient, Gauge


ad = DaikinAltherma('192.168.10.126')
tsdb = TSDBClient('opentsdb.cra.k3s.fr', port=80)

TP = 'cra.hp.'

tsdb.tank_temperature = Gauge(TP+'tank_temperature')
tsdb.tank_temperature.set(ad.tank_temperature)

tsdb.outdoor_temperature = Gauge(TP+'outdoor_temperature')
tsdb.outdoor_temperature.set(ad.outdoor_temperature)

tsdb.leaving_water_temperature = Gauge(TP+'leaving_water_temperature')
tsdb.leaving_water_temperature.set(ad.leaving_water_temperature)

tsdb.power_state = Gauge(TP+'power_state')
tsdb.power_state.set(ad.power_state)


tsdb.close()
tsdb.wait()

# vim: set ts=4 sw=4 et:

