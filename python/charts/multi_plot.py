#!/usr/local/bin/python

"""
"""

from cStringIO import StringIO
import pandas as pd

import matplotlib.pyplot as plt

ibm = StringIO(
'''
Date            AdjClose        Volume
12/2/2013       177.48          4560000
12/3/2013       176.08          5864000
12/4/2013       175.74          5267400
12/5/2013       176.08          4384900
12/6/2013       177.67          4739800
12/9/2013       177.46          3796600
12/10/2013      177.12          4127800
12/11/2013      175.2           4055300
12/12/2013      173.37          5667900
12/13/2013      172.8           4184400
12/16/2013      177.85          7517000
12/17/2013      175.76          5471900
12/18/2013      178.7           5697700
12/19/2013      180.22          5927000
12/20/2013      180.02          7653500
12/23/2013      182.23          4079900
12/24/2013      183.22          1613600
12/26/2013      185.35          3325700
12/27/2013      185.08          3381600
12/30/2013      186.41          3018600
12/31/2013      187.57          3619700
''')

df = pd.read_table(ibm,
                   skiprows=0,
                   header=1,
                   delimiter='\s+',
                   parse_dates=[0])


#--------------------------------------------#
#----- Plot containing Price and Volume -----#
#--------------------------------------------#

# See http://matplotlib.org/examples/api/two_scales.html

# Clear current figure
plt.clf()

fig, adj_close_ax = plt.subplots()

# Make some room on the right and bottom for the extra axis and labels
fig.subplots_adjust(bottom=0.20, right=0.75)

# Rotate and align tick labels
# http://matplotlib.org/users/recipes.html#fixing-common-date-annoyances
fig.autofmt_xdate()

adj_close_ax.plot(df.Date, df.AdjClose, color='b')
adj_close_ax.set_ylabel('Adjusted Close', color='b')
for tl in adj_close_ax.get_yticklabels():
    tl.set_color('b')

volume_ax = adj_close_ax.twinx()
volume_ax.plot(df.Date, df.Volume, color='g')
volume_ax.set_ylabel('Volume', color='g')
for tl in volume_ax.get_yticklabels():
    tl.set_color('g')

plt.title('IBM Dec-2013')

plt.savefig('multi_plot_1.png', dpi=96)
