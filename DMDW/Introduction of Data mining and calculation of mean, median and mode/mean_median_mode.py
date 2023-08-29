data_list=[12,23,34,45,56,67,78,89,90]
#mean
sum_mean=0
data_length=len(data_list)
for y in data_list:
  sum_mean=sum_mean+y
final_mean=sum_mean/data_length
print("Final Mean=",final_mean)

#median
data_list_median=data_list
data_list_median.sort()
if(len(data_list_median)%2==0):
  median=len(data_list_median)//2
  finalmedian=data_list_median[median-1]+data_list_median[median]
  final_median=finalmedian/2
  print("Final Median=",final_median)
else:
  median=len(data_list_median)//2
  final_median=data_list_median[median]
  print("Final Median",final_median)

#mode
data_list_mode=data_list_median
x=[]
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
for i in data_list_mode:
  x.append(countX(data_list_mode,i))
x.sort()

index=-1
max_x=max(x)
for i in range(len(x)):
  if(x[i]==max_x):
    index=i
    break

print("Final Mode",data_list_mode[index-1])



#variance
data_list_variance=data_list_mode
list2=[]
sum_all=0
for i in data_list_variance:
  sum_all=sum_all+((i-final_mean)**2)
final_variance=sum_all/len(data_list_variance)
print("The Final Variance is",final_variance)




#standard deviation
final_standard_deviation=final_variance**0.5
print("Final Standard Deviation is",final_standard_deviation)
