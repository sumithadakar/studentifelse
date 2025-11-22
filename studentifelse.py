import sys
if len(sys.argv) == 3:
  script_name = sys.argv[0]
  name = sys.argv[1]
  rollno = sys.argv[2]
  print("yser provided input values:")
else:
  script_name = sys.argv[0]
  name = "sumit'
  rollno = "101"
  print("no input given - using default values:")

print("script name:", script_name)
print("student name:", name)
print("roll number:", rollno)
