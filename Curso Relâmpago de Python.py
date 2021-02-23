#!/usr/bin/env python
# coding: utf-8

# # Curso Relâmpago de Python

# ## ---------------------------------------------------------------------------------------------------------------------------------

# #### Faremos um breve resumo sobre programação em Python
# #### Este Curso é voltado a pessoas com algum conhecimento básico em programação
# #### Se você é novo, esse curso talvez seja muito avançado para você
# #### Se você já tem boas bases em Python, avance para os exercícios!

# ## -------------------------------------------------------------------------------------------------------------------------------

# ## O que esse curso cobrirá ?

# Tipos númericos
# Strings
# Prints
# Listas
# Dicionários
# Boleanos
# Tuplas e Sets
# Operadores Lógicos
# If, Else, Elif
# For, While
# Range
# Funções
# Expressões Lambda
# MAp e Filter
# 

# ## Operações Básica, váriaveis, strings, listas e indexação

# #### com Python é possivel realizar operações matemáticas.

# ###### Soma

# In[7]:


1+1


# ###### Multiplicação

# In[11]:


1*3


# ###### Divisão

# In[13]:


1/2


# ###### potenciação

# In[14]:


3**2


# ###### Resto de Divisão - Retorna o resto da divisão 

# In[6]:


4 % 2


# #### identificando o tipo da variavel 
# #### método Type()

# In[15]:


type(1)


# In[16]:


type(2.0)


# In[17]:


type('bruno')


# #### Realização de expressões matemáticas 

# In[19]:


(3 + 2)*(4+1)


# ## Atribuições de Variavéis
# 
# #### variaveis são locais na memória onde são guardadas informações
# #### não pode nomear uma variavel com usando números ou caracteres especiais
# #### as variaveis também são "case sensitives" ou seja  x != X.

# In[30]:


x = "a"
X = "b"
print(x,X)


# # ---------------------------------------------------------------------------------------------------------------

# # Listas 

# ### Listas permitem que sejam guardados multiplas informações. Listas começam com []
# 
# #### lista = [ ]

# In[23]:


lista = [1,2,3]


# In[24]:


type(lista)


# In[25]:


print(lista)


# ##### listas são indexadas, a indexação em python começa em zero. Assim podemos acessar um determinado valor pela sua posição indexada. 

# In[26]:


lista [0]


# In[27]:


lista [1]


# In[28]:


lista[2:3]


# In[29]:


lista[1:3]


# # -------------------------------------------------------------------------------------------------------------

# # Dicionários 

# ###  Dicionarios guardam informações associando chaves e valores

# In[31]:


dic = {'chave1':1, 'chave':2}


# In[32]:


dic


# In[33]:


type(dic)


# In[35]:


dic['chave1']


# ##### dicionarios podem guardar listas

# In[36]:


dic2 = {'lista1':[1,2,3], 'lista2':['a','b','c']}


# In[38]:


dic2


# In[39]:


dic2['lista1']


# In[40]:


dic2['lista2']


# # ---------------------------------------------------------------------------------------------------------------

# # Tuplas 

# ### Tuplas são listas imutaveis. 

# In[41]:


tup = (1,2,3)


# In[42]:


type (tup)


# In[43]:


tup[1]


# # ---------------------------------------------------------------------------------------------------------------

# # booleanos 

# In[44]:


### booleanos comparam valores ou expressões lógicas 


# In[45]:


True


# In[46]:


False


# ##### Comparador de igual ==

# In[49]:


1 == 1


# In[51]:


x = 1


# In[52]:


x == 2


# In[53]:


x == 1


# In[54]:


x > 1


# In[55]:


x >= 1


# In[56]:


x != 1


# In[57]:


(x == 1) and (x > 0)


# In[58]:


(x == 1) or (x < 0)


# ### exemplo

# In[64]:


y = 'Reprovado'


# In[65]:


x = 8 


# In[66]:


if x > 7:
    y = 'Aprovado'


# In[67]:


y


# ### Exemplo 

# In[75]:


x = 4


# In[76]:


if x > 7:
    y = 'Aprovado'
else:
    y = 'Reprovado'


# In[77]:


y


# ### Exemplo

# In[73]:


if x > 7:
    y = 'apravado'
elif x > 4:
    y = 'recuperação'
else:
    y = 'reprovado'


# In[74]:


y


# # ---------------------------------------------------------------------------------------------------------------

# # Métodos de iteração For, while

# In[79]:


seq = [1, 2, 3, 4, 5]


# In[80]:


for item in seq:
    print(item)


# #### para fazer uma iteração em python é necesssário criar um objeto que ira possar ao longo por todo os objetos de um objeto
# #### que seja iterável. 

# In[81]:


for item in seq:
    print("hello world")


# ### Método Range( )

# ##### O métod range cria um método que é um iterável  

# ### Looping for

# In[82]:


range (0,100)


# In[84]:


for i in range (0, 10):
    print (i)


# #### você pode criar uma lista usando range

# In[86]:


seq = list(range(0,10))


# In[87]:


print(seq)


# ### Looping While 

# In[90]:


i = 1


# In[91]:


while i < 5:
    print ('i vale: {}'.format(i))
    i = i+1


# #### exemplo

# In[93]:


out = []


# In[94]:


x = [1, 2, 3, 4]


# In[95]:


for item in x:
    out.append(item**2)
out


# ### List compreension

# In[96]:


[item**2 for item in x]


# # ---------------------------------------------------------------------------------------------------------------

# # Funções 

# #### funções são utilizadas quando temos trechos de códigos que precisam ser reutilizados ao longo do programa

# In[97]:


def minha_func(parametros):
    print(parametros)


# In[98]:


minha_func


# In[99]:


minha_func("Hello World")


# #### funções podem ou não retornar valores

# In[100]:


def minha_func(parametros):
    x = parametros**2
    return x


# In[101]:


x = 2


# In[102]:


y = minha_func(x)


# In[103]:


y


# # ---------------------------------------------------------------------------------------------------------------

# # Funções Lambdas 

# #### facilitam a redução do tamanho de código

# ##### exemplo: um função normal  

# In[104]:


def quadrado (var):
    return var ** 2


# In[105]:


quadrado(2)


# #### exemplo: função lambda (só seram usada uma unica vez)

# In[106]:


lambda var: var**2


# ### Map e Filter

# ##### Map passa todos os valores de um sequencia para a funçao

# In[107]:


seq = [1, 2, 3, 4, 5]


# In[108]:


map (quadrado, seq)


# In[109]:


list(map(quadrado, seq))


# In[114]:


list (map(lambda x:x**2, seq))


# #### Filter extrai os valores que cumprem o estipulado

# In[113]:


list (filter(lambda item: item % 2 == 0, seq))


# In[ ]:




