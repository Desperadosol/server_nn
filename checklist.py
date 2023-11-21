def generateSample(subjects: list, groups=['group1', 'group2', 'group3', 'group4', 'group5', 'group6']) -> list:

    sample = []
    #Due to language restrictions we have to use additional variables in order to avoid repetition
    firstLangName = ""
    secondLangName = ""
    subjects = sorted(subjects, key=lambda k: k['score'], reverse=True)

    for i in groups:
        for j in subjects:
            if i == j['group']:
                if j['group'] == "group1":
                    firstLangName = j['name']
                    sample.append(j)
                    break
                elif j['group'] == "group2":
                    if firstLangName == j['name']:
                        continue
                    else:
                        secondLangName = j['name']
                        sample.append(j)
                        break
                else:
                    sample.append(j)
                    break
    
    if len(sample) < 6:
        for i in subjects:
            if i not in sample and i['group'] in ['group2','group3','group4'] and i['name'] not in [firstLangName, secondLangName]:
                sample.append(i)
                break
    
    sorted_subjects = sorted(enumerate(sample), key=lambda x: (x[1]['score'], x[0]), reverse=True)

    for i, (_, subject) in enumerate(sorted_subjects):
        subject['level'] = 'HL' if i < 3 else 'SL'

    newSample = [subject for _, subject in sorted(sorted_subjects, key=lambda x: x[0])]

    return newSample
