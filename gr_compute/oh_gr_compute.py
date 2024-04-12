import matplotlib.pyplot as plt 
  
time = [] 
val = [] 
step_size = 10

# Plotting data
for i in range(101):

  k = i * step_size
  print('Plotting data for T = {}K'.format(k))

  for line in open('../histos/{}k_OH_histo'.format(k), 'r'):
    values = [float(s) for s in line.split()]
    time.append(values[0])
    val.append(values[1])

  plt.plot(time, val, color = 'g', label = 'gr_data') 

  plt.title('g(r) Data for OH at {}K'.format(k), fontsize = 20) 
  plt.legend() 
  plt.savefig('../img/{}k_OH_gr.png'.format(k))

  # Close the plot and empty the data arrays
  plt.close()
  time = [] 
  val = []
