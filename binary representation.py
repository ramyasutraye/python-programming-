def int_to_bin_string(i):
if(i==0):
return 0
whilei:
if(i&1==1):
s="1"+s
 else:
s="0"+s
return s
