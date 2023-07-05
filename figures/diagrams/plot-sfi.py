import matplotlib.patches as pat
import matplotlib.pyplot as plt
import numpy as np
import pyroomacoustics as pra
import seaborn as sns
from matplotlib.collections import LineCollection

mm = 1 / 25.4
fig_w = 120 * mm
aspect = 3.2
box_aspect = 1 / 1.6
fig_h = fig_w / aspect
sns.set_theme(
    style="white",
    rc={
        # "axes.spines.bottom": False,
        # "axes.spines.top": False,
        # "axes.spines.left": False,
        # "axes.spines.right": False,
        "font.sans-serif": "Helvetica",
        "font.size": 8,
        "figure.figsize": (fig_w, fig_h),
        "lines.markersize": 4,
        "axes.linewidth": 1.0,
        "image.cmap": "coolwarm",
    },
)

# microphone array
n_mic = 6
mic_r = 0.02
mic_rot = 17
dx = 2 * mic_r * np.sin(np.pi / n_mic)

# pysical parameters
amp = 1
c = 340
freq = c / (2 * dx)  # Nyquist frequency in spatial domain
omega = 2 * np.pi * freq
kx = 1
ky = kx * np.tan(np.deg2rad(mic_rot))
k = omega / c * np.array([kx, ky])

n_mesh = 1000
x = np.linspace(-mic_r * 1.3 / box_aspect, mic_r * 1.3 / box_aspect, n_mesh)
y = np.linspace(-mic_r * 1.3, mic_r * 1.3, n_mesh)
mic_deg = np.deg2rad(np.arange(0, 360))
mic_x = mic_r * np.cos(mic_deg)
mic_y = mic_r * np.sin(mic_deg)
xx, yy = np.meshgrid(x, y)
pos = np.einsum("i,i...->...", k, np.array([xx, yy]))

# position of microphone array
mic_locs1 = pra.beamforming.circular_2D_array([0, 0], M=n_mic, phi0=0, radius=mic_r)
mic_locs2 = pra.beamforming.circular_2D_array([0, 0], M=n_mic, phi0=np.deg2rad(mic_rot), radius=mic_r)


for n, t in enumerate(np.linspace(0, 1 / freq, 10)):
    # plot
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Sound pressure in continuous field
    A = amp * np.exp(1j) ** (omega * t - pos)
    ax1.pcolormesh(x, y, A.real, vmin=-1, vmax=1, rasterized=True, shading="auto", zorder=-2)

    # microphone array
    ax1.scatter(mic_locs1[0, :], mic_locs1[1, :], s=36, edgecolors="white", marker="o", linewidths=0.5, c="k")
    ax1.scatter(mic_locs2[0, :], mic_locs2[1, :], s=36, edgecolors="white", marker="X", linewidths=0.5, c="C7")
    ax1.add_patch(pat.Circle(xy=(0, 0), radius=mic_r, color="C7", fill=False, zorder=-1))
    ax1.set_title("CMA in continuous sound field", fontsize=8)
    ax1.tick_params(
        axis="both", which="both", bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=False
    )
    ax1.set_aspect("equal")
    ax1.set_box_aspect(box_aspect)

    # Sound pressure at microphone
    sc = amp * np.exp(1j) ** (omega * t - k @ np.array([mic_x, mic_y]))  # sound pressure at the first microphone array
    mic_x1 = np.arange(0, 360, 360 // n_mic)
    mic_x2 = np.arange(0, 360, 360 // n_mic) + mic_rot
    y1 = sc[mic_x1]
    y2 = sc[mic_x2]

    points = np.array([mic_deg, sc.real]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    norm = plt.Normalize(-1, 1)
    lc = LineCollection(segments, array=sc.real, linewidth=1.0, norm=norm)
    ax2.add_collection(lc)
    arrow = pat.FancyArrowPatch(
        posA=(0, 0),
        posB=(mic_deg[-1], 0),
        arrowstyle="->",
        linewidth=1,
        color="k",
        shrinkA=0,
        shrinkB=0,
        zorder=2,
        mutation_scale=8,
    )
    ax2.add_artist(arrow)

    # # without color
    # ax2.plot(mic_deg, np.real(sc), linestyle="-", color="k", linewidth=1)

    ml, sl, bl = ax2.stem(np.deg2rad(mic_x1), y1.real)
    ml.set(linewidth=0.5, color="k", marker="o", markeredgewidth=0.3, markeredgecolor="white")
    sl.set(linewidth=0.5, color="k", linestyle="--")
    bl.set(visible=False)

    ml, sl, bl = ax2.stem(np.deg2rad(mic_x2), y2.real)
    ml.set(linewidth=0.5, color="C7", marker="X", markeredgewidth=0.3, markeredgecolor="white")
    sl.set(linewidth=0.5, color="C7", linestyle="--")
    bl.set(visible=False)

    ax2.tick_params(
        axis="both", which="both", bottom=False, top=False, left=False, right=False, labelleft=False, labelbottom=False
    )
    ax2.set_title("Sound pressure on the circumference", fontsize=8)
    ax2.set_box_aspect(box_aspect)

    plt.subplots_adjust(top=0.90, bottom=0.02, left=0.05, right=0.95, wspace=0.50)

    con = pat.ConnectionPatch(
        xyA=(1.05, 0.2),
        xyB=(-0.05, 0.2),
        coordsA="axes fraction",
        coordsB="axes fraction",
        axesA=ax1,
        axesB=ax2,
        arrowstyle="-|>",
        mutation_scale=8,
        color="gray",
        lw=2,
        connectionstyle="arc3,rad=0.3",
    )
    ax1.add_artist(con)
    ax1.annotate("Discretization", xy=(0.5, 0.32), xycoords="figure fraction", ha="center", va="top")

    plt.savefig(f"sfi{n:02d}.pdf")
