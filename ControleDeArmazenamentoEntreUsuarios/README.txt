O sistema consiste em:

Pegar o arquivo usuario.txt, tratar os dados dentro dele;
Pegar o arquivo arm_usuarios.txt, tratar os dados dentro dele;
Utilizar os dados de armazenamento dentro de arm_usuarios.txt para criar uma coluna de relação entre o usuário e o armazenamento total do servidor, representado em porcentagem;
Pegar os dados das três tabelas e, por meio dos IDs especificados em usuarios.txt na coluna "IDs" e nos IDs em arm_usuarios.txt na coluna "Id_usuario", mesclar as três tabelas;
A tabela de porcentagem que é criada herda o id_usuario da tabela arm_usuarios.txt;
Depois de mesclar todas as tabelas, é preciso pegar os dados e representá-los no arquivo relatorio.txt;
O sistema também realiza a conversão de bytes, que é o tipo de valor de armazenamento de cada usuário na tabela arm_usuarios.txt, e converte para gigabytes, megabytes ou kilobytes.


