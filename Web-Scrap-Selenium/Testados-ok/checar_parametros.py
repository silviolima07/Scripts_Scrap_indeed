#!/usr/bin/env python

import sys
import os
from bs4 import BeautifulSoup

# total arguments
#n = len(sys.argv)-1

def checar_input(n):
    # total arguments
    #n = len(sys.argv)-1

    #cargo = sys.argv[1]

    # Checar parametros de entrada
    #print("Numero de parametros:", n)
    if (n != 1):
        print ("Illegal number of parameters")
        print ("Usage: scrap-indeed.sh CARGO")
        print ("Example: scrap-indeed.sh 'Cientista de dados'")
        exit()


#######################################################################
    
def buscar_campos(driver, url_page, total_vagas):
    cargo=[]
    local=[]
    empresa=[]
    descricao=[]
    page=1
    # O numero de vagas por pagina é 10. Se o total de vagas for menor que 10, pelo 1 pagina é mostrada.
    # Se o numero for 13, vai mostrar 1 pagina com 10 e outra com 3, no total 2 paginas.
    pagina_final = (int(total_vagas/10)+1)*10

    url_page = url_page+str('&start=')

    pagina_limite = 100 # Seria aqui o total de vagas se fosse pesquisar todas vagas
                       # Dessa forma as primeiras 5 paginas apenas.

    if (pagina_final < pagina_limite):
        pagina_limite = pagina_final
    
    print("Serão pesquisadas ", int(pagina_limite/10), "paginas")

    for n in range(0,pagina_limite,10):
        
        print("URL pesquisada:", url_page+str(n))
        driver.get(url_page+str(n))
        driver.implicitly_wait(5)
        all_jobs = driver.find_elements_by_class_name('result')

        for job in all_jobs:

            result_html = job.get_attribute('innerHTML')
            soup = BeautifulSoup(result_html, 'html.parser')
		
            try:
                title = soup.find("a", class_="jobtitle").text.replace('\n', '')
            except:
                title = 'None'
            cargo.append(title)
               

            try:
                location = soup.find(class_="location").text
            except:
                location = 'None'
            local.append(location)        

            try:
                company = soup.find(class_="company").text.replace("\n", "").strip()
            except:
                company = 'None'
            empresa.append(company)        


            try:
                summary = soup.find(class_="summary").text.replace("\n", "").strip()
            except:
                summary = 'None'
            descricao.append(summary)

            #try:
            #    #next_page = driver.find_element_by_xpath('//a[@aria-label={}]//span[@class="pn"]'.format(n+1))
            #    next_page = driver.find_elements_by_css_selector("[aria-label= {}]").format(n+1)
            #    next_page.click()
            #    print("Next page:", n+1)

            #except:
            #    #next_page = driver.find_element_by_xpath('//a[@aria-label="Next"]//span[@class="pn"]')
            #    next_page = driver.find_elements_by_css_selector("[aria-label='Next']")
            #    next_page.click()
            #    print("Next page:", n)

        print("Page: {}".format(str(page)))
        page=page+1
       

    return (cargo, local, empresa, descricao)

