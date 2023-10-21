## Recommendations

- Reviewer 1: Accept with minor revisions
- Reviewer 2: Accept with minor revisions

## Comments

### Reviewer: 1

This paper is generally well-written and addresses the important issue of tracking rapid changes in source location caused by head movements when a CMA is worn on the head.
Here are three suggestions for the authors to improve this paper.

1. The basic signal model in (1) does not consider any background noise, and neither does the simulation. From a practical point of view, background noise is inevitable. Therefore, it is essential to demonstrate the performance of the proposed algorithms under various noise conditions. Alternatively, please consider validating the proposed algorithms through real experiments.
2. Figure 6 is difficult to view, particularly when printed in greyscale. Another figure that supports your conclusion in a clearer manner may be beneficial.
3. The current simulation setup adopts the same number of sources and microphones. It presents a determined case in math. How about other combinations of K and M to demonstrate the under-determined and over-determined cases?

Furthermore, typos are noted in this paper.
For instance, in the third paragraph of the introduction, it should be "relation" instead of "realation."
Please review the paper carefully for such errors when revising.

## Reviewer: 2

The introduction provides a good review of the relevant literature.
It might be good to include a simple system diagram illustrating the key components of the proposed approach (e.g. similar to Figure 1 in [22]).

On Page 4, after mentioning that the rotation angle is assumed to be measured by a sensor it might be good to also mention an example (e.g. an angular acceleration sensor as mentioned later at the end of Section 3).

In Figure 3, (b) and (c) appear to be identical.
Please clarify if this is intended.
Please also clarify what the numbers refer to next to the square outlining the CMA i.e. 3.025, 3.000 and 2.975 in the vertical direction and the 3 numbers in the horizontal direction.

From results in Figures 4 and 5 it appears that the performance when using a forgetting factor of 0.9 are quite similar for each method.
Please clarify this and also if the error bars, which appear overlapping, represent confidence intervals or some other quantity.

In the first sentence of Section 5.4, it should perhaps say “SFIIVA-O and SFIIVA-M” rather than “SFIIVA-O and SFIIVA-O”.

In Figure 6 (c), it appears that results for Channel 4 might not be as good a other channels in that while there is a brighter region around 176 degrees other regions also appear relatively bright (e.g. between 248 and 320 degrees).
Please consider commenting on why this might be the case.

## Additional questions

### Reviewer 1

- Originality of the work: 4
- Quality of writing: 4
- Technical correctness: 5
- All key relevant references are included: 5
- The work is reproducible: 4
- The paper is a good fit for this journal: 5
- The work has potentially high impact: 4

### Reviewer 2

- Originality of the work: 4
  - Comments: The main novelty is the combination of two methods, a blind source separation (BSS) method with a sound field interpolation method to address the problem of BSS applied to Circular Microphone Array (CMA) recordings where the CMA might rotate during separation.
- Quality of writing: 4
  - Comments: Well written.
- Technical correctness: 5
  - Comments: This is technically correct.
- All key relevant references are included: 5
  - Comments: Key references are well covered.
- The work is reproducible: 4
  - Comments: Algorithms summarizing the implementation are provided in the paper and the experimental setup is clear.
- The paper is a good fit for this journal: 5
  - Comments: This is a good fit.
- The work has potentially high impact: 3
  - Comments: The work is an interesting contribution that provides some advantage over existing methods.
