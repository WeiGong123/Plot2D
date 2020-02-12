import matplotlib.pyplot as plt
import xlrd
import numpy as np

# Read excel
book = xlrd.open_workbook('Plot.xlsx')
sheet1 = book.sheets()[0]
nrows = sheet1.nrows
ncols = sheet1.ncols
time = np.array(sheet1.col_values(0)[1:nrows])
RH_Probe_1 = np.array(sheet1.col_values(2)[1:nrows])
RH_Probe_2 = np.array(sheet1.col_values(6)[1:nrows])

# Plot
plt.plot(time, RH_Probe_1, label='RH Probe 1', marker = 'o')
plt.plot(time, RH_Probe_2, label='RH Probe 2', marker = 's')
plt.plot([0, 5000], [0.6, 0.6], label = 'Saturation RH', linestyle = '--')
plt.xlabel("Time/h")
plt.ylabel("Relative Humidity")
plt.legend(loc = 'lower right')
plt.show()

