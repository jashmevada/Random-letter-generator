from string import ascii_letters, ascii_lowercase , digits
from collections import OrderedDict
from tqdm import tqdm
from time import time
from numpy import random


def pw_gen(string: str,  length: int, n: int = 1):
	# 're_res' re -> rearrange and res -> result
	# 'pw_raw' -> password list as raw data
	# 'pw' -> password list

	s = [] # for letters
	pw_raw = [] # to store all poassable valves

	s.extend(list(string)) # convert string to list and store in 's'
	
	start = time ()
	
	for i in tqdm(range(n)):
		random.shuffle(s) # random the letters
		re = "".join(s[0:length]) # make random letter from list 's' of input length
		pw = pw_raw.append(re) # save all at valve in 'pw' array
	
	end = time()
	print("Time taken: ", (end - start))
	res = list(OrderedDict.fromkeys(pw_raw)) # Remove same letter from 'pw'.
	re_res = "\n".join(res) # final list with random letters and removed all same letter and only content unique letters.
	
	# Print number of elements in all arrays
	print("re : " ,len(re),'\n',"pw_raw: ", len(pw_raw), '\n', "res : " ,len(res), '\n',"re_res : " ,len(re_res))
	
	filename = input("Enter File name: ")
	
	with open(f"{filename}", 'w') as pw:
		pw.write(re_res)
		pw.close()
	
	return re_res

if __name__ == "__main__":
	pw_gen(ascii_lowercase, 5, 150000)
	
