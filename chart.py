import matplotlib.pyplot as plt

def generate_charts(type_chart,values1,values2,column1,column2):
    
    if 'bar' in type_chart :
        fig, ax = plt.subplots()
        ax.bar(values1,values2)
        plt.savefig(f'./charts/bar-{column1}-{column2}.png')
        plt.close()
    else:
        fig, ax = plt.subplots()
        ax.pie(values2,labels=values1)
        ax.axis('equal')
        plt.savefig(f'./charts/pie-{column1}-{column2}.png')
        plt.close()