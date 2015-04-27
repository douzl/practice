#!/usr/bin/env python

import re
import string
from sys import argv
from os.path import exists
import bz2
import contextlib

pattern = 'appkey'
pattern_appkey = 'appkey:<<[\S]*>>'
pattern_actions = 'action:<<[\S]*>>'

script, logs = argv

apps_count = {
    'all': {
        'appname': 'all',
        'times-actions': 0,
        'session-initiate': 0,
        'session-accept': 0,
        'call-accept': 0,
        'session-terminate': 0,
        'caller-relay': 0,
        'call-rate': 0,
    }
}

def count_actions(appname, action):
    if appname in apps_count:
       apps_count[appname][action] = apps_count.get(appname).get(action) + 1
       apps_count[appname]['times-actions'] = apps_count.get(appname).get('times-actions') + 1
    else:
       apps_count[appname] = {
           'appname': appname,
           'times-actions': 0,
           'session-initiate': 0,
           'session-accept': 0,
           'call-accept': 0,
           'session-terminate': 0,
           'caller-relay': 0,
           'call-rate': 0,
       }
       apps_count[appname][action] = apps_count.get(appname).get(action) + 1
       apps_count[appname]['times-actions'] = apps_count.get(appname).get('times-actions') + 1
       

def calucate_call_rate(session_accept, caller_relay):
    if caller_relay == 0:
        return 0
    else:
        return float(session_accept) / float(caller_relay)
        
def count_call_rate():
    for app in apps_count:
        session_accept = apps_count[app]['session-accept']
        caller_relay = apps_count[app]['caller-relay']
        call_rate = calucate_call_rate(session_accept, caller_relay)
        apps_count[app]['call-rate'] = call_rate
        
def report_app(appname, reportfile):
    times_actions = apps_count[appname]['times-actions']
    session_initiate = apps_count[appname]['session-initiate']
    session_accept = apps_count[appname]['session-accept']
    call_accept = apps_count[appname]['call-accept']
    session_terminate = apps_count[appname]['session-terminate']
    caller_relay = apps_count[appname]['caller-relay']
    call_rate = apps_count[appname]['call-rate']
    
    reportfile = open(reportfile, "a")
    reportfile.write("APP Name: %s\n" % (appname))
    reportfile.write("Actions: %d\n" % (times_actions))
    reportfile.write("session-initiate: %d\n" % (session_initiate))
    reportfile.write("session-accept: %d\n" % (session_accept))
    reportfile.write("call-accept: %d\n" % (call_accept))
    reportfile.write("session-terminate: %d\n" % (session_terminate))
    reportfile.write("caller-relay: %d\n" % (caller_relay))
    reportfile.write("call-rate: %f\n" % (call_rate))
    reportfile.write("---------------------\n")
    reportfile.close()    
    
with contextlib.closing(bz2.BZ2File(logs, 'rb')) as logfile:
    for logmessage in logfile:
        appkey = re.findall(pattern_appkey, logmessage)
        actions = re.findall(pattern_actions, logmessage)
        if len(appkey) != 0:
            appname=appkey[0].split('"')
            actions = re.findall(pattern_actions, logmessage)
            action=actions[0].split('"')
#    print '%s, %s' % (appkey, appname[1])
#    print '%s, %s' % (actions, action[1])    
            count_actions('all', action[1])
            count_actions(appname[1], action[1])

count_call_rate()

report = "report.txt"
reportfile = open(report, "w")
reportfile.write("Log: %s\n" % (logs))
reportfile.close()    

report_app('all', report)
for app in apps_count:
    if app != 'all':
        report_app(app, report)
