#----CONDIÇÕES ANINHADAS----

#Basicamente colocar uma estrutura dentro da outra 

Nome = str(input('Qual é o seu nome? ')).strip()

Nome = Nome.lower()

#-----Aplicacao incorreta-----

#Caso usemos outro if como condição secundária o programa executará os dois if se uma das condições for atendida, ou seja, para criar um programa que atenda varias condições distintas nos temos que usar elif

#if Nome == 'gustavo':
#    print('Bom dia {} seu nome é muito bonito!'. format(Nome))
   
#if Nome == 'lucas' or 'pedro' or 'joao':
#    print('Bom dia {} seu nome é muito comum!'. format(Nome))

#Porque essa aplicaocao nao funciona mas o ex_033 funciona?
# Primeira explicacao: Para o python o que foi escrito foi --> if (nome == 'lucas') or ('pedro') or ('joao'). Como pedro e joao nao estao sendo comparadas a nenhuma variavel
# o python enxerga-os como "strings nao vazias" que tambem sao interpretadas como um true booleano, ou seja,
# o python entende o codigo como "se o nome digitado for lucas ou SE QUALQUER COISA FOR DIGITADA rode essa parte do codigo" ou seja, mesmo que se digite gustavo que eh
# uma condicao verdadeira o outro if sera rodado ja que uma outra condicao tambem sera verdadeira (no caso digitar qualquer coisa)  

#Quando usar apenas if e quando usar elif
# Ou seja usar uma estrutura condicional sem elif, implica que todas as possiveis condicoes ja foram listadas dentro do if (como eh o caso do ex_033).
# No caso do codigo a cima uma condicao foi atendida mas com a ausencia de um elif as outras condicoes serao verificadas.
# Caso existisse um elif e fosse digitado 'gustavo' nenhuma outra condicao sera verificada
# ou seja, apenas com if's mesmo se uma condicao for verdadeira outras condicoes serao verificadas.
# com a presenca de um elif, caso uma das condicoes sejam verdadeiras as outras condicoes nao serao verificadas. 


#-----Aplicacao correta 1-----

#if Nome == 'gustavo':
#    print('Bom dia {} seu nome e muito bonito!'. format(Nome))
#if Nome == 'lucas' or Nome == 'pedro' or Nome == 'joao':
#    print('Bom dia {} se nome e muito comum!')

#Aqui todas as condicoes possiveis foram cobertas, caso seja digitado um nome que nao seja um dos tres  nada sera exibido

#-----Aplicacao correta 2-----

#if Nome == 'gustavo':
#    print('Bom dia {} seu nome e muito bonito!'. format(Nome))
#elif Nome == 'lucas' or 'pedro' or 'joao':
#    print('Bom dia {} se nome e muito comum!') 

#Aqui, mesmo que duas condicoes sejam verdadeiras a primeira que for atendida sempre tera prioridade (caso nao tenha entendido leia as anotacoes mais acima a respeito)

#-----Aplicacao correta 2-----

#if Nome == 'gustavo': 
#    print ('Bom dia {} seu nome é muito bonito!'. format(Nome))
#elif Nome == 'lucas' or Nome =='pedro' or Nome == 'joão':
#    print('Bom dia {} seu nome e muito comum!'. format(Nome))
#else:
#    print('Bom dia {}!'. format(Nome))

#Aqui todas as possibilidades estao delimitadas corretamente ou seja, mesmo se escrevessemos sem elif ainda funcionaria, com o adicional de uma mensagem extra
#caso as duas primeiras condicoes nao sejam atendidas, novamente, cobrindo todas as possibilidades e corrigindo a questao do 'or'

#=====DICAS IMPORTANTES=====

#sempre ler estruturas de controle como. "Para tal coisa acontecer uma dessas condicoes deve ser atendida (No caso de OR)" 
#Ou "Uma dessas condicoes deve ser atendida (no caso do AND)" 

