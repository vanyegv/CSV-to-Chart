import pandas as pd
from chart import generate_charts as generate_charts

def run():
  data = pd.read_csv('./datasets/data.csv')
  titles = list(data.head(0))
  #dict_titles = { n:title[n] for n,title in range(0,len(titles)) }
  
  column1 = input(f'Introduce 2 column names to filter \n{titles} \n=> ')
  column2 = input('=> ')
  chart = input('\nIntroduce type of chart\nbar chart\tpie chart\n=> ')

  if (column1 in titles) and (column2 in titles) and ('pie' in chart or 'bar' in chart):
    value1 = list(data[column1])
    value2 = list(data[column2])
    generate_charts(type,value1,value2)
    
  else:
    print('Selection not valid\n')
    run()
  





    
  return

if __name__ == '__main__':
  run()