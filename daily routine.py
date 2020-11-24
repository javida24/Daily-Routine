# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:29:19 2020

@author: javid
"""

print('Hi welocme today\n'
      'Javid\'s daily routine\n'
      'Please answer:\ntrue with 1\nnot with 0')

a = ['happy', 'smile', 'laugh', 'peak emotional state',
     'posture & deep breathing', 'teeth brush x3',
     'motiviation video', 'yoga', 'meditation',
     'Michael music', 'push up', 'pull up',
     'sleep 30min nap', 'sleep from 12 to 6',
     'healthy diet & weight', 'read book',
     'relaxing music', 'piano improvise', 
     'piano poirot', 'sing', 'guitar', 'sunburst',
     'read meta-analysis', 'no web trash', 'eat Apple']

c = 0
d = []
for n in range(25):
    print(a[n])
    b = int(input())
    c = c+b
    if b==0:
        d.append(a[n])

print('your success rate for today is:\n', 
      c/25*100, '\nThanks, here is your goals remained'
      ' for today:\n', d, '\nGood luck')