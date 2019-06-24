class Stock():

  year = 2016

  #Here we have a class object that is specifically made to contain data for a single stock
  #(For readability purposes)

  def __init__(self, ticker):
    self.ticker = ticker
    from yahoo_historical import Fetcher
    chart = Fetcher(ticker, [self.year, 1, 1], [2019, 6, 18])
    self.data = chart.getHistorical()
    self.opens = self.data['Open']
    self.highs = self.data['High']
    self.lows = self.data['Low']
    self.closes = self.data['Close']
    self.adj_close = self.data['Adj Close']
    self.volumes = self.data['Volume']
    
    self.positions = {}
    for i in range(len(self.data)):
      self.positions[i] = i


    def returnWins(category):
      myList = []
      #Fixed
      for i in range(0, len(category) - 1):
        
        curr = category[i]
        prev = category[i+1]

        if curr > prev:
          myList.append(1)
        elif curr == prev:
          myList.append(0)
        else:
          myList.append(-1)

      return myList
    
    self.y_answer = returnWins(self.highs)
  
  def info(self):
    print("Stock {} has several features. Opens, Highs, Lows, Closes, Adj_close, and Volumes.".format(self.ticker))