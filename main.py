import pandas as pd
from chart import generate_charts as generate_charts
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def run():
  data = pd.read_csv('./datasets/data.csv')
  titles = list(data.head(0))
  #dict_titles = { n:title[n] for n,title in range(0,len(titles)) }
  
  #column1 = input(f'Introduce 2 column names to filter \n{titles} \n=> ')
  #column2 = input('=> ')
  #type_chart = input('\nIntroduce type of chart\nbar chart\tpie chart\n=> ')
  column1 = 'columna1'
  column2 = 'columna2'
  type_chart = 'bar'
  
  if (column1 in titles) and (column2 in titles) and ('pie' in type_chart or 'bar' in type_chart):
    value1 = list(data[column1])
    value2 = list(data[column2])
    chart = generate_charts(type_chart,value1,value2,column1,column2)
    print(chart)

    return FileResponse(chart)  #f'<img src="{chart}" alt="chart">'
  else:
    print('Selection not valid\n')
    run()

  
    

if __name__ == '__main__':
  run()