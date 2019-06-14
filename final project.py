import pandas as pd 
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_excel("GISdata.xlsx", sheet_name = "cancercases")

print(df)

cancer = go.Bar(x = df ["CancerType"], y = df ["Number"]

                ) 

plot([cancer])

titles = go.Layout(
                        #define title of the group
                        title = "Cancer Cases",
                        
                        #define title for x axis
                        xaxis = go.layout.XAxis(
                                title = go.layout.xaxis.Title(
                                text = "Cancer Types" 
                             )
                         ),
                            #define for the title of the y axis
                        yaxis = go.layout.YAxis(
                                title = go.layout.yaxis.Title(
                                text = "Number of Cancer Cases" ,
                                )
                            )
                        )

fig = go.Figure (data = [cancer], layout = titles)
plot(fig)
