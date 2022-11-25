import pandas as pd
from chart import generate_charts as generate_charts
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse


app = FastAPI()

@app.get("/api")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.get("/api2")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}





@app.get("/api3")
def assign_variables():
  data = pd.read_csv('./datasets/data.csv')
  titles = list(data.head(0))
  head_options = ''

  for title in titles:
    head_options += f'<option value="{title}">{title}</option>'

  html_content = f'''
  <html>
    <body>
      <p>CSV to Chart</p>
        <form action='/chart'>

        <label for="csv_file">Choose a csv file:</label><br>
        <input type="file" id="csv_file" name="csv_file"><br><br>

        <label for="column1">Identifier</label><br>
        <select name="head_selection_1"><br>
          {head_options}
        </select><br><br>
        
        <label for="head_selection_2">Values:</label><br>
        <select name="head_selection_2"><br>
          {head_options}
        </select><br><br>

        <label for="type_chart">Type Chart:</label><br>
        <select name="chart_selection"><br>
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
async def return_chart(head_selection_1,head_selection_2,chart_selection):
  data = pd.read_csv('./datasets/data.csv')
  titles = list(data.head(0))
  column1 = head_selection_1 
  column2 = head_selection_2 
  type_chart = chart_selection
  
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