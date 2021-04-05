
def utility(i, S, p, theta, mu, k_ep, k_d, k_p):
    sum = 0
    sum += (k_p*(S[i]-p))
    sum -= penalty(i, S, p, theta, mu, k_ep, k_d, k_p)
    return round(sum, 5)

def penalty(i, S, p, theta, mu, k_ep, k_d, k_p):
    pen = 0
    pen += k_d * (theta[i]-mu)
    pen += k_ep * (S[i]-mu)
    return round(pen, 5)

if __name__=="__main__":
    # config
    N = [1, 2, 3, 4]
    n = len(N)
    
    S = [230, 253, 233, 225]
    
    p = 170
    theta = [170, 195, 170, 170]
    mu = sum(theta) / len(theta)

    k_ep, k_d, k_p = 4.8, 6.0, 0.8

    # printing utilities
    utils = []
    pens = []
    for i in N:
        utils.append(utility(i-1, S, p, theta, mu, k_ep, k_d, k_p))
        pens.append(penalty(i-1, S, p, theta, mu, k_ep, k_d, k_p))
    print(f"Utility = {utils}")
    print(f"Penalty = {pens}")


