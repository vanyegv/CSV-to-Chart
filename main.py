import pandas as pd
from chart import generate_charts as generate_charts
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/api")
def assign_variables():
  data = pd.read_csv('./datasets/data.csv')
  titles = list(data.head(0))
  html_content = f'''
  <html>
    <body>
      <p>Select a column a column</p>
      <p>{titles}</p>
        <form action='/chart'>
        <label for="column1">First column:</label><br>
        <input type="text" id="column1_" name="column1_"><br>
        
        <label for="column2">Second Column:</label><br>
        <input type="text" id="column2_" name="column2_"><br>
        
        <label for="type_chart">Type Chart:</label><br>
        <input type="text" id="type_chart_" name="type_chart_"><br>
        
        <input type="submit" value="Submit">
        </form>
    </body>
  </html>
  '''
  return HTMLResponse(content=html_content,status_code=200)

@app.get("/chart")
async def return_chart(column1_,column2_,type_chart_):
  data = pd.read_csv('./datasets/data.csv')
  titles = list(data.head(0))
  #dict_titles = { n:title[n] for n,title in range(0,len(titles)) }
  
  #column1 = input(f'Introduce 2 column names to filter \n{titles} \n=> ')
  #column2 = input('=> ')
  #type_chart = input('\nIntroduce type of chart\nbar chart\tpie chart\n=> ')
  column1 = column1_ #'columna1'
  column2 = column2_ #'columna2'
  type_chart = type_chart_#'pie'
  
  if (column1 in titles) and (column2 in titles) and ('pie' in type_chart or 'bar' in type_chart):
    value1 = list(data[column1])
    value2 = list(data[column2])
    chart = generate_charts(type_chart,value1,value2,column1,column2)
    print(chart)
    return FileResponse(chart) 

  else:
    print('Selection not valid\n')
    return_chart()
    

if __name__ == '__main__':
  run()