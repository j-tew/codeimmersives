def myMean(nums):
    l = sorted(nums)
    return float((l[0] + l[-1]) / 2)

with open('sql/covid_vax_rates.txt', 'r') as f:
    lines = f.readlines()
    cols = lines.pop(0).split('\t')
    cols[-1] = cols[-1][:-1]

data = {
    line.split('\t')[0]: {
        cols[1]: line.split('\t')[1],
        cols[2]: line.split('\t')[2],
        cols[3]: line.split('\t')[3],
        cols[4]: line.split('\t')[4]
    } for line in lines
}

percent_refused = [float(state['SHARE_ADULT_POP_OF_WHO_WILL_LIKELY_REFUSE_VACCINATION'][:-1]) for state in data.values()]
vax_maj = [(state,float(vax_pop['POP_CURRENTLY_FULLY_VACCINATED'][:-1])) for state,vax_pop in data.items() if float(vax_pop['POP_CURRENTLY_FULLY_VACCINATED'][:-1]) > float(60)]

print(f'Average percentage of people refusing vaccination:\n{myMean(percent_refused)}%\n\nStates with higher than 60% vaccination:')
for state in vax_maj:
    print(f'{state[0]} --> {state[1]}%')

