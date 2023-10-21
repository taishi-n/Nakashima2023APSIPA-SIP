18-Oct-2023

Dear Mr. Nakashima,

SIP-2023-0063 entitled "Self-Rotation-Robust Online-Independent Vector Analysis with Sound Field Interpolation on Circular Microphone Array" which you submitted to the APSIPA Transactions on Signal and Information Processing, has been reviewed. The comments of the Associate Editor and reviewer(s) are included at the bottom of this letter.

The reviewer(s) have recommended publication, but also suggest some minor revisions to your manuscript. Therefore, I invite you to respond to the reviewer(s)' comments and revise your manuscript.

To revise your manuscript, log into https://mc.manuscriptcentral.com/apsipa and enter your Author Center, where you will find your manuscript under "Manuscripts with Decisions." Under "Actions," click on "Create a Revision." Your manuscript number will be appended to denote a revision. You may also click this link to start your revision:

**_ PLEASE NOTE: This is a two-step process. After clicking on the link, you will be directed to a webpage to confirm. _**

https://mc.manuscriptcentral.com/apsipa?URL_MASK=adf1814f443f4cc291ab7a865ef041d6

When submitting your revised manuscript, you will be able to respond to the comments made by the reviewer(s) in the space provided. Please use this space to document any changes you make to the original manuscript. In order to expedite the processing of the revised manuscript, please be as specific as possible in your response to the reviewer(s).

Because we are trying to facilitate timely publication of manuscripts submitted to the APSIPA Transactions on Signal and Information Processing, your revised manuscript should be uploaded as soon as possible. We expect to receive your revision by 01-Nov-2023. If it is not possible for you to submit your revision by this date, please contact the Editorial Office to rearrange the due date. Otherwise, we may have to consider your paper as a new submission.

Once again, thank you for submitting your manuscript to the APSIPA Transactions on Signal and Information Processing and I look forward to receiving your revision.

Sincerely,

Prof. C.-C. Jay Kuo
Editor-in-Chief, APSIPA Transactions on Signal and Information Processing
cckuo@sipi.usc.edu

Associate Editor's Comments to Author:

Associate Editor: Gan, Woon Seng
Comments to the Author:
(There are no comments.)

Reviewer(s)' Comments to Author:

Reviewer: 1

Recommendation: Accept with minor revisions

Comments:
This paper is generally well-written and addresses the important issue of tracking rapid changes in source location caused by head movements when a CMA is worn on the head. Here are three suggestions for the authors to improve this paper.

1. The basic signal model in (1) does not consider any background noise, and neither does the simulation. From a practical point of view, background noise is inevitable. Therefore, it is essential to demonstrate the performance of the proposed algorithms under various noise conditions. Alternatively, please consider validating the proposed algorithms through real experiments.

2. Figure 6 is difficult to view, particularly when printed in greyscale. Another figure that supports your conclusion in a clearer manner may be beneficial.

3. The current simulation setup adopts the same number of sources and microphones. It presents a determined case in math. How about other combinations of K and M to demonstrate the under-determined and over-determined cases?

Furthermore, typos are noted in this paper. For instance, in the third paragraph of the introduction, it should be "relation" instead of "realation." Please review the paper carefully for such errors when revising.

Additional Questions:
<b>Originality of the work</b>
A rating of 1 indicates work that is similar in formulation and approach to many others in the literature. A rating of 5 corresponds to an approach you have not seen taken before.: 4

Originality of the work Comments:

<b>Quality of writing</b>
A rating of 1 indicates work that is hard to understand and/or contains serious grammatical errors. A rating of 5 corresponds to a very well written paper.: 4

Quality of writing Comments:

<b>Technical correctness</b>
A rating of 1 indicates work that has significant flaws and errors. A rating of 5 corresponds to work that is technically correct.: 5

Technical correctness Comments:

<b>All key relevant references are included</b>
A rating of 1 indicates that some very related work is not cited. A rating of 5 indicates that all relevant references are included.: 5

Key references Comments:

<b>The work is reproducible</b>
A rating of 1 indicates that significant details are missing, so that someone reading the work would not be able to replicate the results. A rating of 5 indicates that the description, or code associated with the paper, would be sufficient to allow the results to be replicated.: 4

The work is reproducible Comments:

<b>The paper is a good fit for this journal</b>
A rating of 1 would indicate a poor fit, different from most papers published in the journal. A rating of 5 would indicate a good fit, in line with typical work published in the journal.: 5

The paper is a good fit for this journal Comments:

<b>The work has potentially high impact</b>
A rating of 1 would indicate that it is unlikely others will use or extend this work. A rating of 5 would indicate that it is very likely this will lead to follow-up work.: 4

Potentially high impact Comments:

Reviewer: 2

Recommendation: Accept with minor revisions

Comments:
The introduction provides a good review of the relevant literature. It might be good to include a simple system diagram illustrating the key components of the proposed approach (e.g. similar to Figure 1 in [22]).

On Page 4, after mentioning that the rotation angle is assumed to be measured by a sensor it might be good to also mention an example (e.g. an angular acceleration sensor as mentioned later at the end of Section 3).

In Figure 3, (b) and (c) appear to be identical. Please clarify if this is intended. Please also clarify what the numbers refer to next to the square outlining the CMA i.e. 3.025, 3.000 and 2.975 in the vertical direction and the 3 numbers in the horizontal direction.

From results in Figures 4 and 5 it appears that the performance when using a forgetting factor of 0.9 are quite similar for each method. Please clarify this and also if the error bars, which appear overlapping, represent confidence intervals or some other quantity.

In the first sentence of Section 5.4, it should perhaps say “SFIIVA-O and SFIIVA-M” rather than “SFIIVA-O and SFIIVA-O”.

In Figure 6 (c), it appears that results for Channel 4 might not be as good a other channels in that while there is a brighter region around 176 degrees other regions also appear relatively bright (e.g. between 248 and 320 degrees). Please consider commenting on why this might be the case.

Additional Questions:
<b>Originality of the work</b>
A rating of 1 indicates work that is similar in formulation and approach to many others in the literature. A rating of 5 corresponds to an approach you have not seen taken before.: 4

Originality of the work Comments: The main novelty is the combination of two methods, a blind source separation (BSS) method with a sound field interpolation method to address the problem of BSS applied to Circular Microphone Array (CMA) recordings where the CMA might rotate during separation.

<b>Quality of writing</b>
A rating of 1 indicates work that is hard to understand and/or contains serious grammatical errors. A rating of 5 corresponds to a very well written paper.: 4

Quality of writing Comments: Well written.

<b>Technical correctness</b>
A rating of 1 indicates work that has significant flaws and errors. A rating of 5 corresponds to work that is technically correct.: 5

Technical correctness Comments: This is technically correct.

<b>All key relevant references are included</b>
A rating of 1 indicates that some very related work is not cited. A rating of 5 indicates that all relevant references are included.: 5

Key references Comments: Key references are well covered.

<b>The work is reproducible</b>
A rating of 1 indicates that significant details are missing, so that someone reading the work would not be able to replicate the results. A rating of 5 indicates that the description, or code associated with the paper, would be sufficient to allow the results to be replicated.: 4

The work is reproducible Comments: Algorithms summarizing the implementation are provided in the paper and the experimental setup is clear.

<b>The paper is a good fit for this journal</b>
A rating of 1 would indicate a poor fit, different from most papers published in the journal. A rating of 5 would indicate a good fit, in line with typical work published in the journal.: 5

The paper is a good fit for this journal Comments: This is a good fit.

<b>The work has potentially high impact</b>
A rating of 1 would indicate that it is unlikely others will use or extend this work. A rating of 5 would indicate that it is very likely this will lead to follow-up work.: 3

Potentially high impact Comments: The work is an interesting contribution that provides some advantage over existing methods.
