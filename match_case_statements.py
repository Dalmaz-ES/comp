# MATCH CASE STATEMENTS (switch) = An alternative to elif statements
#                             execute some code if a value matches a 'case'
#                             benefits: cleaner and readable syntax

"""
def day_of_week(day):
    if day == 1:
        return "Its Sunday"
    elif day == 2:
        return "Its Monday"
    elif day == 3:
        return "Its Tuesday"
    elif day == 4:
        return "Its Wednesday"
    elif day == 5:
        return "Its Thursday"
    elif day == 6:
        return "Its Friday"
    elif day == 7:
        return "Its Saturday"
    else:
        return "Invalid day"

print(day_of_week(1))
"""



#rather then many elif statements use:
"""
def day_of_week(day):

    match day:
        case 1:
            return "Its Sunday"
        case 2:
            return "Its Monday"
        case 3:
            return "Its Tuesday"
        case 4:
            return "Its Wednesday"
        case 5:
            return "Its Thursday"
        case 6:
            return "Its Friday"
        case 7:
            return "Its Saturday"
        case _:
            return "Invalid day"

print(day_of_week(2))
"""



#similar example
"""
def is_weekend(day):

    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Sunday"))
"""



