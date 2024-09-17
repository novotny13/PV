tuple1 = (2, 4 , 5,"pepa","nothing",  4 , 5,"pepa", True)
list = [2, 4 , 5,"pepa","nothing", 4 , 5,"pepa", True]
set = {"apple", "banana", "cherry", True, 1, 2, "cherry"}
dic = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "brand": "Lexus",

}
string = "peeeep123"
string
print(tuple1)
print(list)
print(set)
print(dic)
print(string)

dlist = [tuple1, list, set,dic,string]
dtuple1 = (tuple1, list, set,dic,string)
dset = {tuple1,string}#u can only put strings nad tupples in set (out of these 5)
ddic = {
  "brand": "list",
  "model": set,
  "year": list,
  "brand": tuple1,
    "something": dic,

}
dstring = "9"
print("test for nesting------------------------------")
print(dlist)
print(dtuple1)
print(dset)
print(ddic)
print("tuple methods---------------------------------")
print(dir(tuple1))

print("Test for len()--------------------------------")
print(len(tuple1))
print(len(list))
print(len(set))
print(len(dic))
print(len(string))

print("test for size change--------------------------")
print("tuple methods---------------------------------")
print(dir(tuple1))
print("----------------------------------------------")
print("--LIST--")
print(str(len(list))+" before change")
print(str(id(list)) + " id")
list.append(5)
print(str(len(list)) + " after change")
print(str(id(list)) + " id")
print("--SET--")
print(str(len(set))+" before change")
print(str(id(set)) + " id")
set.add(5)
print(str(len(set)) + " after change")
print(str(id(set)) + " id")
print("--DIRECTORY--")
print(str(len(dic))+" before change")
print(str(id(dic)) + " id")
dic.clear()
print(str(len(dic)) + " after change")
print(str(id(dic)) + " id")
print("--STRING--")
print(str(len(string))+" before change")
print(str(id(string)) + " id")
string += "5"
print(str(len(string)) + " after change")
print(str(id(string)) + " id")
print("\n")
print("\n")
print("test for inserting into colections-------------")
print("\n")
print("--LIST--")
print(dir(tuple1))
print("-----------------------------------------------")
print("\n")
print("--LIST--")
print(list)
print(str(id(list)) + " id")
list.append(5)
print(str(id(list)) + " id")
print(list)
list.insert(1,None)
print(str(id(list)) + " id")
print(list)
print("\n")
print("--SET--")
print(set)
print(str(id(set)) + " id")
set.add(789)
set.add(None)

print(set)
print(str(id(set)) + " id")
print("\n")
print("--DIRECTORY--")

print(str(id(dic)) + " id")
print("\n")
print("--STRING--")

print(str(id(string)) + " id")
print("\n")