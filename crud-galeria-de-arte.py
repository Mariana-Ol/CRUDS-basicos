#lista para armazenar as obras cadastradas
acervo = []

#CREATE
def cadastro_de_obra(nome, artista, ano, tecnica, tamanho, estilo):
    nova_obra = {'nome': nome, 
                 'artista': artista,
                 'ano' : ano,
                 'tecnica' : tecnica,
                 'tamanho' : tamanho,
                 'estilo' : estilo}
    acervo.append(nova_obra)

#READ
#Visualizar todas as obras cadastradas
def visualizar_acervo():
    return acervo

#Visualizar uma obra específica (identificando-a pelo nome)
def visualizar_obra(obra_nome):
    for obra in acervo:
        if obra['nome'] == obra_nome:
            return obra

#Visualizar obras de um determinado artista
def visualizar_obras_artista(artista):
    global acervo
    acervo_filtrado = [obra for obra in acervo if obra['artista'] == artista]
    return acervo_filtrado

#UPDATE      
def atualizar_obra(obra_nome, **kwargs):
    for obra in acervo:
        if obra['nome'] == obra_nome:
            obra.update(**kwargs) #O método update atualiza valores em um dicionário (não pode ser usado em listas)
            print(f'O cadastro de {obra_nome} atualizado com sucesso.')
            return
        else:
            print('Obra não encontrada.')

#DELETE
def excluir_obra(obra_nome):
    for obra in acervo:
        if obra['nome'] == obra_nome:
            acervo.remove(obra)
            print("A obra", obra['nome'], "foi excluída do acervo.")
            return
        else:
            print("Obra não encontrada.")
        

'''O uso de **kwargs em Python é uma maneira de passar um número variável de argumentos nomeados para uma função. 
Quando você utiliza **kwargs, você pode fornecer pares chave-valor como argumentos para a função, e dentro da função esses argumentos são acessados 
como um dicionário.'''


cadastro_de_obra('Femmes au jardin', 'Claude Monet', 1866, 'óleo, canvas', '205 x 255', 'Impressionismo')
cadastro_de_obra('Mount Tabor', 'Benedetta', 1936, ' ', ' ', 'Futurismo')
cadastro_de_obra('Danse à la ville', 'Pierre-Auguste Renoir', 1880, 'óleo, canvas', '90 x 180', 'Surrealismo')
cadastro_de_obra('Lo Spirito', 'Benedetta', 1930, 'guache', ' ', 'Futurismo')


#print(visualizar_acervo())
#print(visualizar_obra('Lo Spirito'))

#atualizar_obra('Danse à la ville', ano = 1883, estilo = 'Impressionismo')  #Corrigindo as informações da obra Danse à la ville

#print(visualizar_obra('Danse à la ville'))