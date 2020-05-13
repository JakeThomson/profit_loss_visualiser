import webbrowser
import pandas as pd
import random
import plotly
import plotly.graph_objects as go

df = pd.read_csv("balance.csv")


balance = 10000
total_profit_loss = 0
bot_accuracy = 0.7
profit_stop = 0.02
trade_percentage = 0.25
loss_stop = 0.01

for i in range(len(df)):
    outcome = random.random()
    if outcome < bot_accuracy:
        # Winning trade
        profitloss = balance * trade_percentage * profit_stop
        balance += profitloss
    else:
        # Losing trade
        profitloss = balance * trade_percentage * loss_stop
        balance -= profitloss
        profitloss = -profitloss

    df["Balance"].iloc[i] = balance
    df["ProfitLoss"].iloc[i] = profitloss

fig = go.Figure(
    data=[go.Scatter(x=df["Date"], y=df["Balance"])],
    layout=go.Layout(
        title=go.layout.Title(text="Balance over time")
    )
)

plotly.offline.plot(fig, filename='plot.html', auto_open=False)
webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s') \
    .open('file:///D:/Uni/Year%203/Dissertation/Application/balance/plot.html')

