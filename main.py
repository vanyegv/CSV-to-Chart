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
  menu = ''
  
  for title in titles:
    menu += f'<option value="{title}">{title}</option>'

  html_content = f'''
  <html>
    <body>
      <p>Select a column</p>
        <form action='/chart'>

        <label for="column1">Identifier</label><br>
        <select name="column1_"><br>
          {menu}
        </select><br><br>
        
        <label for="column2_">Values:</label><br>
        <select name="column2_"><br>
          {menu}
        </select><br><br>

        <label for="type_chart">Type Chart:</label><br>
        <select name="type_chart_"><br>
          <option value="bar chart">bar chart</option><br>
          <option value="pie chart">pie chart</option><br>
        </select><br><br>

        <input type="submit" value="Submit"><br>
        </form>
    </body>
  </html>
  '''
  return HTMLResponse(content=html_content,status_code=200)

@app.get("/chart")
async def return_chart(column1_,column2_,type_chart_):
  data = pd.read_csv('./datasets/data.csv')
  titles = list(data.head(0))
  column1 = column1_ 
  column2 = column2_ 
  type_chart = type_chart_
  
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