import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pathlib
import argparse

sns.mpl.use("pgf")
sns.set(
    context="paper",
    rc={
        "axes.grid": True,
        "axes.titlepad": 4,
        "axes.labelpad": 2,
        "axes.labelsize": "medium",
        "font.size": 8,
        "font.family": "serif",
        # "font.family": "sans-serif",
        "font.serif": "cmr10",
        "font.sans-serif": "Hiragino Sans",
        "grid.alpha": 0.8,
        "grid.linestyle": "--",
        "grid.linewidth": 0.5,
        "legend.fontsize": "x-small",
        "legend.frameon": True,
        "legend.framealpha": 0.8,
        "legend.title_fontsize": "x-small",
        "legend.handlelength": 1.5,
        "legend.columnspacing": 0.5,
        "lines.linewidth": 0.75,
        "lines.markersize": 1,
        "pdf.fonttype": 42,
        "savefig.pad_inches": 0.05,
        "savefig.transparent": True,
        "text.usetex": True,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.labelsize": "x-small",
        "ytick.labelsize": "x-small",
    },
    style="ticks",
)
sns.set_palette("tab10")

# この2個だけはrcParamsで指定してもseaborn内で上書きされる
plot_kws = {
    "mec": None,
}

# figure size
mm = 1 / 25.4  # inch to mm
aspect = 1.6
fig_w = 50 * mm
fig_h = fig_w / aspect


parser = argparse.ArgumentParser(prog="PlotSDR", description="Plot segmental SI-SDR improvements.")
parser.add_argument("csvpath")
args = parser.parse_args()
csvpath = pathlib.Path(args.csvpath)
df = pd.read_csv(csvpath, index_col=False)
drop = [
    "bss.ref_mic",
    "bss.n_iter",
    "bss.demix_update",
    "SDR_est",
    "SDR_mix",
]

df.drop(columns=drop, inplace=True)

by = [
    "frame",
    "channel",
    "process",
    "bss.source_model",
    "bss.f_limit",
    "bss.forget",
    "fft.len",
]

group = df.groupby(by=by, as_index=False).mean().reset_index()

# rename
new_cols = {
    "frame": "Time (s)",
    "bss.source_model": "Source model",
    "bss.f_limit": "Frequency band limitation",
    "SDR_imp": "SI-SDRi (dB)",
    "bss.forget": "Forgetting factor",
}
group.rename(columns=new_cols, errors="raise", inplace=True)
print(group)

# replace
methods = {
    "online-rot": "SFIIVA-M",
    "online-sfi": "SFIIVA-O",
    "online-reset": "Reset",
    "online": "Naive",
}
group.replace(methods, inplace=True)
print(group)

print(group[new_cols["bss.forget"]].unique())
for fftlen in group["fft.len"].unique():
    for alpha in group[new_cols["bss.forget"]].unique():
        for model in group[new_cols["bss.source_model"]].unique():
            for freq in group[new_cols["bss.f_limit"]].unique():
                print(model, freq, alpha)
                queries = [
                    f"`{new_cols['bss.forget']}` == {alpha}",
                    f"`{new_cols['bss.source_model']}` == '{model}'",
                    f"`{new_cols['bss.f_limit']}` == {freq}",
                ]
                d = group.query(" and ".join(queries))
                grid = sns.relplot(
                    data=d,
                    x=new_cols["frame"],
                    y=new_cols["SDR_imp"],
                    # row="channel",
                    hue="process",
                    hue_order=list(methods.values()),
                    style="process",
                    markers=True,
                    dashes=False,
                    kind="line",
                    errorbar=None,
                    height=fig_h,
                    aspect=aspect,
                    facet_kws={"legend_out": True, "despine": False, "xlim": (0, 60), "ylim": (-15, 25)},
                    **plot_kws,
                )

                # remove title in legend
                grid.fig.legends[0].remove()
                handles, labels = grid.ax.get_legend_handles_labels()
                grid.fig.axes[0].legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 1), ncol=4)

                # adjust
                grid.fig.axes[0].axvline(x=30, color="k", linewidth=0.75, linestyle="--")
                grid.fig.tight_layout()  # (left, bottom, right, top)
                grid.fig.subplots_adjust(**dict(left=0.15, bottom=0.20, right=0.85, top=0.85))

                alpha_fmt = f"{alpha:.3f}"[2:]
                grid.fig.savefig(csvpath.parent / f"{model}_{freq}_fft{fftlen}_{alpha_fmt}.pdf")
                plt.clf()
                plt.close()
