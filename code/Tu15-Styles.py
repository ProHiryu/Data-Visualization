from matplotlib import style

style.use('ggplot')

  #candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
    ax1.plot(date,closep)
    ax1.plot(date,openp)

style.use('fivethirtyeight')

print(plt.style.available)

style.use('dark_background')

print(plt.__file__)
