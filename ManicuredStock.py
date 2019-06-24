class ManicuredStock:

  def __init__(self, stock):

    def returnWins(category):
      myList = []
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


    def change(category):
      myList = []
      for i in range(0, len(category) - 1):
        curr = category[i]
        prev = category[i+1]
        myList.append(curr - prev)
      return myList




    self.mw_opens = returnWins(stock.opens)
    self.mw_highs = returnWins(stock.highs)
    self.mw_lows = returnWins(stock.lows)
    self.mw_closes = returnWins(stock.closes)
    self.mw_adj_close = returnWins(stock.adj_close)
    self.mw_volumes = returnWins(stock.volumes)
    ###############################################
    self.w_opens = stock.opens[:-1]
    self.w_highs = stock.highs[:-1]
    #self.w_lows = returnWins(stock.lows)
    self.w_closes = stock.closes[:-1]
    #self.w_adj_close = returnWins(stock.adj_close)
    self.w_volumes = stock.volumes[:-1]

    self.c_highs = change(stock.highs)

  def boxify(self):
    box = []
    box.append(self.mw_opens)
    #box.append(self.mw_highs)
    box.append(self.mw_lows)
    box.append(self.mw_closes)
    box.append(self.mw_adj_close)
    box.append(self.mw_volumes)
    box.append(self.w_opens)
    box.append(self.w_highs)
    box.append(self.w_closes)
    box.append(self.w_volumes)
    box.append(self.c_highs)

    #print(box)
    #print("data length: {}".format(len(self.mw_opens)))
    return box
