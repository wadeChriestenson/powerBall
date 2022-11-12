import pandas as pd
import numpy as np
from scipy import stats
import plotly
import plotly.express as px
from dash import Dash, html, dcc

app = Dash(__name__)

input_csv = pd.read_csv('../csv/Powerball_History.csv')

powerBall_DF = pd.DataFrame(input_csv)

Date, \
Num_1, \
Num_2, \
Num_3, \
Num_4, \
Num_5, \
Powerball = powerBall_DF['Date'], \
            powerBall_DF['Num_1'], \
            powerBall_DF['Num_2'], \
            powerBall_DF['Num_3'], \
            powerBall_DF['Num_4'], \
            powerBall_DF['Num_5'], \
            powerBall_DF['Powerball']

Median_Num_1, \
Median_Num_2, \
Median_Num_3, \
Median_Num_4, \
Median_Num_5, \
Median_Powerball = np.median(powerBall_DF['Num_1']), \
                   np.median(powerBall_DF['Num_2']), \
                   np.median(powerBall_DF['Num_3']), \
                   np.median(powerBall_DF['Num_4']), \
                   np.median(powerBall_DF['Num_5']), \
                   np.median(powerBall_DF['Powerball'])

print(f'{Median_Num_1:.0f}',
      f'{Median_Num_2:.0f}',
      f'{Median_Num_3:.0f}',
      f'{Median_Num_4:.0f}',
      f'{Median_Num_5:.0f}',
      f'{Median_Powerball:.0f}')

fig_median = px.scatter(x=[1, 2, 3, 4, 5, 6],
                        y=[Median_Num_1,
                           Median_Num_2,
                           Median_Num_3,
                           Median_Num_4,
                           Median_Num_5,
                           Median_Powerball
                           ]
                        )

fig1 = px.scatter(x=Num_1, y=Date)
fig2 = px.scatter(x=Num_2, y=Date)
fig3 = px.scatter(x=Num_3, y=Date)
fig4 = px.scatter(x=Num_4, y=Date)
fig5 = px.scatter(x=Num_5, y=Date)
figPowerball = px.scatter(x=Powerball, y=Date)

app.layout = html.Div(children=[
    html.H1(children='History of Powerball Picks'),
    html.H2(children='''All ''' + str(len(Date)) + ''' Picks for the Powerball from 02/03/2010 to 11/09/2022'''),
    html.H3(children='''The Median Numbers of All Picks: ''' +
                     f'{Median_Num_1:.0f}' + ''' '''   
                     f'{Median_Num_2:.0f}' + ''' '''
                     f'{Median_Num_3:.0f}' + ''' '''
                     f'{Median_Num_4:.0f}' + ''' '''
                     f'{Median_Num_5:.0f}' + ''' '''
                     f'{Median_Powerball:.0f}'''),
    dcc.Graph(
        id='median',
        figure=fig_median
    ),
    dcc.Graph(
        id='Num_1',
        figure=fig1
    ),
    dcc.Graph(
        id='Num_2',
        figure=fig2
    ),
    dcc.Graph(
        id='Num_3',
        figure=fig3
    ),
    dcc.Graph(
        id='Num_4',
        figure=fig4
    ),
    dcc.Graph(
        id='Num_5',
        figure=fig5
    ),
    dcc.Graph(
        id='Powerball',
        figure=figPowerball
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
