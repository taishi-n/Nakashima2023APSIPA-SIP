# Responses to Reviewers' Comments (SIP-2023-0063)

Authors: Taishi Nakashima, Yukoh Wakabayashi, and Nobutaka Ono
Date: 31 Oct. 2023

## Dear Editor and Reviewers:

Dear associate editor and reviewers,

Thank you very much for your constructive suggestions and valuable comments on our paper entitled "Self-Rotation-Robust Online-Independent Vector Analysis with Sound Field Interpolation on Circular Microphone Array" (SIP-2023-0063).
We have carefully revised the manuscript according to the comments.
Comments from reviewers are quoted with gray box like:

> This is an example for quotations of comments from reviewers.

We will provide a point-by-point reply that explains reviewers' comments.
For the reviewers' convenience, we have marked modified parts as red.
The notations and citations used in this letter are the same as in the revised manuscript.

## Responses to Reviewer 1

> 1. The basic signal model in (1) does not consider any background noise, and neither does the simulation. From a practical point of view, background noise is inevitable. Therefore, it is essential to demonstrate the performance of the proposed algorithms under various noise conditions. Alternatively, please consider validating the proposed algorithms through real experiments.

- 再実験を行う？

> 2. Figure 6 is difficult to view, particularly when printed in greyscale. Another figure that supports your conclusion in a clearer manner may be beneficial.

- 図が独特なのでもっともな指摘…
- 周波数ごとの指向特性も追加する？

> 3. The current simulation setup adopts the same number of sources and microphones. It presents a determined case in math. How about other combinations of K and M to demonstrate the under-determined and over-determined cases?

- 答えるのが難しい…
- Overdetermined の実験はやったことがあるが，同じ音源が違うチャネルに分けて分離されるなど評価が難しくなる
- Underdetermined の実験はやったことはないが，IVA ベースの音源分離なのでそもそも分離されなくなりそう

> Furthermore, typos are noted in this paper.
> For instance, in the third paragraph of the introduction, it should be "relation" instead of "realation."
> Please review the paper carefully for such errors when revising.

注意深くチェックした．
スペルチェックを通したし，再度英文校閲にも出す．

## Responses to Reviewer 2

> It might be good to include a simple system diagram illustrating the key components of the proposed approach (e.g. similar to Figure 1 in [22]).

提案に感謝する．
修正版の図 1 を新しく追加した．

> On Page 4, after mentioning that the rotation angle is assumed to be measured by a sensor it might be good to also mention an example (e.g. an angular acceleration sensor as mentioned later at the end of Section 3).

わかりにくい点を指摘してくれて感謝する．
該当箇所の文章を修正した．

> In Figure 3, (b) and (c) appear to be identical.
> Please clarify if this is intended.
> Please also clarify what the numbers refer to next to the square outlining the CMA i.e. 3.025, 3.000 and 2.975 in the vertical direction and the 3 numbers in the horizontal direction.

同じ図ではなく，マイクの位置が変わっている．
しかし，指摘通り紛らわしい図であるので，Figure 3 (b), (c) をひとつの図で表すことにした．
また，図中の 3.025, 3.000 などはマイクロホンアレイ中心の座標を表す数値であり，単位は m である．図に説明を追加した．

> From results in Figures 4 and 5 it appears that the performance when using a forgetting factor of 0.9 are quite similar for each method.
> Please clarify this and also if the error bars, which appear overlapping, represent confidence intervals or some other quantity.

0.95, 0.98 の結果と比べると，分離性能が
忘却係数が 0 に近いほど過去の影響をすぐ忘れるため，0.95, 0.98 など他の結果に比べてマイクアレイ回転に対する追従は早い．
しかし，その代わりに分離性能が低くなり，十分な時間が経過後も高い分離性能を得られないまま飽和している．
Figure 5 は標準的な箱ひげ図であるため，エラーバーは外れ値を除いた最大値・最小値を表している．

> In the first sentence of Section 5.4, it should perhaps say “SFIIVA-O and SFIIVA-M” rather than “SFIIVA-O and SFIIVA-O”.

提案に感謝する．
注意深く原稿をチェックし，typo を修正した．

> In Figure 6 (c), it appears that results for Channel 4 might not be as good a other channels in that while there is a brighter region around 176 degrees other regions also appear relatively bright (e.g. between 248 and 320 degrees).
> Please consider commenting on why this might be the case.

- 今回は音声信号のため，8000Hz 付近の高い周波数成分がなく，どこに null を向けてもよくなるため…？
