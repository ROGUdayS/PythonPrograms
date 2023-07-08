TimeTable={"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[]}
def initTimeTable():
    for i in [9,10,11,12,13,14,15,16]:
        for j in TimeTable.keys():
            TimeTable[j].append(" None ")

def days_in_TT():
    return input("Input the days of the week (in format as Monday, Tuesday , Wednesday, Thursday, Friday, Saturday) :")

def time_slots_in_TT():
    return int(input("Input the Time slot (from 9, 10, 11, 12, 13, 14, 15, 16) :"))

def course_in_TT():
    return input("Input the course you would like to add :")

def insertion(day, time, course):
    if TimeTable[day][time-9] == " None ":
        TimeTable[day][time-9] = course
        return course
    else:
        return " None "

def delete(day,time):
    TimeTable[day][time-9] = "None"
    return

def replace(day,time,course):
    TimeTable[day][time-9] = course
    return

initTimeTable()
while True:
    print("------------------ Time Table ------------------")
    choice=input("""Select the Operation you want to perform :
    1. View the Time Table
    2. Insert Course Into the Time Table
    3. Delete a Course in the Time Table
    4. Replace a Course in the Time Table
    5. Exit the Time Table
    """)
    if choice=="1":
        for i in TimeTable:
            print(i, TimeTable[i])

    elif choice=="2":
        day=days_in_TT()
        time=time_slots_in_TT()
        course=course_in_TT()
        insertion(day,time,course)

    elif choice=="3":
        day=days_in_TT()
        time=time_slots_in_TT()
        delete(day,time)

    elif choice=="4":
        day = days_in_TT()
        time = time_slots_in_TT()
        course = course_in_TT()
        replace(day, time, course)

    elif choice=="5":
        exit()