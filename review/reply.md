---
title: Responses to Reviewers' Comments (SIP-2023-0063)
author: Taishi Nakashima, Yukoh Wakabayashi, and Nobutaka Ono
creator: Taishi Nakashima
subject: Reply letter
---

## Responses to Reviewers' Comments (SIP-2023-0063)

Dear Associate Editor and Reviewers,

Thank you very much for your constructive suggestions and valuable comments on our paper entitled "Self-Rotation-Robust Online-Independent Vector Analysis with Sound Field Interpolation on Circular Microphone Array" `(SIP-2023-0063)`.
We have carefully revised the manuscript according to the comments.
Comments from reviewers are quoted with gray box like:

> This is an example for quotations of comments from reviewers.

We will provide a point-by-point reply that explains reviewers' comments.
For the reviewers' convenience, we have marked modified parts as red.
The notations and citations used in this letter are the same as in the revised manuscript.

## Responses to Reviewer 1

> 1. The basic signal model in (1) does not consider any background noise, and neither does the simulation.
>    From a practical point of view, background noise is inevitable.
>    Therefore, it is essential to demonstrate the performance of the proposed algorithms under various noise conditions.
>    Alternatively, please consider validating the proposed algorithms through real experiments.

- **要相談**
  - 実環境実験は時間的に難しい…
  - ノイズありシミュレーションを行ったとしても分離性能が全体的に下がるだけになりそう…
- 反論案:
  - 論文中のモデルは音源分離の文脈で広く用いられている標準的ものである
  - ノイズを付加したシミュレーション実験および実環境実験は今後検討する

> 2. Figure 6 is difficult to view, particularly when printed in greyscale.
>    Another figure that supports your conclusion in a clearer manner may be beneficial.

- **要相談**
  - 図が独特なのでもっともな指摘…
  - 現状の全周波数を同径方向にプロットしたものではなく，ビームフォーマの論文でよく見かける，1000Hz, 2000Hz, 4000Hz...などの指向特性を追加する？

> 3. The current simulation setup adopts the same number of sources and microphones.
>    It presents a determined case in math.
>    How about other combinations of $K$ and $M$ to demonstrate the under-determined and over-determined cases?

- **要相談**
  - 答えるのが難しい…
  - Overdetermined の実験はやったことがあるが，同じ音源が違うチャネルに分けて分離されるなど評価がかなり難しくなる
  - Underdetermined の実験はやったことはないが，IVA ベースの音源分離なのでそもそも分離されなくなりそう

> Furthermore, typos are noted in this paper.
> For instance, in the third paragraph of the introduction, it should be "relation" instead of "realation."
> Please review the paper carefully for such errors when revising.

Thank you for your suggestion.
We have carefully corrected that typo and other minor errors.

<div style="page-break-after:always"></div>

## Responses to Reviewer 2

> It might be good to include a simple system diagram illustrating the key components of the proposed approach (e.g. similar to Figure 1 in [22]).

Thank you for your recommendation.
We have added a new figure (Figure 1 in the revised manuscript).

> On Page 4, after mentioning that the rotation angle is assumed to be measured by a sensor it might be good to also mention an example (e.g. an angular acceleration sensor as mentioned later at the end of Section 3).

Thank you for pointing out an unclear point.
We have added an example of the sentence at the end of the first paragraph in Section 2.

> In Figure 3, (b) and (c) appear to be identical.
> Please clarify if this is intended.

The figure was not the same, but rather two separate drawings to show the rotation of the microphones.
We acknowledge that the two figures are confusing as pointed out.
Figure 3 (b) in the revised manuscript has been combined into one figure.

> Please also clarify what the numbers refer to next to the square outlining the CMA i.e. 3.025, 3.000 and 2.975 in the vertical direction and the 3 numbers in the horizontal direction.

The numbers in the figure are used to represent the coordinates of the center of the microphone array in metre.
An explanation for that has been added to the caption of Figure 3 in the revised manuscript.

> From results in Figures 4 and 5 it appears that the performance when using a forgetting factor of 0.9 are quite similar for each method.

Thank you for your helpful comment.
We have added an explanation for that in Section 5.2.

> Please clarify this and also if the error bars, which appear overlapping, represent confidence intervals or some other quantity.

The bars represent the maximum and minimum values excluding outliers since Figure 5 is a well-known box-and-whisker diagram.
We have added an explanation for that to the figure caption in the revised manuscript.

> In the first sentence of Section 5.4, it should perhaps say “SFIIVA-O and SFIIVA-M” rather than “SFIIVA-O and SFIIVA-O”.

Thank you for your correction.
We have carefully corrected that.

> In Figure 6 (c), it appears that results for Channel 4 might not be as good a other channels in that while there is a brighter region around 176 degrees other regions also appear relatively bright (e.g. between 248 and 320 degrees).
> Please consider commenting on why this might be the case.

- **考え中**
  - 今回は音声信号のため 8000Hz 付近の高い周波数成分がなく，どこに null を向けてもよくなるため…？
