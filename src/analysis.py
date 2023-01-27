""" Run the model. """

import econpizza as ep
import numpy as np
import pandas as pd

def run_analysis(mod_ilt, mod_plt, shock_size):
    """ This function runs the model and saves the data.
        
        Args: 
            mod_ilt: Path for the yaml file with ILT.
            mod_plt: Path for the yaml file with PLT.
            shock_size (float): Size of the shock.

        Returns (csv): dataframe

    """

    # Load yaml-files
    mod_ilt = mod_ilt
    mod_plt = mod_plt

    # use the model and solve for steady states
    mod_ilt = ep.load(mod_ilt)
    _ = mod_ilt.solve_stst()
    mod_plt = ep.load(mod_plt)
    _ = mod_plt.solve_stst()

    # risk premium shock
    shock = ("e_rp", shock_size)

    # use the stacking method
    x_ilt, flag_ilt = mod_ilt.find_path(shock=shock)
    x_plt, flag_plt = mod_plt.find_path(shock=shock)

    # combine data and save it in a DataFrame
    data = np.column_stack([x_ilt, x_plt])
    data = pd.DataFrame(data)
    data.columns = [var + "_ilt" for var in mod_ilt['variables']] + [var + "_plt" for var in mod_plt['variables']]

    return data