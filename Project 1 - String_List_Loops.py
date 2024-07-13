#!/usr/bin/env python
# coding: utf-8

# An e-commerce company, Store 1, recently started collecting data on its customers. Store 1's goal is to better understand customer behavior and make data-driven decisions to improve their online experience.
# 
# As part of the analytics team, your first task is to assess the quality of a sample of collected data and prepare it for future analysis.
# 
# ==========================================================================================================================
# 
# Uma empresa de comércio eletrônico, Store 1, começou recentemente a coletar dados sobre seus clientes. O objetivo da Store 1 é entender melhor o comportamento dos clientes e tomar decisões baseadas em dados para melhorar experiência online deles.
# 
# Como parte da equipe analítica, sua primeira tarefa é avaliar a qualidade de uma amostra de dados coletados e preparar elas para análises futuras.

# # Quiz
# 
# Store 1 aims to ensure consistency in data collection. As part of this effort, the quality of the data collected on users needs to be assessed. You have been asked to review the data collected and propose changes. Below, you will see data on a particular user. Review the data and identify possible problems.
# 
# ==========================================================================================================================
# 
# A Store 1 visa garantir a consistência na coleta de dados. Como parte desse esforço, a qualidade dos dados coletados sobre os usuários precisa ser avaliada. Foi pedido que você revise os dados coletados e proponha alterações. Abaixo, você verá dados sobre um determinado usuário. Revise os dados e identifique possíveis problemas.

# In[1]:


user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']


# **Options:**
# 
# 1. The data type of `user_id` should be changed from string to integer.
#     
# 2. The `user_name` variable contains a string with unnecessary spacing and an underscore between the first and last name.
#     
# 3. The data type of `user_age` is incorrect.
#     
# 4. The `fav_categories` list contains strings in capital letters. We should convert the values in the list to lower case instead.
# 
# ==========================================================================================================================
# 
# **Opções:**
# 
# 1. O tipo de dados de `user_id` deve ser alterado de string para número inteiro (integer).
#     
# 2. A variável `user_name` contém uma string com espaçamento desnecessário e um sublinhado entre o nome e o sobrenome.
#     
# 3. O tipo de dados de `user_age` está incorreto.
#     
# 4. A lista `fav_categories` contém strings em letras maiúsculas. Em vez disso, devemos converter os valores da lista para letras minúsculas.

# Write in the Markdown cell below the number of options you have identified as problems. If you have identified several problems, separate the number with commas. For example, if you think the numbers 1 and 3 are incorrect, write 1, 3, and explain why.
# 
# ==========================================================================================================================
# 
# Escreva na célula Markdown abaixo o número de opções que você identificou como problemas. Se você identificou vários problemas, separe o número por vírgulas. Por exemplo, se você acha que os números 1 e 3 estão incorretos, escreva 1, 3, e explique o motivo.

# **Write your answer and explain your reasoning:**
# 
# 
# 2 - There is a space at the beginning and end of the name that is unnecessary and to be standardized it is ideal to delete it, and the separation of the name is not incorrect to be done with " _ ", but separating it by space makes the information cleaner.
# 
# 3 - User_age is set to float when it should be set to int, because when we talk about age we only have whole numbers and no decimal places.
# 
# 4 - fav_categories should be lowercase because being uppercase is not wrong, however, to ensure ease of use and consistency it is better to transform them as indicated.
# 
# **Bonus: Option 1 is correct to be in str because although it is just a number, it is an identification assigned to the customer and will not be used to perform numerical operations.
# 
# ==========================================================================================================================
# 
# **Escreva sua resposta e explique seu raciocínio:**
# 
# 
# 2 - Existe um espaço na parte inicial e final do nome que é desnecessário e para ficar padronizado é ideal apagar, e a separação do nome não está incorreta ser feita com " _ ", porém separar por espaço deixa a informação mais limpa.
# 
# 3 - User_age está como float quando essa informação deverá ser int, pois quando falamos de idade temos apenas números inteiros e sem qualquer casa decimal
# 
# 4 - fav_categories devemos transformar para minúscula porque estar em maiúscula não está errado, contudo, para garantir 
# uma facilidade no uso e consistência é melhor transformâ-las como indicado.
# 
# **Bônus: A opção 1 está correta estar como str porque apesar de ser apenas números trata-se de uma identificação atribuída ao cliente e não será utilizado para fazer operações numéricas**

# # Task 1
# 
# Let's implement the changes we've identified. First, we want to fix the problems with the `user_name` variable. As we've seen, it has unnecessary spaces and an underscore as a separator between the first and last name. Your goal is to remove the spaces and then replace the underscore with a space.
# 
# ==========================================================================================================================
# 
# # Tarefa 1
# 
# Vamos implementar as mudanças que identificamos. Primeiro, queremos corrigir os problemas com a variável `user_name`. Como verificamos, ela possui espaços desnecessários e um sublinhado como separador entre o nome e o sobrenome. Seu objetivo é remover os espaços e depois substituir o sublinhado por espaço.

# In[1]:


user_name = ' mike_reed '
user_name = user_name.strip() # remove spaces from the original string / remova os espaços na string original
user_name = user_name.replace('_',' ') # replace the underline with a space / substitua o sublinhado por espaço

print(user_name)


# # Task 2
# 
# Next, we need to split the updated `user_name` into two substrings to get a list that contains two values: the string for the first name and the string for the last name.
# 
# ==========================================================================================================================
# 
# # Tarefa 2
# 
# Em seguida, precisamos dividir o `user_name` atualizado em duas substrings para obter uma lista que contém dois valores: a string para o nome e a string para o sobrenome.

# In[3]:


user_name = 'mike reed'
name_split = user_name.split(' ') # split the user_name string here / divida a string user_name aqui

print(name_split)


# # Task 3
# 
# Great! Now we want to work with the `user_age` variable. As we mentioned before, it has an incorrect data type. Let's correct this problem by transforming the data type and printing the final result.
# 
# ==========================================================================================================================
# 
# # Tarefa 3
# 
# Ótimo! Agora queremos trabalhar com a variável `user_age`. Como mencionamos antes, ela possui um tipo de dados incorretos. Vamos corrigir esse problema transformando o tipo de dados e imprimindo o resultado final.

# In[4]:


user_age = 32.0
user_age = int(user_age) # change the data type of a user's age / altere o tipo de dados da idade de um usuário

print(user_age)
print(type(user_age)) # line of code created just to check and make sure the variable has the correct type / linha de código criada apenas para conferir e garantir que a variável ficou com o tipo correto


# # Task 4
# 
# As we know, data isn't always perfect. We have to consider scenarios in which the value of `user_age` cannot be converted into an integer. To prevent our system from failing, we must take steps in advance.
# 
# Write a code that tries to convert the variable `user_age` into an integer and assigns the transformed value to `user_age_int`. If the attempt fails, we will display a message asking the user to provide their age as a numeric value with the message: `Provide your age as a numeric value.`
# 
# ==========================================================================================================================
# 
# # Tarefa 4
# 
# Como sabemos, os dados nem sempre são perfeitos. Temos que considerar cenários em que o valor de `user_age` não pode ser convertido em um número inteiro. Para evitar que nosso sistema falhe, devemos tomar medidas com antecedência.
# 
# Escreva um código que tenta converter a variável `user_age` em um número inteiro e atribua o valor transformado a `user_age_int`. Se a tentativa falhar, vamos exibir uma mensagem solicitando que o usuário forneça sua idade como um valor numérico com a mensagem: `Forneça sua idade como um valor numérico.`

# In[5]:


user_age = 'thirty two' # this is the variable that stores the age as a string. / esta é a variável que armazena a idade como uma string.

try:
    user_age_int = int(user_age)
    print(user_age_int)
except:
    print('Forneça sua idade como um valor numérico')


# # Task 5
# 
# Finally, note that all the bookmark categories are stored in capital letters. To populate a new list called `fav_categories_low` with the same categories, but in lower case, repeat the values in the `fav_categories` list, modify them and append the new values to the `fav_categories_low` list. As always, print the final result.
# 
# ==========================================================================================================================
# 
# # Tarefa 5
# 
# Por fim, observe que todas as categorias de favoritos são armazenadas em letras maiúsculas. Para preencher uma nova lista chamada `fav_categories_low` com as mesmas categorias, mas em letras minúsculas, repita os valores na lista `fav_categories`, os modifique e anexe os novos valores à lista `fav_categories_low`. Como sempre, imprima o resultado final.

# In[6]:


fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []

for categories in fav_categories:
    fav_categories_low.append(categories.lower())

print(fav_categories_low)


# # Task 6
# 
# We have obtained additional information on the consumption habits of our users, including the amount spent in each of their favorite categories. Management is interested in the following metrics:
# 
# - Total amount spent by the user
# - Minimum amount spent
# - Maximum amount spent
# 
# Let's calculate and print these values:
# 
# ==========================================================================================================================
# 
# # Tarefa 6
# 
# Conseguimos informações adicionais sobre os hábitos de consumo de nossos usuários, incluindo o valor gasto em cada uma de suas categorias favoritas. A administração está interessada nas seguintes métricas:
# 
# - Valor total gasto pelo usuário
# - Valor mínimo gasto
# - Valor máximo gasto
# 
# Vamos calcular e imprimir esses valores:

# In[7]:


fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]

total_amount = sum(spendings_per_category)
max_amount = max(spendings_per_category)
min_amount = min(spendings_per_category)


print(total_amount)
print(max_amount)
print(min_amount)


# # Task 7
# 
# The company wants to offer discounts to its loyal customers. Customers who make purchases totaling more than $1,500 are considered loyal and will receive a discount.
# 
# Our goal is to create a `while` loop that checks the total amount spent and stops when it is reached. To simulate new purchases, the `new_purchase` variable generates a number between 30 and 80 in each cycle. This represents the amount of money spent on a new purchase, and is what you need to add to the total.
# 
# As soon as the target value is reached and the `while` cycle is closed, the final value is printed.
# 
# ==========================================================================================================================
# 
# # Task 7
# 
# A empresa quer oferecer descontos aos seus clientes fiéis. Clientes que fizerem compras totalizando mais de $1.500 são considerados fiéis e vão receber um desconto.
# 
# Nosso objetivo é criar um ciclo `while` que verifique o valor total gasto e pare quando ele for atingido. Para simular novas compras, a variável `new_purchase` gera um número entre 30 e 80 em cada ciclo. Isso representa a quantidade de dinheiro gasto em uma nova compra, e é o que você precisa adicionar ao total.
# 
# Assim que o valor alvo for atingido e o ciclo `while` for encerrado, o valor final será impresso.

# In[8]:


from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent <= 1500: 
	new_purchase = randint(30, 80) 
	total_amount_spent += new_purchase 

print(total_amount_spent)
print('Cliente fiel. Enviar oferta desconto') 


# # Task 8
# 
# We now have all the information about a customer the way we want it. The administration of a company has asked us to find a way to summarize all the information about a user. Their goal is to create a formatted string that uses information from the `user_id`, `user_name` and `user_age` variables.
# 
# Here is the final string we want to create: `User 32415 is called mike and is 32 years old.'`
# 
# ==========================================================================================================================
# 
# # Tarefa 8
# 
# Agora temos todas as informações sobre um cliente da maneira que queremos. A administração de uma empresa nos pediu para encontrar uma maneira de resumir toda a informação sobre um usuário. Seu objetivo é criar uma string formatada que usa informações das variáveis ​​`user_id`, `user_name` e `user_age`.
# 
# Aqui está a string final que queremos criar: `Usuário 32415 chama-se mike e tem 32 anos.`

# In[9]:


user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

user_info = "Usuário {} chama-se {} e tem {}".format(user_id, user_name[0], user_age)

print(user_info)


# As you may already know, companies collect and store data in a specific way. Store 1 wants to store all the information about its customers in a table.
# 
# | user_id | user_name | user_age | purchase_category | spending_per_category |
# | --- | --- | --- | --- | --- |
# | '32415' | 'mike', 'reed' | 32 | 'electronics', 'sport', 'books' | 894, 213, 173 |
# | '31980' | 'kate', 'morgan' | 24 | 'clothes', 'shoes' | 439, 390 |
# 
# In technical terms, a table is simply a nested list that has a sublist for each user.
# 
# Store 1 has created such a table for its users. It is stored in the variable `users`. Each sublist contains the user's ID, first and last name, age, favorite categories and the amount spent on each category.
# 
# ==========================================================================================================================
# 
# Como você já deve saber, as empresas coletam e armazenam dados de uma maneira específica. A Store 1 deseja armazenar todas as informações sobre seus clientes em uma tabela.
# 
# | user_id | user_name | user_age | purchase_category | spending_per_category |
# | --- | --- | --- | --- | --- |
# | '32415' | 'mike', 'reed' | 32 | 'electronics', 'sport', 'books' | 894, 213, 173 |
# | '31980' | 'kate', 'morgan' | 24 | 'clothes', 'shoes' | 439, 390 |
# 
# Em termos técnicos, uma tabela é simplesmente uma lista aninhada que possui uma sublista para cada usuário.
# 
# A Store 1 criou essa tabela para seus usuários. Ela está armazenada na variável `users`. Cada sublista contém o ID do usuário, nome e sobrenome, idade, categorias favoritas e o valor gasto em cada categoria.

# # Task 9
# 
# To calculate the company's revenue, follow these steps:
# 
# 1. Use a `for` loop to iterate through the `users` list.
# 2. Extract the list of expenses for each user and add up the values.
# 3. Update the revenue figure with the total for each user.
# 
# This will give you the company's total revenue, which you will print out at the end.
# 
# ==========================================================================================================================
# 
# # Tarefa 9
# 
# Para calcular a receita da empresa, siga estas etapas:
# 
# 1. Use um ciclo `for` para iterar na lista `users`.
# 2. Extraia a lista de gastos de cada usuário e some os valores.
# 3. Atualize o valor da receita com o total de cada usuário.
# 
# Isso vai fornecer a receita total da empresa, que você vai imprimir no final.

# In[9]:


users = [
  
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
        [894, 213, 173]
    ], 

    
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'shoes'],
        [439, 390]
    ]
]

revenue = 0

for user in users:
	spendings_list = user[4]
	total_spendings = sum(spendings_list) 
	revenue += total_spendings


print(revenue)


# # Task 10
# 
# Use a for loop to go through the list of users we have provided and print out the names of customers under 30.
# 
# ==========================================================================================================================
# 
# # Tarefa 10
# 
# Use um ciclo for para percorrer a lista de usuários que fornecemos e imprima os nomes dos clientes com menos de 30 anos.

# In[10]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]


for user in users:
    if user[2] < 30:
        full_name = ' '.join(user[1])
        print(full_name)


# # Task 11
# 
# Let's combine tasks 9 and 10 and print out the names of users under the age of 30 with total spending over 1,000 dollars.
# 
# ==========================================================================================================================
# 
# # Tarefa 11
# 
# Vamos juntar as tarefas 9 e 10 e imprimir os nomes de usuários com menos de 30 anos com gastos totais acima de 1.000 dólares.

# In[11]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

for user in users:
    spendings_list = user[4] # primeiro temos de extrair os dados dos gastos
    total_spendings = sum(spendings_list) # depois de extraído podemos somar estes dados para ter o valor gasto, para ser possível fazer o loop de verificação
    if user[2] < 30 and total_spendings > 1000:
        full_name = ' '.join(user[1])
        print(full_name)
        


# # Task 12
# 
# Now let's print the name and age of all the users who have bought clothes. Print the name and age in the same print statement.
# 
# ==========================================================================================================================
# 
# # Tarefa 12
# 
# Agora vamos imprimir o nome e a idade de todos os usuários que compraram roupas (clothes). Imprima o nome e a idade na mesma instrução de impressão.

# In[12]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]


for user in users:
    if 'clothes' in user[3]:
        full_name = ' '.join(user[1])
        age = user[2]
        print('{}, {}'.format(full_name, age))

