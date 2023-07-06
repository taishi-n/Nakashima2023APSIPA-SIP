import matplotlib.patches as pat
import matplotlib.pyplot as plt
import numpy as np
import pyroomacoustics as pra
import seaborn as sns
from matplotlib.collections import LineCollection
from matplotlib.patheffects import withStroke


def calc_rotation_matrix(n_mic: int, deg: float):
    """
    マイクが円状に等間隔に配置されたマイクロホンアレイの回転行列
    フーリエ変換の和の範囲を (-M/2 + 1, ..., M/2) ではなく，
    (0, ..., M-1) で計算したバージョン

    Parameters
    ----------
    n_mic: int
        マイク数
    deg: float
        回転角度

    Returns
    -------
    U: ndarray (n_mic, n_mic)
        回転行列
    """
    x = np.linspace(0, n_mic - 1, n_mic)
    y = np.linspace(0, n_mic - 1, n_mic)
    i, j = np.meshgrid(x, y)
    delay = np.deg2rad(deg) * n_mic / (2 * np.pi)
    L = delay - j + i

    W = np.exp(2j * np.pi / n_mic)
    U = (W ** (-L * np.ceil((n_mic - 1) / 2))) * (W ** (L * (n_mic - 1) / 2)) * np.sinc(L) / np.sinc(L / n_mic)
    return U


mm = 1 / 25.4
fig_w = 120 * mm
aspect = 3.2
box_aspect = 1 / 1.6
fig_h = fig_w / aspect
sns.set_theme(
    style="white",
    rc={
        "axes.linewidth": 1.0,
        "axes.titlesize": "medium",
        "font.sans-serif": "Helvetica",
        "font.size": 8,
        "figure.figsize": (fig_w, fig_h),
        "lines.markersize": 4,
        "image.cmap": "coolwarm",
        "text.usetex": True,
    },
)

color_ref = "black"
color_rot = "0.6"
color_sfi = "yellow"

# microphone array
n_mic = 6
mic_r = 0.02
mic_rot = 17.89
dx = 2 * mic_r * np.sin(np.pi / n_mic)

# pysical parameters
complex_plane_wave_2d = lambda amp, omega, t, pos: amp * np.exp(1j * (omega * t - pos))
amp = 1
c = 340
freq = c / (2 * dx)  # Nyquist frequency in spatial domain
freq = 8000
omega = 2 * np.pi * freq
kx = 1
ky = kx * np.tan(np.deg2rad(mic_rot))
k = omega / c * np.array([kx, ky])

n_mesh = 2000
xy_zoom = 1.5
x = np.linspace(-mic_r * xy_zoom / box_aspect, mic_r * xy_zoom / box_aspect, n_mesh)
y = np.linspace(-mic_r * xy_zoom, mic_r * xy_zoom, n_mesh)
xx, yy = np.meshgrid(x, y)
pos = np.einsum("i,i...->...", k, np.array([xx, yy]))

# continuous microphone coodinates
n_mesh_deg = 1000
deg = np.deg2rad(np.linspace(0, 360, n_mesh_deg))
mic_x = mic_r * np.cos(deg)
mic_y = mic_r * np.sin(deg)
mic_pos_c = k @ np.array([mic_x, mic_y])

# discrete microphone coodinates
mic_deg_ref = np.deg2rad(np.linspace(0, 360, n_mic, endpoint=False))
mic_deg_rot = np.deg2rad((np.linspace(0, 360, n_mic, endpoint=False) + mic_rot) % 360)

mic_x_ref = mic_r * np.cos(mic_deg_ref)
mic_x_rot = mic_r * np.cos(mic_deg_rot)

mic_y_ref = mic_r * np.sin(mic_deg_ref)
mic_y_rot = mic_r * np.sin(mic_deg_rot)

mic_pos_ref = k @ np.array([mic_x_ref, mic_y_ref])
mic_pos_rot = k @ np.array([mic_x_rot, mic_y_rot])


# position of microphone array
mic_locs1 = pra.beamforming.circular_2D_array([0, 0], M=n_mic, phi0=0, radius=mic_r)
mic_locs2 = pra.beamforming.circular_2D_array([0, 0], M=n_mic, phi0=np.deg2rad(mic_rot), radius=mic_r)
mic_locs_txt = pra.beamforming.circular_2D_array([0, 0], M=n_mic, phi0=0, radius=0.9 * xy_zoom * mic_r)


n_freq = 20
for n, t in enumerate(np.linspace(0, 1 / freq, n_freq)):
    # plot
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Sound pressure in continuous field
    A = complex_plane_wave_2d(amp, omega, t, pos).real
    ax1.pcolormesh(x, y, A, vmin=-1, vmax=1, rasterized=True, shading="auto", zorder=-3)

    # microphone array
    ax1.scatter(mic_locs1[0, :], mic_locs1[1, :], s=25, ec="white", marker="o", lw=0.5, color=color_ref)
    ax1.scatter(mic_locs2[0, :], mic_locs2[1, :], s=25, ec="white", marker="o", lw=0.5, color=color_rot)

    ax1.annotate(
        "",
        xytext=np.mean(mic_locs1, axis=1),
        xy=mic_locs2[:, 0],
        ha="center",
        va="bottom",
        arrowprops=dict(arrowstyle="->", color="white", lw=0.5),
    )
    ax1.annotate(
        "",
        xytext=np.mean(mic_locs1, axis=1),
        xy=mic_locs1[:, 0],
        ha="center",
        va="bottom",
        arrowprops=dict(arrowstyle="-", ls="dashed", color="white", lw=0.5),
        zorder=-1,
    )
    ax1.text(
        s=r"$\theta$",
        x=0.5 * mic_locs2[0, 0],
        y=0.5 * mic_locs2[1, 0],
        va="bottom",
        ha="center",
        fontsize="large",
        path_effects=[withStroke(linewidth=1.0, foreground="white")],
    )
    for i, p in enumerate(mic_locs_txt.T):
        ax1.text(
            s=fr"$x_{i}$",
            x=p[0],
            y=p[1],
            va="center",
            ha="center",
            fontsize="large",
            path_effects=[withStroke(linewidth=1.0, foreground="white")],
        )
    ax1.add_patch(pat.Circle(xy=(0, 0), radius=mic_r, ls="--", lw=0.5, fill=False, zorder=-1))
    ax1.set_title("CMA in continuous sound field")
    ax1.tick_params(
        axis="both", which="both", bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=False
    )
    ax1.set_aspect("equal")
    ax1.set_box_aspect(box_aspect)

    # Sound pressure at microphone
    yc = complex_plane_wave_2d(amp, omega, t, mic_pos_c).real  # sound pressure in continuous field
    y_ref = complex_plane_wave_2d(amp, omega, t, mic_pos_ref).real  # sound pressure in continuous field
    y_rot = complex_plane_wave_2d(amp, omega, t, mic_pos_rot).real
    U = calc_rotation_matrix(n_mic, mic_rot)
    sc_sfi = (U @ y_rot).real

    points = np.array([deg, yc]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    norm = plt.Normalize(-1, 1)
    lc = LineCollection(segments, array=yc, linewidth=1.0, norm=norm)
    ax2.add_collection(lc)
    arrow = pat.FancyArrowPatch(
        posA=(-0.2, 0),
        posB=(deg[-1] + 0.2, 0),
        arrowstyle="-|>",
        linewidth=0.5,
        color="k",
        shrinkA=0,
        shrinkB=0,
        zorder=-1,
        mutation_scale=8,
    )
    ax2.add_artist(arrow)
    ax2.annotate(r"$\phi$", xy=(deg[-1], 0.10), xycoords="data", ha="center", va="bottom")

    ml, sl, bl = ax2.stem(mic_deg_ref, y_ref)
    ml.set(linewidth=0.5, color=color_ref, marker="o", markeredgewidth=0.3, markeredgecolor="white")
    sl.set(linewidth=0.5, color=color_ref, linestyle="--")
    bl.set(visible=False)

    ml, sl, bl = ax2.stem(mic_deg_rot, y_rot)
    ml.set(linewidth=0.5, color=color_rot, marker="o", markeredgewidth=0.3, markeredgecolor="white")
    sl.set(linewidth=0.5, color=color_rot, linestyle="--")
    bl.set(visible=False)

    # # Result of sound field interpolation
    # ml, sl, bl = ax2.stem(mic_deg_ref, sc_sfi)
    # ml.set(linewidth=0.5, color=color_sfi, marker="X", markeredgewidth=0.3, markeredgecolor="white")
    # sl.set(linewidth=0.5, color=color_sfi, linestyle="--")
    # bl.set(visible=False)

    ax2.tick_params(
        axis="both", which="both", bottom=False, top=False, left=False, right=False, labelleft=False, labelbottom=False
    )
    ax2.set_title("Sound pressure on the circumference")
    ax2.set_box_aspect(box_aspect)

    plt.subplots_adjust(top=0.90, bottom=0.02, left=0.05, right=0.95, wspace=0.50)

    con = pat.ConnectionPatch(
        xyA=(1, 0.2),
        xyB=(0, 0.2),
        coordsA="axes fraction",
        coordsB="axes fraction",
        axesA=ax1,
        axesB=ax2,
        shrinkA=5,
        shrinkB=5,
        arrowstyle="->",
        mutation_scale=10,
        color="gray",
        lw=0.8,
        connectionstyle="arc3,rad=0.3",
    )
    ax1.add_artist(con)
    ax1.annotate("Discretization", xy=(0.5, 0.32), xycoords="figure fraction", ha="center", va="top")

    plt.savefig(f"sfi{n:02d}.pdf")
    plt.close()
