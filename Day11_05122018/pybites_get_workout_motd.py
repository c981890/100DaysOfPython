workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
    """Title case passed in day argument (monday or MONDAY -> Monday)
       and check if it is in the given workout_schedule dict.

       If it is there retrieve the workout, if not raise a KeyError.

       Return the chill or go_train variable depending the retrieved
       workout value ('Rest' or workout bla)

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    correct_day = day.title()
    if correct_day in workout_schedule:
        if workout_schedule[correct_day] == 'Rest':
            result = chill
        else:
            result = go_train.format(workout_schedule[correct_day])
    else:
        raise KeyError('no weekday in input')
    return result

# Shorter version
#    day = day.title()
#
#    if day not in workout_schedule:
#        raise KeyError(f'{day} is not a valid day')
#
#    workout = workout_schedule.get(day)
#
#    return chill if workout == rest else go_train.format(workout)
