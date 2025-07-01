Este blog de receitas foi totalmente desenvolvido para concretizar meu conhecimento em Django.

Este projeto, compreende as noções básicas sobre desenvolvimento fullstack. 

# Frontend + Views Django

Inicialmente utilizando apenas HTML, CSS e Javascript puro foi desenvolvido a Home do blog.

![image](https://github.com/user-attachments/assets/c6fa10c9-b19b-4074-95b5-40cf5798e57e)

Utilizando Class based view, foi criado no django para renderizar as home, realizando a busca na queryset por todas as receitas cadastradas.

Além disso, foi criado a view de detalhe de cada receita, apenas clicando na receita desejada, é possível visualizá-la

![image](https://github.com/user-attachments/assets/121b6835-f0f7-4f06-be0e-4b892ceb368a)

Também utilizando logica em python foi criado o metodo de paginação caso exceda o número de receitas possíveis de aparecer em uma página, no caso, 9 receitas.

![image](https://github.com/user-attachments/assets/9f84b73f-cae6-402f-a793-6f5b6c89944e)

Também há filtro por receita que deseja pesquisar ou categorias de receita, como café da manhã, vegana, etc.

Nesse caso um filtro realizado só por receitas veganas,

![image](https://github.com/user-attachments/assets/20df74d1-3bf8-4005-b4ac-42287b5b8cf2)

Nesse caso pesquisa por nome de receita, "Torta".

![image](https://github.com/user-attachments/assets/e780b552-88ce-4616-a98a-f2be42d7d61f)

# Cadastro de usuários e logins

Foi desenvolvido a parte de cadastro de usuários permitindo o usuário realizar seu cadastro, tomando todo cuidado com segurança e evitando inserir dados maliciosos...

![image](https://github.com/user-attachments/assets/a7a1f07b-5d1f-4b98-8dab-72ad4f51b000)

Checando os inputs que o usuário colocou e avisando possíveis erros...

![image](https://github.com/user-attachments/assets/9bdb014e-b51d-4cf8-98e5-dafd27fd4f9f)

Relização de cadastro com sucesso...
![image](https://github.com/user-attachments/assets/cfce0860-71e4-4c90-85aa-305f8f15ee58)

Permitido realizar Login...
![image](https://github.com/user-attachments/assets/b2538f5f-85de-4141-bf78-05961ff0ef13)

Formulário de cadastro de novas receitas...
![image](https://github.com/user-attachments/assets/beb4b856-e5f1-4db1-8866-149058f1df2a)

Realização do Logout e redirecionado para tela de login. Foi desenvolvido todo o cuidado para usuários sem login não conseguir acessar os endpoints relacionados a cadastro de receitas ou acesso ao dashboard.
![image](https://github.com/user-attachments/assets/97aac648-50d4-43d6-89bd-8f1ffcd6d8fe)


# Em desenvolvimento
Frotend do Dashboard dos usuários com suas receitas...
Melhoria do Frontend de login, cadastro e formulário da criação de receitas...



