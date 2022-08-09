from string import ascii_letters, ascii_lowercase , digits
from collections import OrderedDict
from tqdm import tqdm
from time import time 
from numpy import random

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
		random.shuffle(s) # random the letters 
		re = "".join(s[0:length]) # all random letter as per given length 
		pw = pw_raw.append(re) # save all at valve in 'pw' array 	
	
	end = time()
	print("Time taken: ", (end - start))
	res = list(OrderedDict.fromkeys(pw_raw)) # sort all thing like small elements 
	re_res = "\n".join(res) # and make final array called 're_res' re -> rearrange and res -> result 
	
	# Print number of elements in all arrays 
	print("re : " ,len(re),'\n',"pw_raw: ", len(pw_raw), '\n', "res : " ,len(res), '\n',"re_res : " ,len(re_res))
	
	filename = input("Enter File name: ")
	
	with open(f"{filename}", 'w') as pw:
		pw.write(re_res)
		pw.close()
	
	return re_res

# Driver Code  
if __name__ == "__main__":
	random_letter = ascii_lowercase
	pw_gen(random_letter, 5, 150000)