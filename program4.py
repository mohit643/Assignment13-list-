""" Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"] """


list=["Java", "SQL", "C", "Reactnative","Javascript", "Python"]

len=len(list)
for  x in range(len):
   if list[x]=='SQL':
     list[x]='NoSQL'

   elif list[x]=='Reactnative':
      list[x]='Flutter'  
  
print(list)   