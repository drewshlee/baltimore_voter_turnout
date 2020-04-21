import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import pandas as pd

df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/minoritymajority.csv')
df_sample_r = df_sample[df_sample['STNAME'] == 'Maryland']
df_sample_r.sort_values(by=['CTYNAME'])
df = pd.read_csv('MarylandTurnout.csv')
df_corona = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-20-2020.csv',index_col=0)
df_corona = df_corona[df_corona['Province_State'] == 'Maryland']
df_corona.sort_values(by=['Admin2'])
df_corona = df_corona.drop(df_corona.loc[df_corona.index==90024.0].index)

#fig = px.line(df_sample_r, x = 'FIPS', y = 'TOT_POP', title='Population Size Across Baltimore Counties')
#fig.show()

voterTurnout = df['Voter Turnout PCT'].tolist()
coronaCases = df_corona['Confirmed'].tolist()
pctInfected = [100*i / j for i, j in zip(df_corona['Confirmed'].tolist(), df['County Population'].tolist())]
infectMin, infectMax = min(pctInfected), max(pctInfected)
normInfect = pctInfected
for i, val in enumerate(normInfect):
      normInfect[i] = (val) / (infectMax)
normalized65Pop = df['Normalized65'].tolist()
riskNum = [i*j for i, j in zip(normInfect, normalized65Pop)]
riskMax = max(riskNum)
for i, val in enumerate(riskNum):
      riskNum[i] = (val) / (riskMax)
riskNum = [round(100*i) for i in riskNum]
fips = df_sample_r['FIPS'].tolist()
values = riskNum

num = 10j
num2 = int(np.imag(num)+1)
r = 165
g = 235
b = 255
steps = np.linspace(10, 200, num2)

color = ["rgb("+str(abs(r-steps[i]))+","+str(abs(g-steps[i]))+","+
         str(abs(b-steps[i]))+")"for i in range(num2)]

endpts = list(np.mgrid[min(values):max(values):num])
colorscale = color
colorscale2 = ["#ebf3fb", "#c6dbef", "#85bcdb", "#4292c6", "#1361a9", "#08306b"]

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['Maryland'], show_state_data=False,
    colorscale=colorscale, binning_endpoints=endpts, round_legend_values=True,
    show_hover=True, centroid_marker={'opacity': 0},
    plot_bgcolor='rgb(229,229,229)',
    paper_bgcolor='rgb(229,229,229)',
    title_text='Risk Number for Each County',
    legend_title='Normalized % over 65 x Normalized Infected',
    county_outline={'color': 'rgb(255,255,255)', 'width': 1},
    exponent_format=True,
)
fig.layout.template = None
fig.show()