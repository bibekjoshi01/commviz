import plotly.graph_objects as go


def plot_signal(
    t,
    x,
    title="Signal",
    discrete=False,
    color="blue",
):

    fig = go.Figure()

    if discrete:
        # Stem plot: markers + vertical lines
        for xi, ti in zip(x, t):
            fig.add_trace(
                go.Scatter(
                    x=[ti, ti],
                    y=[0, xi],
                    mode="lines+markers",
                    marker=dict(color=color, size=8),
                    line=dict(color=color, width=2),
                    showlegend=False,
                )
            )
    else:
        fig.add_trace(
            go.Scatter(
                x=t, y=x, mode="lines", name="Signal", line=dict(color=color, width=2)
            )
        )

    fig.update_layout(
        title=title,
        xaxis_title="Time",
        yaxis_title="Amplitude",
        template="plotly_white",
        height=400,
        margin=dict(l=10, r=10, t=40, b=40),  # small margin inside figure
        paper_bgcolor="white",  # plot background
        plot_bgcolor="white",  # plotting area background
        xaxis=dict(
            showline=True,
            linecolor="black",
            linewidth=1,
            showgrid=True,
            gridcolor="lightgray",
            gridwidth=1,
        ),
        yaxis=dict(
            showline=True,
            linecolor="black",
            linewidth=1,
            showgrid=True,
            gridcolor="lightgray",
            gridwidth=1,
        ),
    )

    return fig
