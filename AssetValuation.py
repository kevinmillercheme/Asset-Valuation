asset = 'NVDA'
price = 186 # current price
dividend = 0.0002 # current div ratio
marketCap = 4.58e9 # current market cap
PEratio = 45.28 # current PE ratio
PBratio = 38 # current PB
EGR = 0.6426 # 5-Year EGR for stability

# PEG Ratio = PEratio / Earnings Growth Rate (EGR)

# Linear regression is used for socioeconomic impact
def marketCapEval(marketCap):
    if marketCap > 1e6:
        mcfactor = 1
        print('solid', mcfactor)
    elif marketCap < 1e6 and marketCap > 1e3:
        mcfactor = 0.8
        print('decent', mcfactor)
    elif marketCap > 1e2:
        mcfactor = 0.6
        print('no', mcfactor)
    else:
        mcfactor = 0.25
        print('bad', mcfactor)

