"""
money-and-computer
 
規劃需要的電子設備和預計的使用年限，來計算每個月需要的支出。
"""

TABLE = [
#   類別          價格（千）    時間（年）    當前設備 
    "Name     ", "Price(k) ", "Time(y) ", "Current ",
    "Laptop   ", "22       ", "4+      ", "MacBook Pro ",
    "Phone    ", "14       ", "2+      ", "MI MIX 2S ",
    "Console  ", "16       ", "4+      ", "PlayStation4 / Switch $",
    "Monitor  ", "10       ", "4+      ", "Dell U2515h $",
    "PC       ", "35       ", "4+      ", "I5 16G 256SSD GTX750Ti ",
    "Tablet   ", "13       ", "2+      ", "iPad Mini 5"
    ]

if __name__ == "__main__":
  print("Money and Computer")

  # # too stupid some how
  # for i in range(1, len(TABLE) // 4):
  #   pass

  result = [int(i[0]) / (int(i[1][::-1]) * 12)
            for i in zip(TABLE[1 + 4::4], TABLE[2 + 4::4])]

  def print_line(x, y): return print(
      ("{}| " * 5)[:-2].format(*(x[0:3] + [y] + x[3:4])))

  print_line(TABLE[0:5], "Pay  ")
  for x in range(len(result)):
    print_line(TABLE[0+4*(x+1):5+4*(x+1)], str(result[x])[:4] + " ")

  print("each month pay total: <{:0.2}> (k)".format(sum(result)))
