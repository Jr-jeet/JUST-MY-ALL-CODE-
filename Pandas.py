import pandas as p 
# df=p.read_csv("himani  sem 2 addmission.pdf",encoding=latin1 / utf-8)
#(if error come then:-  then pass in encoding , utf-8  or latin1 )
# df=p.read_excel("himani  sem 2 addmission.pdf",encoding=latin1 / utf-8)
# df=p.read_json("himani  sem 2 addmission.pdf",encoding=latin1 / utf-8)
# print(df)              use for read data "what is in the data"
# gcsfs   if data in google cloude

# data ={
#  "name":['ram','jeet','Dhiraj','jimo','raj','elo','luv','muskan','simran','game'],
#  "age":[20,32,54,23,45,67,89,12,34,56],
# "salary":[92000,10000,20000,30000,37777,90000,70000,40000,23000,40020],
#  "city":['mumbai','jaipur','kerala','delhi','pune','banglore','chennai','kolkata','lucknow','patna']

# }

# df=p.DataFrame(data)
# print(df)
# print(df.describe)
# df.to_csv("df.csv",index=False) #use for save data in csv file

# data ={
#  "name":['ram','jeet','Dhiraj'],
#  "age":[20,32,54],
#  "city":['mumbai','jaipur','kerala']

# }

# df=p.DataFrame(data)
# print(df)
# df.to_json("df.json",index=False)                #use for save data in json file

# df=p.read_csv("C:\Jeet.py.01\venv\Scripts\ibm-research_enterprise-ops_leaderboard.csv")
# print(df.head((3)))        # hee we get first row of data
  # there is 2 methods     "head" and "tail"  head is use for first row and tail is use for last row

# df=p.read_json("df.json")
# r=df.tail(1)
# print(r)    


# df=p.read_excel('C:\Jeet.py.01\Delinquency_prediction_dataset.xlsx')
# print(df.head(4))
# print(df.info())       #it gives you about the dataset
