import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('python 102\\app_readcsv\\data.csv')
  continents = set(country['Continent'] for country in data)
  # print(list(continents))
  continent_name = input(f"Ingresa el continente que deseas filtrar {continents}: ")
  result = utils.population_by_continent(data, continent_name)
  # print(result)
  labels, values = utils.get_population_percentages(result)
  # print(labels, values)
    
#   charts.generate_bar_chart(labels, values)
  charts.generate_pie_chart(labels, values)


if __name__ == '__main__':
  run()





