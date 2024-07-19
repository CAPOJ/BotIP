def check_for(adress):
    ip = adress.split('/')[0]
    sbmsk = adress.split('/')[1]
    return ip, sbmsk