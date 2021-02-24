#!/usr/bin/env python
# coding: utf-8

# ## Exercícios de Revisão em python
# 
# Exércicios de compreensão sobre as funcionalidades do Python. 

# ### Exercícios
# Responda as perguntas ou complete as tarefas em negrito abaixo, use o método específico, se aplicavel. 

# #### -- Resolva: 7 elevado a 4 potência

# In[2]:


a = 7**4
print("7 elevado a 4 potência = ", a)


# #### -- Quebre a seguinte string em uma lista

# s = "Olá, pai!"

# In[3]:


s = "Olá, pai!"
a = s.split(',')
print (a)


# ## -- Dadas as variáveis: 
# 
# planeta = "Terra"
# 
# Diametro = 12742
# 
# #### -- Use .format() para printar a seguinte frase: 
# 
# O diâmetro da Terra é de 12742 kilômetros. 

# In[5]:


planeta = "Terra"
diametro = 12742

print(f'O diâmetro da {planeta} é de {diametro} de quilometros')


# In[9]:


print('O diâmetro da {} é de {} de quilometros'.format(planeta, diametro))


# ## -- Dada a lista abaixo,use indexação para obter apenas a string "Olá".

# In[10]:


lst = [1,2,[3,4],[5,[100,200,['olá']],23,11],1, 7]


# In[26]:


print(lst[3][1][2])


# ## -- Dado o seguinte dicionário aninhado, extraia a palavra "olá"

# In[12]:


d = {'k1':[1, 2, 3, {'café':['banana','mulher','colher',{'alvo':[1,2,3,'olá']}]}]}


# In[11]:


print(d.items())


# ## -- Construa uma função que retire o dominio dado um e-mail no seguinte formato: 
# 
# ##### Exemplo:
# ##### user@domain.com
# ##### Retorna:
# ##### domain.com

# In[16]:


def retornaDominio(mail):
    if '@' in mail:
        a = 1 + mail.index('@')
        print(mail[a:])


# In[23]:


mail = 'user@domain.com'


# In[24]:


retornaDominio(mail)


# ## -- Crie uma função que retorna True se a palavra 'dog' estiver contida na string de entrada. Não se preocupe  com os casos de extremosomo uma pontuação que está sendo anexada à palavra 'dog', mas que seja case sensitive

# In[37]:


def encontraDog(parametro):
    parametro = parametro.lower()
    if 'dog' in parametro:
        return True
    else:
        return False
    


# In[38]:


parametro = 'Existe um dog ai ?'
parametro_2 = 'EXISTE UM DOG AI ?'


# In[39]:


encontraDog(parametro)


# In[40]:


encontraDog(parametro_2)


# ## -- Use expressões lambda e a função filter() para filtrar as palavras de uma lista que não começa com a letra "S". Por Exemplo
# ##### seq = ['sopa','cachorro','salada','gato','ótimo']
# ##### Deve ser filtrada para:
# ##### seq = ['sopa','salada']

# In[41]:


seq = ['sopa','cachorro','salada','gato','ótimo']


# In[45]:


list(filter(lambda item: item[0] == 's', seq))


# #### -- Você está dirigindo um pouco rápido demais, e um policial para você. Escreva uma função para retornar um dos 3 resultado possiveis: "Sem multa", "Multa Pequena" ou "Multa Grande". Se a sua velocidade for igual ou inferior a 60, o resultado é "sem multa". Se a velocidade for entre 61 e 80, o resultado é "Multa pequena". Se a velocidadae é e 81 ou mais, o resultado é "Multa Grande". A menos que seja seu aniversário. Em seu aniversário, sua velocidade poser ser 5 unidades maior em todos os casos. 

# In[47]:


from datetime import date
def capturar_velocidade(velocidade, aniversario):
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    dia_A = aniversario[0:1]
    mes_A = aniversario [3:4]
    
    if (dia_A == dia) and (mes_A == mes):
        if velocidade >= 85:
            print("Multa Alta")
        elif velocidade < 85  or  velocidade > 65:
            print ("Multa pequena")
        else:
            print("Sem Multa")
            
    else:
        if velocidade >= 80:
            print("Multa Alta")
        elif velocidade < 80  or  velocidade > 60:
            print ("Multa pequena")
        else:
            print("Sem Multa")
        
    


# In[48]:


capturar_velocidade(65, '14/08/1986')


# In[49]:


capturar_velocidade(81,'14/08/1986')


# In[ ]:




