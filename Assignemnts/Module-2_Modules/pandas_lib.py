import pandas

data={
    "id":[1,2,3,4,5],
    "name":["sanket","nirav","ashok","hitesh","darshan"],
    "city":["rajkot","ahmedabad","bhavnagar","surat","baroda"]
}
#print(data)

x=pandas.DataFrame(data)
print(x)