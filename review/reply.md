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

## General Comment

- Clearly に伝えるために提案法の名前変えました
  - `SFIIVA-O` -> `SFIIVA-Obs`
  - `SFIIVA-M` -> `SFIIVA-Par`
- それに合わせて図中の凡例変えました

<div style="page-break-after:always"></div>

## Responses to Reviewer 1

> 1. The basic signal model in (1) does not consider any background noise, and neither does the simulation.
>    From a practical point of view, background noise is inevitable.
>    Therefore, it is essential to demonstrate the performance of the proposed algorithms under various noise conditions.
>    Alternatively, please consider validating the proposed algorithms through real experiments.

Thank you for your constructive comments.
As pointed out, we acknowledge that it is important to show the results of experiments in noisy environments from a practical point of view.
Additional experiments were performed under the following conditions:

1. Experiments with extra interference noise.
2. Experiments with speech babble noise.

For detailed experimental conditions, results, and discussions, please see the new Subsection 5.5 in the revised edition.
As for experiments under real environments, due to time constraints, we decided to leave it for future work and have added to the conclusions of the revised manuscript.

> 2. Figure 6 is difficult to view, particularly when printed in greyscale.
>    Another figure that supports your conclusion in a clearer manner may be beneficial.

Thank you for your suggestion.
As shown below, we also made a modified example plot of a beam pattern with only a few frequencies, which is widely used in the context of beamforming, but we think it is rather difficult to view.
![ref](./fig/freq-limit/ref.png)
![rot-sfiiva-m](./fig/freq-limit/rot-sfiiva-m.png)
![rot-sfiiva-o](./fig/freq-limit/rot-sfiiva-o.png)
However, as you pointed out, authors agree that the color map makes it difficult to see.
Therefore, we kept the original plotting style, but changed the color map, and made some modifications such as the position of the color bar and the size of each plot.
![plasma-ref](./fig/ref.png)
![plasma-rot-sfiiva-o](./fig/rot_sfiiva-o.png)
![plasma-rot-sfiiva-m](./fig/rot_sfiiva-m.png)

> 3. The current simulation setup adopts the same number of sources and microphones.
>    It presents a determined case in math.
>    How about other combinations of $K$ and $M$ to demonstrate the under-determined and over-determined cases?

The purpose of this paper is to make BSS robust against self-rotation of microphone array.
As discussed in the famous independent component analysis or its extensions, the determined condition is the most basic and widely used in the context of BSS.
For over-determined or under-determined conditions, many methods have attributed them to the determined condition by imposing additional prior information or complex models.
Therefore, we believe that it is reasonable to start with the most basic determined condition.
However, it is a very useful point to consider those conditions in the future.
An explanation has been added to the conclusion with examples of BSS methods under over-determined or under-determined conditions.

> Furthermore, typos are noted in this paper.
> For instance, in the third paragraph of the introduction, it should be "relation" instead of "realation."
> Please review the paper carefully for such errors when revising.

Thank you for your suggestion.
We have carefully corrected that typo and other minor errors.
We also plan to have it professionally proofread by a native English speaker if the paper is accepted.

<div style="page-break-after:always"></div>

## Responses to Reviewer 2

> It might be good to include a simple system diagram illustrating the key components of the proposed approach (e.g. similar to Figure 1 in [22]).

Thank you for your recommendation.
We have added a new figure (Figure X in the revised manuscript).
And we have renamed our proposed methods for readability.

> On Page 4, after mentioning that the rotation angle is assumed to be measured by a sensor it might be good to also mention an example (e.g. an angular acceleration sensor as mentioned later at the end of Section 3).

Thank you for pointing out an unclear point.
We have added an example of the sentence at the end of the first paragraph in Section 2 (Page 4 in the revised manuscript).

> In Figure 3, (b) and (c) appear to be identical.
> Please clarify if this is intended.

The two figures (Figure 3 (b) and (c) in the first manuscript) showed the placement before and after the circular microphone array is rotated and are not identical.
As pointed out, however, we acknowledge that the two figures are confusing.
We have removed the two figures and added a new figure (Figure 4 (b) in the revised manuscript) to show the rotation more clearly.

> Please also clarify what the numbers refer to next to the square outlining the CMA i.e. 3.025, 3.000 and 2.975 in the vertical direction and the 3 numbers in the horizontal direction.

The numbers in the figure represent the coordinates of the center of the circular microphone array in meters.
However, because we felt that this would complicate the figure and hinder understanding, we removed the numbers from the figure.
Instead, we added their explanation in the caption of Figure 4(b).

> From results in Figures 4 and 5 it appears that the performance when using a forgetting factor of 0.9 are quite similar for each method.

Thank you for your helpful comment.
In online AuxIVA, setting the forgetting factor $\alpha$ to smaller value is equivalent to reducing the contribution of past data.
This results in faster convergence and tracking of the microphone array rotation but tends to limit the separation performance.
The result with a forgetting factor $\alpha$ of 0.9 clearly demonstrates that tendency.
We believe that each method performs similarly in this case because the separation performance of all methods is immediately saturated.
We have added an explanation for that in Section 5.2 (Page 15 in the revised manuscript).

> Please clarify this and also if the error bars, which appear overlapping, represent confidence intervals or some other quantity.

The bars represent the maximum and minimum values excluding outliers since Figure 5 is a well-known box-and-whisker diagram.
We have added an explanation for that to the figure caption in the revised manuscript.

> In the first sentence of Section 5.4, it should perhaps say “SFIIVA-O and SFIIVA-M” rather than “SFIIVA-O and SFIIVA-O”.

Thank you for your correction.
We have carefully corrected that.

> In Figure 6 (c), it appears that results for Channel 4 might not be as good a other channels in that while there is a brighter region around 176 degrees other regions also appear relatively bright (e.g. between 248 and 320 degrees).
> Please consider commenting on why this might be the case.

Thank you for your insightful comment.
Online AuxIVA is equivalent to adaptively estimating the nulls that suppresses interference sources in each frequency.
In this experiment, speech signal was used as the source signal, so the frequency components around 8000 Hz were not included.
We believe that the direction of the non-interference source was incorrectly estimated only in the frequency band that did not include speech as a result.
These explanations have been added to the experimental results.
