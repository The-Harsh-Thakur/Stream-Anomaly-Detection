import plotly.graph_objects as go
from plotly.offline import plot  # For offline plotting

def visualize_data(data_stream, anomaly_scores):
    """
    Visualizes the data stream and anomaly scores using Plotly.

    Args:
        data_stream (list or np.ndarray): The original data stream to be visualized.
        anomaly_scores (list or np.ndarray): The corresponding anomaly scores for the data stream.
    """
    # Create a new figure using Plotly's Figure object
    fig = go.Figure()

    # Add a trace for the data stream (regular data)
    fig.add_trace(go.Scatter(
        x=list(range(len(data_stream))),  # X-axis: index of each data point
        y=data_stream,                    # Y-axis: value of the data stream
        mode='lines',                     # Display the data as a line
        name='Data Stream'                # Name of this trace (for legend)
    ))

    # Add a trace for the anomaly scores
    fig.add_trace(go.Scatter(
        x=list(range(len(anomaly_scores))),  # X-axis: index of each data point
        y=anomaly_scores,                    # Y-axis: value of the anomaly score
        mode='lines',                        # Display the anomaly score as a line
        name='Anomaly Score',                # Name of this trace (for legend)
        line=dict(color='red')               # Set the line color for anomaly scores to red
    ))

    # Update the layout of the plot (titles, axis labels, and height)
    fig.update_layout(
        title="Anomaly Detection in Data Stream",  # Title of the plot
        xaxis_title="Index",                       # X-axis label
        yaxis_title="Value",                       # Y-axis label
        height=600                                # Height of the plot in pixels
    )

    # Save the plot as an HTML file and automatically open it in the default browser
    plot(fig, filename='anomaly_detection_plot.html', auto_open=True)
