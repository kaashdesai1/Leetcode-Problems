 def is_match(s,p):
	   if len(s) == 0 and len(p) == 0:
		   return True

	   if len(s) > 0 and len(p) == 0:
		   return False

	   first_match = bool(s) and p[0] in {s[0], '.'}

	   if len(p) >= 2 and p[1] == '*':
		   # return (excluding or including )
		   # when excluding  is_match(s,p[2:]) 
		   # think about case where s = "b" and p = "a*b" 
		   # if we exclude a* then first_match is already false so we can't condifer it when excluding
		   # 
		   return is_match(s,p[2:]) or (first_match and is_match(s[1:],p))

	   return first_match and is_match(s[1:],p[1:])
