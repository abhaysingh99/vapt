file=open('/Users/vishalkumar/Desktop/testing/mysite/text3.txt','r')
data3 = file.readlines()
file.close()
data3= str(data3[0])
data3 = data3.strip('Nmap done: ')
data3 = [data3]






# string = ' xoxo love xoxo   '

# # Leading whitepsace are removed
# print(string.strip(' xoxoe'))