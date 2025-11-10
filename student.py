import sys
if len(sys.argv) ==3:
  script_name=sys.argv[0]
  name=sys.argv[1]
  rollno=sys.argv[2]
  print("user provided input")
else:
  script_name=sys.argv[0]
  name="Pragati"
  rollno="102"
  print("values assigned")
print("script name",script_name)
print("name",name)
print("rollno",rollno)
  
