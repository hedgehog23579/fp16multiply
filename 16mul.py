def mul16(a,b):
 sign = 0x8000
 exp = 0x7c00

 frac = 0x3ff

 a = int(a,2)
 b = int(b,2)
 
 sign_a = (a&sign) >> 15
 sign_b = (b&sign) >> 15

 if((a&exp) == 0):
  exp_a = (a&exp) >> 10 + 1
  frac_a = a&frac + 1024#?
 else:
  exp_a = (a&exp) >> 10
  frac_a = (a&frac) + 1024 #?
 if((b&exp) == 0):
  exp_b = (b&exp)>>10 + 1
  frac_b = b&frac
 else:   
  exp_b = (b&exp) >> 10
  frac_b = (b&frac) + 1024

 #print('frac_a=',bin(frac_a)[2:])
 #print('frac_b=',bin(frac_b)[2:])
 #print('exp_a=',bin(exp_a)[2:])
 #print('exp_b=',bin(exp_b)[2:])

 sign_o = sign_a ^ sign_b
 exp_o = exp_a + exp_b
 product = frac_a * frac_b
 #print('product=',bin(product)[2:])
 #print('exp_o=',exp_o)
 #print('product & 0x100000=',bin(product & 0x100000))
 if(product&0x200000):  #20000?
  exp_o = exp_o + 1
  product = product >> 1
 if(exp_o < 15):
  while(exp_o < 15):
   exp_o = exp_o + 1
   product = product >> 1
 else:
  while((product & 0x100000)==0 and exp_o != 15):
   exp_o = exp_o - 1
   product = product << 1
 exp_o = exp_o - 15
 if(exp_o == 0):
  product = product >> 1
 #print('product=',bin(product)[2:])
 frac_o = (product & 0x1ffc00) >> 10
 #print('frac_o=',bin(frac_o)[2:])
 if(product & 0x200):
  frac_o = frac_o + 1
 sign_o = sign_o << 15
 exp_o = exp_o << 10
 sign_o = sign_o | exp_o | frac_o
 o = sign_o
 return o
'''
 if __name__ == '__main__':
 ##print('bb')
 ans = mul16('1100000000011100','1011111110110011')
 print('ans = ',bin(ans)[2:].zfill(16))
 print('true ans=','0100001111101001')
 ##print(hex(-2.0),hex(-3.0))
'''