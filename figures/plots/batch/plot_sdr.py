import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.mpl.use("pgf")
sns.set(
    context="paper",
    rc={
        "axes.grid": True,
        "axes.titlepad": 4,
        "axes.labelpad": 2,
        # "font.size": 9,
        "font.family": "serif",
        "font.serif": "cmr10",
        # "font.sans-serif": "Noto Sans JP",
        "grid.alpha": 0.8,
        "grid.linestyle": "--",
        "grid.linewidth": 0.5,
        "legend.fontsize": "x-small",
        "legend.frameon": True,
        "legend.framealpha": 0.9,
        "legend.title_fontsize": "small",
        "lines.linewidth": 0.8,
        "lines.markersize": 2,
        "pdf.fonttype": 42,
        "savefig.pad_inches": 0.05,
        "savefig.transparent": True,
        "text.usetex": True,
        "xtick.direction": "in",
        "ytick.direction": "in",
    },
    style="ticks",
)
sns.set_palette("tab10")

# この2個だけはrcParamsで指定してもseaborn内で上書きされる
plot_kws = {
    # "mew": 0.0,
    "mec": None,
}

# figure size
mm = 1 / 25.4  # inch to mm
aspect = 1.8
fig_w = 72 * mm
fig_h = fig_w / aspect


df = pd.read_csv("bsseval_all.csv", index_col=False)
drop = [
    "fft.win",
    "bss.ref_mic",
    "bss.n_iter",
    "bss.forget",
    "fft.len",
    "fft.hop",
    "process",
    "bss.demix_update",
    "SDR_est",
    "SDR_mix",
]
df.drop(columns=drop, inplace=True)

by = [
    "frame",
    "channel",
    "bss.source_model",
    "bss.f_limit",
    "mixdir_name",
]

group = df.groupby(by=by, as_index=False).mean().reset_index()

# rename
new_cols = {
    "frame": "Time (s)",
    "bss.source_model": "Source model",
    "bss.f_limit": "Frequency band limitation",
    "mixdir_name": "SFI",
    "SDR_imp": "SI-SDRi (dB)",
}
group.rename(columns=new_cols, errors="raise", inplace=True)

# post select
group.query(f"`{new_cols['bss.f_limit']}` == 8000", inplace=True)

# replace
group.replace({"int": True, "rot-mix": False}, inplace=True)

for model in group[new_cols["bss.source_model"]].unique():
    for freq in group[new_cols["bss.f_limit"]].unique():
        print(model, freq)
        queries = [
            f"`Source model` == '{model}'",
            f"`{new_cols['bss.f_limit']}` == {freq}",
        ]
        d = group.query(" and ".join(queries))
        grid = sns.relplot(
            data=d,
            x=new_cols["frame"],
            y=new_cols["SDR_imp"],
            hue=new_cols["mixdir_name"],
            hue_order=[True, False],
            style=new_cols["mixdir_name"],
            style_order=[True, False],
            markers=True,
            dashes=False,
            kind="line",
            ci=None,
            height=fig_h,
            aspect=aspect,
            facet_kws={"legend_out": False, "despine": False, "xlim": (0, 40)},
            **plot_kws,
        )

        # adjust
        grid.fig.axes[0].axvline(x=10, color="k", linewidth=.75, linestyle="--")
        grid.fig.axes[0].axvline(x=25, color="k", linewidth=.75, linestyle="--")
        grid.fig.tight_layout()  # (left, bottom, right, top)
        grid.fig.subplots_adjust(**dict(left=0.18, bottom=0.20, right=0.97, top=0.97))

        grid.fig.savefig(f"{model}_{freq}.pdf")
        plt.clf()
        plt.close()
