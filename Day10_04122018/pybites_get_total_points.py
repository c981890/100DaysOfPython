from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5),
               }


def get_total_points(belts=ninja_belts_updated):
    """Calculate the amount of points rewarded on PyBites given the
       ninja_belts dictionary, formula: belt score x belt owners (aka ninjas)
       (of course there are more points but let's keep it simple)

       Make your code generic so if we update ninja_belts to include
       more belts (which we do in the tests) it will still work.

       Ah and you can get score and ninjas from the namedtuple with nice
       attribute access: belt.score / belt.ninjas (reason why we get
       you familiar with namedtuple here, because we love them and use
       them all over the place!)

       Return the total number of points int from the function."""

    points = 0
    for key in belts.keys():
        points += belts[key].score * belts[key].ninjas
    return points

get_total_points(ninja_belts)


#E        +  where 2675 = get_total_points({
#    'black': BeltStats(score=600, ninjas=5),
#    'blue': BeltStats(score=250, ninjas=5),
#    'brown': BeltStats(score=400, ninjas=2),
#    'green': BeltStats(score=175, ninjas=1), ...})
