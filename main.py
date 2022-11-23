import pandas as pd
import matplotlib

def run():
  data = pd.read_csv('data.csv')
  titles = list(data.head(0))
  #print(titles)
  column1 = input(f'Select column \n{titles}\n=> ')
  column2 = input('=> ')
  
  if column1 not in titles or column2 not in titles:
    print('Wrong selection')
    run()
  
  else:
    print('Selection done')
    value1 = list(data[column1])
    value2 = list(data[column2])
    
    print(value1)

    
  return

if __name__ == '__main__':
  run()