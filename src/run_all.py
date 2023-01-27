""" Run the model. """

import os
import pandas as pd
import numpy as np
from analysis import run_analysis
from plot import plot_irf

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
bld_dir = "bld"
bld_path = os.path.join(parent_dir, bld_dir)
src_dir = "src"
src_path = os.path.join(parent_dir, src_dir)

if not os.path.exists(bld_path):
    os.mkdir(bld_path)

mod_ilt = os.path.join(src_path, "model_ILT.yaml")
mod_plt = os.path.join(src_path, "model_PLT.yaml")
shock_size = 0.05

data = run_analysis(mod_ilt, mod_plt, shock_size)

data.to_csv(os.path.join(bld_path, "model.csv"))

varlist_ilt = ["c_ilt", "n_ilt", "pi_ilt", "w_ilt", "R_ilt", "y_ilt", "i_ilt", "piw_ilt", "b_ilt"]
varlist_plt = ["c_plt", "n_plt", "pi_plt", "w_plt", "R_plt", "y_plt", "i_plt" , "piw_plt", "b_plt"]

data_ilt=data[varlist_ilt]
data_plt=data[varlist_plt]

steady_states_ilt = data_ilt[:1]
steady_states_plt = data_plt[:1]

ss_dev_ilt=100*((np.array(data_ilt)-np.array(steady_states_ilt))/np.array(steady_states_ilt))
ss_dev_plt=100*((np.array(data_plt)-np.array(steady_states_plt))/np.array(steady_states_plt))

data_ss = np.column_stack([ss_dev_ilt, ss_dev_plt])
data_ss = pd.DataFrame(data_ss)
data_ss.columns = varlist_ilt + varlist_plt

periods = 40
data_plot = data_ss.head(periods)
x_plot = range(periods)

fig_y = plot_irf(data=data_plot, x=x_plot, var1="y_ilt", var2="y_plt", title ="Output")
fig_pi = plot_irf(data=data_plot, x=x_plot, var1="pi_ilt", var2="pi_plt", title="Price Inflation")
fig_c = plot_irf(data=data_plot, x=x_plot, var1="c_ilt",var2="c_plt", title="Consumption")
fig_i = plot_irf(data=data_plot, x=x_plot, var1="i_ilt", var2="i_plt", title="Investment")
fig_n = plot_irf(data=data_plot, x=x_plot, var1="n_ilt", var2="n_plt", title="Labor")
fig_w = plot_irf(data=data_plot, x=x_plot, var1="w_ilt", var2="w_plt", title="Wage")
fig_piw = plot_irf(data=data_plot, x=x_plot, var1="piw_ilt", var2="piw_plt", title="Wage Inflation")
fig_r = plot_irf(data=data_plot, x=x_plot, var1="R_ilt", var2="R_plt", title="Interest Rate")
fig_b = plot_irf(data=data_plot, x=x_plot, var1="b_ilt", var2="b_plt", title="Bonds")

###
fig_y.write_image(os.path.join(bld_path, "irf_y.pdf"))
fig_pi.write_image(os.path.join(bld_path,  "irf_pi.pdf"))
fig_c.write_image(os.path.join(bld_path,  "irf_c.pdf"))
fig_i.write_image(os.path.join(bld_path, "irf_i.pdf"))
fig_n.write_image(os.path.join(bld_path, "irf_n.pdf"))
fig_w.write_image(os.path.join(bld_path, "irf_w.pdf"))
fig_b.write_image(os.path.join(bld_path, "irf_b.pdf"))
fig_piw.write_image(os.path.join(bld_path, "irf_piw.pdf"))
fig_r.write_image(os.path.join(bld_path, "irf_r.pdf"))
