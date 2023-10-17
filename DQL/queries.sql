/* Linguagem de Consulta de Dados (DQL - do inglês Data Query Language):

Especificar (descrever textualmente) as 20 (vinte) consultas que deseja efetuar no banco de dados (Conforme apresentada na entrega 1 do PjBL, caso houverem alterações, especificar quais foram). 
Implementar todas as intruções SELECT (consultas) para seleção para cada uma das extrações de informação definidas no projeto.

*/

USE aunimal_hotel_pet;

-- -----------------------------------------------------------------------------------
-- Listar todos os clientes registrados no hotel;
-- -----------------------------------------------------------------------------------

SELECT id_cliente AS "ID", nome AS "Clientes"
FROM cliente cl
JOIN pessoa pss ON cl.id_cliente = pss.id_pessoa
ORDER BY pss.nome;


-- -----------------------------------------------------------------------------------
-- Listar todos os animais que estão registrados no hotel;
-- Obs.: Listamos os pets que no momento possuem vínculo ativo com alguma reserva.
-- -----------------------------------------------------------------------------------

SELECT pet.nome AS "Animais"
FROM pet
JOIN pet_reserva pr
ON pet.id_pet = pr.id_pet;


-- -----------------------------------------------------------------------------------
-- Listar todos os funcionários registrados no hotel;
-- -----------------------------------------------------------------------------------

SELECT nome AS "Funcionários"
FROM funcionario
JOIN pessoa
ON id_funcionario = id_pessoa
ORDER BY nome;

-- -----------------------------------------------------------------------------------
-- Permitir que os funcionários registrem reservas para a estadia de animais no hotel;
-- -----------------------------------------------------------------------------------



-- -----------------------------------------------------------------------------------
-- Registrar datas de check-in e checkout, serviços, tipo de acomodação;
-- -----------------------------------------------------------------------------------



-- -----------------------------------------------------------------------------------
-- Adicionar atributos para cada animal (nome, raça, idade…);
-- -----------------------------------------------------------------------------------



-- -----------------------------------------------------------------------------------
-- Registrar novos clientes;
-- -----------------------------------------------------------------------------------

-- Caso não seja cadastrado:

INSERT INTO pessoa (nome, nascimento, cpf, rg, sexo, email, est_civil, nacionalidade, data_criacao)
VALUES
('Maria Oliveira', '2000-10-20', '23446789012', '8765432', 'F', 'maria.oliveira@outlook.com', 'VIUVO', 'Brasil', NOW());

-- Caso já possua os dados pessoais cadastrados:



-- -----------------------------------------------------------------------------------
-- Listar os registros das reservas; 
-- -----------------------------------------------------------------------------------


-- -----------------------------------------------------------------------------------
-- Registrar informações de contato e endereço dos funcionários e clientes; 
-- -----------------------------------------------------------------------------------



-- -----------------------------------------------------------------------------------
-- Registrar novos funcionários;
-- -----------------------------------------------------------------------------------

INSERT INTO pessoa (nome, nascimento, cpf, rg, sexo, email, est_civil, nacionalidade, data_criacao) 
VALUES ('Nome Funcionário', 'YYYY-MM-DD', 'CPF', 'RG', 'M', 'email@example.com', 'SOLTEIRO', 'Brasil', 'YYYY-MM-DD HH:MM:SS');

INSERT INTO funcionario (id_funcionario, data_criacao, profissao, salario) 
VALUES (LAST_INSERT_ID(), 'YYYY-MM-DD HH:MM:SS', 'Profissão', Salario);


-- -----------------------------------------------------------------------------------
-- Permitir que funcionários tenham acesso aos dados de reservas do sistema;
-- Obs.: Estamos substituindo por criar uma view com os aniersariantes do mês atual.
-- -----------------------------------------------------------------------------------

CREATE VIEW f_aniversiante AS
SELECT p.nome AS 'Funcionário', p.nascimento AS 'Aniversário'
FROM funcionario f
JOIN pessoa p ON f.id_funcionario = p.id_pessoa
WHERE MONTH(p.nascimento) = MONTH(CURDATE());

SELECT * FROM f_aniversiante;

-- -----------------------------------------------------------------------------------
-- Permitir a atualização de dados dos animais;
-- -----------------------------------------------------------------------------------



-- -----------------------------------------------------------------------------------
-- Permitir a atualização de dados dos funcionários;
-- -----------------------------------------------------------------------------------



-- -----------------------------------------------------------------------------------
-- Permitir que os funcionários tenham acesso aos dados dos pets dos clientes;
-- -----------------------------------------------------------------------------------



-- -----------------------------------------------------------------------------------
-- Permitir a atualização de dados dos clientes;
-- -----------------------------------------------------------------------------------



-- -----------------------------------------------------------------------------------
-- Permitir a atualização de dados do endereço;
-- -----------------------------------------------------------------------------------



-- -----------------------------------------------------------------------------------
-- Permitir que os funcionários tenham acesso aos dados de cobrança;
-- -----------------------------------------------------------------------------------



-- -----------------------------------------------------------------------------------
-- Recuperar a data que o cliente foi cadastrado, para calcular quanto tempo a pessoa é nosso cliente.
-- -----------------------------------------------------------------------------------

