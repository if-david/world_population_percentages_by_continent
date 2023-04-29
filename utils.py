def get_population_percentages(filtered_data):
    population_percentages = {}
    for country in filtered_data:
        population_percentages[country['Country']] = country['World Population Percentage']
    labels = population_percentages.keys()
    values = population_percentages.values()
    return labels, values

def population_by_continent(data, continent_name):
    try:  
        filtered_data = [continent for continent in data if continent['Continent'] == continent_name]
        if len(filtered_data) == 0:
            raise ValueError('No se encontraron países en ese continente')
    except ValueError as error:
        print(str(error))
        exit()
    return filtered_data    