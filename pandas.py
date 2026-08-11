#PANDAS:

#1.CREATE DB:
import pandas as pd
data={"employeeID":[101,102,103,104,105,106,107,108],
      "name":["siva","priya","pavi","bharath","sakthi","sudhies","babu","kaja"],
      "dept":["cse","it","cse","hr","finance","cse","ece","cse"],
      "salary":[10000,20000,30000,40000,50000,60000,70000,80000],
      "JoiningDate":["2023-01-15", "2022-06-20", "2023-03-10", "2021-08-12",
        "2022-11-05", "2024-01-20", "2023-07-18", "2024-02-25"]}
df=pd.DataFrame(data)
df["JoiningData"]=pd.to_datetime(df["JoiningDate"])
print(df)

#2.USE .info() AND .describe():
print("DataFrame informations:")
df.info()
print("\nSummary statistics:")
print(df.describe())

#3.FILTER EMPLOYEES:
filtered=df[(df['JoiningDate']>"2023-01-01")&
            (df["salary"]>50000)]
print(filtered)

#4.AVERAGE.MIN,MAX:
result=df.groupby("dept")["salary"].agg(["mean","min","max"])
print(result)

#5.HANDLE NaN VALUES:
df.loc[2,"salary"]=None
df.loc[5,"salary"]=None
print(df)
print(df["salary"].isnull())
df_dropped = df.dropna()
print(df_dropped)
mean_salary = df["salary"].mean()
df["salary"] = df["salary"].fillna(mean_salary)
print(df)

#6.SORT BY SALARY DESC AND DEPT ASC:
sorted_df=df.sort_values(
    by=["salary","dept"],
    ascending=[False,True])
print(sorted_df)

#7.CLASSIFY EMPLOYEES AS SENIOR/MID/JUNIOR:
def classify_salary(salary):
    if salary>=60000:
        return "senior"
    elif salary>=50000:
        return "mid"
    else:
        return "junior"
df["level"]=df["salary"].apply(classify_salary)
print(df[["name","salary","level"]])

#8.MERGE TWO DF:
employee=pd.DataFrame({"employeeID":[101,102],
                       "name":["siva","priya"],
                       "dept":["cse","it"]})
budget=pd.DataFrame({"dept":["it","hr"],
                     "budget":[500000,300000]})

# #INNER JOIN:
inner = pd.merge(
    employee,
    budget,
    on="dept",
    how="inner"
)
print("Inner Join:")
print(inner)

# #LEFT JOIN:
left = pd.merge(
    employee,
    budget,
    on="dept",
    how="left"
)
print("Left Join:")
print(left)

# #RIGHT JON:
right = pd.merge(
    employee,
    budget,
    on="dept",
    how="right"
)
print("Right Join:")
print(right)

# #OUTER JOIN:
outer = pd.merge(
    employee,
    budget,
    on="dept",
    how="outer"
)
print("Outer Join:")
print(outer)

#9.CREATE A PIVOT TABLE:
df["City"] = [
    "Chennai", "Chennai", "Bangalore", "Chennai",
    "Bangalore", "Chennai", "Bangalore", "Chennai"
]
pivot = pd.pivot_table(
    df,
    values="salary",
    index="dept",
    columns="City",
    aggfunc="mean"
)
print(pivot)

#10.EXPORT TO CSV ANF READ IT BACK:
df.to_csv("employees_cleaned.csv", index=False)
new_df = pd.read_csv("employees_cleaned.csv")
print(new_df)
print(df.equals(new_df))