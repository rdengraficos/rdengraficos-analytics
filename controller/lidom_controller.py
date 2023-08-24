from dash import Input, Output, callback
from app import app
from models.lidom_model import LidomModel
from graph.lidom_graph import LidomGraph


@callback(
    Output(component_id='ganados_grafico', component_property='children'),
    Input(component_id='temporada', component_property='value')
)
def update_vis(temporada):
    print(temporada)
    ganados = LidomModel.get_position_table()
    fig = LidomGraph.build_position_table_line(ganados)

    return fig