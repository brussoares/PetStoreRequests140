# 1 - bibliotecas
import json         # leitor e escritor de arquivos json
import pytest       # engine / framework de teste de unidade
import requests     # framework de teste de API

# 2 - classe (opcional no Python, em muitos casos)
 
# 2.1 - atributos ou variaveis
# consulta e resultado esperado
pet_id = 476149401          # código do animal
pet_name = "Snoopy"         # nome do animal
pet_category_id = 1         # código da categoria do animal
pet_category_name = "dog"   # titulo da categoria
pet_tag_id = 1              # código do rótulo
pet_tag_name = "vacinado"   # tiulo do rotulo
pet_status = "available"    # status do animal

# informações em comum
url = 'https://petstore.swagger.io/v2/pet'          # endereço
headers = { 'Content-Type': 'application/json' }    # formato dos dados trafegados

# 2.2 - funções / métodos

def test_post_pet():
    # configura
    # dados de entrada estão no arquivo json
    pet=open('./fixtures/json/pet1.json')       # abre o arquivo json
    data=json.loads(pet.read())                 # ler o conteúdo e carrega como json em uma variavel data
    # dados de saída / resultado esperado estão nos atributos acima das funções

    # executa
    response = requests.post(                   # executo o método post com as informações a seguir
        url=url,                                # endereço
        headers=headers,                        # cabeçalho / informaçoes extras da mensagem
        data=json.dumps(data),                  # a mensagem = json
        timeout=5                               # tempo limite da transmissão, em segundos
    )

    # valida
    response_body = response.json()             # cria uma variavel e carrega a resposta em formato json

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name
    
def test_get_pet():
    # configura
    # dados de entrada e saida / resultado esperado estão na seção de atributos antes das funções
    
    # executa
    response = requests.get(
        url= f'{url}/{pet_id}',  # chama o endereço do get/consulta passando o codigo do animal
        headers=headers
    )
    
    
    # valida
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == 'available'
    
    
def test_put_pet():
    # configura
    pet = open('./fixtures/json/pet2.json')
    data = json.loads(pet.read())
    # dados de saida / resultado esperado
    
    # executa
    response = requests.put(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )
    # Valida
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == 'sold'
    
    
def test_delete_pet():
    # configura
    # dados de entrada e saida virão dos atributos
    
    # executa
    response = requests.delete(
        url=f'{url}/{pet_id}',
        headers=headers
    )
    
    # valida
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(pet_id)
    