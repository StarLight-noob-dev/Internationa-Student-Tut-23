def find_new_tutor(data):
    """
    Find the top 3 Students based on their Grades to be tutors
    :param data: Dictionary containing the Name (key) and their grades (value) of the students
    """
    # As we store the data in a new dictionary the original data is not changed
    tutors = {}
    for i in data:

        val = data[i]

        if val[0]=='EPI':
            grades=val[1]
            tutors[i]=sum(grades)/len(grades)

    # Order based on the float value related to the name then only returns the first 3 items
    out = dict(sorted(tutors.items(), key=lambda x: x[1])[:3])
    return out



Students = {
    'Kansas':['EPI',(1,2,1,1)],
    'Robert':['GPR',(3,2,4,4,5)],
    'Olaf':['EPI',(3,)],
    'Kolleger':['EPI',(1,2)],
    'Oliver':['Mathe',(3,4)],
    'Benjamin':['EPI',(2,4,1)],
    'Nicolas':['EPI',(1,2,3,1)]
    }

print(find_new_tutor(Students))