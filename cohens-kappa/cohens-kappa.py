import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    rater1 = np.array(rater1)
    rater2 = np.array(rater2)
    n = len(rater1)
    p_o = np.sum(rater1 == rater2) / n

    labels = np.union1d(rater1,rater2)
    p_e = 0.0
    for label in labels:
        count1 = np.sum(rater1 == label)
        count2 = np.sum(rater2 == label)

        p_e += (count1/n) * (count2/n)

    if p_e == 1.0:
        return 1.0

    return (p_o - p_e) / (1-p_e)