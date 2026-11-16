import numpy as np

hours=np.array([2,4,5,1,6,3,8,7,2,5])

count1=0
for i in hours:
	count1+=1

total_study_hours=sum(hours)
print(total_study_hours)

average_study_hour=np.mean(hours)
print(average_study_hour)

max_study_hours=np.max(hours)
print(max_study_hours)

min_study_hours=np.min(hours)
print(min_study_hours)

students_study_more_than_two_hours=hours[hours>4]
print(students_study_more_than_two_hours)

count=0

for i in students_study_more_than_two_hours:
	count+=1
print(count)

percentage_students_study_more_than_two_hours=(count/count1)*100
print(percentage_students_study_more_than_two_hours)

marks=np.array([35,80,45,90,25,75,60,95])

ma=marks[marks>=60]

print(ma)
mw=np.count_nonzero(marks[marks>=40])
print(mw)

per=(np.count_nonzero(marks[marks<40])/len(marks))*100
print(per)

new=np.where(marks<40,40,marks)
print(new)
