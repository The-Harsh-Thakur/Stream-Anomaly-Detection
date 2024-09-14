import plotly.graph_objects as go
from plotly.offline import plot  # For offline plotting

def visualize_data(data_stream, anomaly_scores):
    fig = go.Figure()

    # Add trace for data stream
    fig.add_trace(go.Scatter(
        x=list(range(len(data_stream))),
        y=data_stream,
        mode='lines',
        name='Data Stream'
    ))

    # Add trace for anomaly scores
    fig.add_trace(go.Scatter(
        x=list(range(len(anomaly_scores))),
        y=anomaly_scores,
        mode='lines',
        name='Anomaly Score',
        line=dict(color='red')
    ))

    # Update layout
    fig.update_layout(
        title="Anomaly Detection in Data Stream",
        xaxis_title="Index",
        yaxis_title="Value",
        height=600
    )

    # Save the plot as an HTML file and open it in the default browser
    plot(fig, filename='anomaly_detection_plot.html', auto_open=True)
