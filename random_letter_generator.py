from string import ascii_letters, ascii_lowercase , digits
#from random import shuffle 
from collections import OrderedDict
from tqdm import tqdm
from time import time 
from numpy import random, int64

# Main fuction 
def pw_gen(string: str,  length: int, n: int = 1): 
	# 're_res' re -> rearrange and res -> result
	# 'pw_raw' -> passworld list as raw data  
	# 'pw' -> Passworld list

	s = [] # for letters 
	pw_raw = [] # to store all poassable valves 

	s.extend(list(string)) # convert string to list and store in 's' 

	start = time ()
	# Main loop 
	for i in tqdm(range(n)):
		r = random.shuffle(s) # random the letters 
		re = "".join(s[0:length]) # all random letter as per given length 
		pw = pw_raw.append(re) # save all at valve in 'pw' array 
	
	 
	# pw_raw_ = [(pw_raw.append(("".join(s[0: length]))) , shuffle(s) )for i in tqdm( range(n) )]
	
	end = time()
	print("Time taken: ", (end - start))
	res = list(OrderedDict.fromkeys(pw_raw)) # sort all thing like small elements 
	re_res = "\n".join(res) # and make final array called 're_res' re -> rearrange and res -> result 
	
	# Print number of elements in all arrays 
	print("re : " ,len(re),'\n',"pw_raw: ", len(pw_raw), '\n', "res : " ,len(res), '\n',"re_res : " ,len(re_res))
	
	with open("test\\password_1_2.lst", 'w') as pw:
		pw.write(re_res)
		pw.close()

	return re_res

# Driver Code  
if __name__ == "__main__":
	apt = ascii_lowercase
	a =  pw_gen(apt, 5, 15000000)
