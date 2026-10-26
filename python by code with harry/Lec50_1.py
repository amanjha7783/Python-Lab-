f = open("myfile2.text","w")
lines = ['line1','line2', 'line3']
for line in lines:
  f.writelines(line + '\n')
f.close()