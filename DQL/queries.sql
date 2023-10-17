/* Linguagem de Consulta de Dados (DQL - do inglês Data Query Language):

Especificar (descrever textualmente) as 20 (vinte) consultas que deseja efetuar no banco de dados (Conforme apresentada na entrega 1 do PjBL, caso houverem alterações, especificar quais foram). 
Implementar todas as intruções SELECT (consultas) para seleção para cada uma das extrações de informação definidas no projeto.

*/

-- Listar todos os clientes registrados no hotel;

SELECT nome AS "Clientes cadastrados"
FROM cliente
JOIN pessoa ON cliente.id_cliente = pessoa.id_pessoa;

-- Listar todos os animais que estão registrados no hotel;

SELECT nome 
-- Listar todos os funcionários registrados no hotel;
-- Permitir que os funcionários registrem reservas para a estadia de animais no hotel;
-- Registrar datas de check-in e checkout, serviços, tipo de acomodação;
-- Adicionar atributos para cada animal (nome, raça, idade…);
-- Registrar novos clientes; 
-- Listar os registros das reservas; 
-- Registrar informações de contato e endereço dos funcionários e clientes; 
-- Registrar novos funcionários; 
-- Permitir que funcionários tenham acesso aos dados de reservas do sistema; 
-- Permitir a atualização de dados dos animais; 
-- Permitir a atualização de dados dos funcionários; 
-- Permitir que os funcionários tenham acesso aos dados dos pets dos clientes; 
-- Permitir a atualização de dados dos clientes; 
-- Permitir a atualização de dados do endereço; 
-- Permitir que os funcionários tenham acesso aos dados de cobrança; 
-- Recuperar a data que o cliente foi cadastrado, para calcular quanto tempo a pessoa é nosso cliente. 


SELECT p.nome AS 'Funcionário', p.nascimento AS 'Aniversário'
FROM funcionario f
JOIN pessoa p ON f.id_funcionario = p.id_pessoa
WHERE MONTH(p.nascimento) = MONTH(CURDATE());