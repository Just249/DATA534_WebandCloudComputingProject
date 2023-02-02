#15 Drugs that the Phamacy order and they what to know
from api_wrapper.Vim_jdrugconsumption import jdrugconsumption as jdrugconsumption
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import numpy as np

order = pd.DataFrame(jdrugconsumption("LIP BALM SPF 15", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("TOLBUTAMIDE", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("PLACIDYL CAP 200MG", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("PLACIDYL CAP 500MG", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("NEMBUTAL SODIUM CAP 100MG", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("ERYTHROCIN IV", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("NEMBUTAL SODIUM INJ 50MG/ML", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("EES-200", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("ERYTHROCIN LIQUID 125", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("COLCHICINE TAB 0.6MG", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("ERYTHROCIN FILMTAB 250MG", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("DURETIC 5MG", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("ISOPTO CARBACHOL 1.5%", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("ISOPTO CARBACHOL 3%", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("ALCON TEARS 0.5%", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("XYLOCAINE 1% W EPINEPHRINE 1:100000", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("XYLOCARD", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("XYLOCAINE OINTMENT 5%", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("PENBRITIN CAP 250MG", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("PENBRITIN CAP 500MG", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("ATROMID S CAP 500MG", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order = order.append(jdrugconsumption("ORBENIN CAP 250MG", '9ec4bb641b31ddeeb9bfd84908c8dbb1'))
order

form = order['Form'].unique()
admin = order['Administration Route'].to_numpy()
 
alt.Chart(order).mark_bar().encode(
    x= alt.Y('Administration Route', sort='-y'),
    y='count()',
    color='Administration Route',
    tooltip=['Administration Route']
).properties(
            width=300,
            height=200,
            title = "Order Statistic")

