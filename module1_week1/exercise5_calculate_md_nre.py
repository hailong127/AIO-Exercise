def md_nre_single_sample(y, y_hat, n, p):
    y_root = y**(1/n)
    y_hat_root = y_hat**(1/n)
    loss = (y_root-y_hat_root)**p
    return print(loss)


md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1)
md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1)
md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1)
md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1)