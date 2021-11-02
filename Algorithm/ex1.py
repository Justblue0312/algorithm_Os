s = '123456789'
res = []

def combinations(index, sofar, total):
	if index == len(s):
		if total == 100:
			res.append(sofar)
		return

	for i in range(index+1, len(s)+1):
		combinations(i, sofar+'+'+s[index:i] if sofar else s[index:i], total+int(s[index:i]))
		combinations(i, sofar+'-'+s[index:i], total-int(s[index:i]))

combinations(0, '', 0)
for idx, r in enumerate(res):
  print(idx+1, r)