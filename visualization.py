import plotly.graph_objects as go
from plotly.subplots import make_subplots

def visualize_data(data, anomalies):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        vertical_spacing=0.1, subplot_titles=('Data Stream', 'Detected Anomalies'))
    
    fig.add_trace(go.Scatter(y=data, mode='lines', name='Data Stream'), row=1, col=1)
    fig.add_trace(go.Scatter(x=anomalies, y=data[anomalies], mode='markers', 
                             marker=dict(color='red', size=8), name='Anomalies'), row=2, col=1)
    
    fig.update_layout(title='Real-Time Anomaly Detection', height=600, showlegend=True)
    fig.show()
