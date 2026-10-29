# awarding a person competing in a triathlon competion
# asking the user for their finishing time in 3 events: \
# swimming, cycling, running

swimming_time = float(input("Enter your swimming time in minutes: "))
cycling_time = float(input("Enter your cycling time in minutes: "))
running_time = float(input("Enter your running time in minutes: "))

# calculating total time
total_time = swimming_time + cycling_time + running_time

# total time aquisition displayed
print(f"total time for the triathlon is: {total_time} minutes.")

# awards based on total time
if total_time <= 100:
    award = "Pronvincial Colours"
elif total_time <= 105:
    award = "Provincial Half Colours"
elif total_time <= 110:
    award = "Provincial Scroll"

else:
    award = "No Award"

#  award obtained displayed
print(f"award: {award}")
