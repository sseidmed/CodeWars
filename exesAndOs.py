def xo(s):
  
  o = ''
  x = ''
  new_str = s.lower()
  for i in range(len(new_str)):
    if new_str[i] == 'o':
      o+=new_str[i]
    if new_str[i] == 'x':
      x+=new_str[i]
  if len(x) == len(o):
    return True
  return False

print(xo("zzoo"))

'''
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false'''

#lower case all characters
#loop through the string:
# no x, no o, should return True 
#initialize 2 empty variables and increment if x or o found
#compare len of both variables at the print
# if both equal to each other, return True, else False
