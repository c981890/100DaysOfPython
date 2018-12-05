# In this bite you will work with a list of names.
# First you will write a function to take out duplicates and title case them.
# Then you will sort the list in alphabetical descending order by surname and
# lastly determine what the shortest first name is. For this exercise you can
# assume there is always one name and one surname.
# With some handy Python builtins you can write this in a pretty concise way.
# Get it sorted :)

from operator import itemgetter

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    dedup_names = []
    for i in names:
        if i.title() not in dedup_names:
            dedup_names.append(i.title())
    return dedup_names

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""

    splitted_names = []
    joined_names = []
    names = dedup_and_title_case_names(names)

    for i in names:
        splitted_names.append(i.split())
    sorted_names = sorted(splitted_names, key=itemgetter(1), reverse=True)
    for i in sorted_names:
        joined_names.append(' '.join(i))
    return joined_names


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    splitted_names = []
    joined_names = []
    names = dedup_and_title_case_names(names)
    for i in names:
        splitted_names.append(i.split())
    def length_of_first_item(splitted_names):
        return len(splitted_names[0])
    sorted_names = sorted(splitted_names, key=length_of_first_item)
    return sorted_names[0][0]

shortest_first_name(NAMES)
