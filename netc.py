def check_net():
    import requests
    try:
        requests.get('https://google.com')
        return True
    except:
        return False
