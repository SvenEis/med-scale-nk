""" Functions for plots.
"""

import plotly.express as px


def plot_irf(data,x,var1,var2, title):
    """ Plot the Impulse Response Functions.
    	Args:
		    data: pd.DataFrame with the data for IRFs.
		    x: variable for x-axis 
		    y: variable for x-axis 
		    title (str): title of plot.
		    yaxis_title (str): title of y-axis.
	
        Returns:
		    fig: Returns figure
    """
    fig = px.line(data,x=x,y=[var1,var2])
    fig.update_layout(
        title="",  # Empty title
        xaxis_title="Quarters",  # x-axis labeling
        yaxis_title="Proportional Deviation from the steady state (in %)",  # y-axis labeling
        legend=dict(  # For horizontal legend
            orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
        ),
        legend_title_text=title,
        plot_bgcolor="whitesmoke",
    )
    newnames = {var1:'ILT', var2: 'PLT'}
    fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )
    return fig