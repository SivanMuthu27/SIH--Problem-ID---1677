import plotly.graph_objects as go

def visualize_results(query, contexts, response):
    fig = go.Figure()

    # Add query text
    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        text=[f"Query: {query}"],
        mode='text',
        textfont=dict(size=16),
        showlegend=False
    ))

    # Add retrieved contexts
    for i, context in enumerate(contexts):
        fig.add_trace(go.Scatter(
            x=[0], y=[-i-1],
            text=[f"Context {i+1}: {context}"],
            mode='text',
            textfont=dict(size=14),
            showlegend=False
        ))

    # Add RAG response
    fig.add_trace(go.Scatter(
        x=[0], y=[-len(contexts)-1],
        text=[f"RAG Response: {response}"],
        mode='text',
        textfont=dict(size=16, color='red'),
        showlegend=False
    ))

    fig.update_layout(
        title="Query and Results Visualization",
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False, autorange='reversed'),
        showlegend=False
    )

    fig.show()
