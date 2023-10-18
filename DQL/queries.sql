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

SELECT pet.nome AS "Nome", raca.classificacao AS "Raça", especie.tipo AS "Espécie"
FROM raca
LEFT JOIN especie ON raca.id_raca = especie.id_raca
LEFT JOIN pet ON especie.id_especie = pet.id_especie;

-- -----------------------------------------------------------------------------------
-- Listar todos os funcionários registrados no hotel;
-- -----------------------------------------------------------------------------------

SELECT pss.nome AS "Funcionários", f.profissao AS "Profissão", f.id_funcionario AS "ID"
FROM funcionario f
JOIN pessoa pss
ON f.id_funcionario = pss.id_pessoa
ORDER BY pss.nome;

-- -----------------------------------------------------------------------------------
-- Permitir que os funcionários registrem reservas para a estadia de animais no hotel;
-- -----------------------------------------------------------------------------------

INSERT INTO reserva (check_in, checkout, descricao, valor_total, id_cliente, id_funcionario)
VALUES ('2024-01-28 14:00:00', '2024-02-15 12:00:00', 'Reserva para carnaval', 2700.00, 1, 10);

-- -----------------------------------------------------------------------------------
-- Registrar datas de check-in e checkout, serviços, tipo de acomodação;
-- -----------------------------------------------------------------------------------

INSERT INTO reserva (check_in, checkout, descricao, valor_total, id_cliente, id_funcionario)
VALUES ('2023-10-18 14:00:00', '2023-10-23 12:00:00', 'Reserva para aniversário', 1500.00, 1, 10);
INSERT INTO servico (valor_total, descricao)
VALUES (700.00, 'Festa Aunimal');
INSERT INTO reserva_servico (id_reserva, id_servico)
VALUES (7, 7);

-- -----------------------------------------------------------------------------------
-- Adicionar atributos para cada animal (nome, raça, idade…);
-- -----------------------------------------------------------------------------------

INSERT INTO raca (classificacao) VALUES ('Labrador Retriever');
INSERT INTO especie (tipo, id_raca) VALUES ('CACHORRO', 7);
INSERT INTO pet (data_criacao, nome, peso, sexo, pelagem, porte, nascimento, descricao, id_especie, cliente_id)
VALUES (NOW(), 'Pong', 25.5, 'M', 'Curta', 'M', '2020-10-10', 'Cachorro amigável', 7, 3);

-- -----------------------------------------------------------------------------------
-- Registrar novos clientes;
-- -----------------------------------------------------------------------------------

-- Caso não seja cadastrado:
INSERT INTO pessoa (nome, nascimento, cpf, rg, sexo, email, est_civil, nacionalidade, data_criacao)
VALUES
('Maria Oliveira', '2000-10-20', '23446789012', '8765432', 'F', 'maria.oliveira@outlook.com', 'VIUVO', 'Brasil', NOW());

INSERT INTO cliente VALUES (13, NOW());

-- Caso já possua os dados pessoais cadastrados:
INSERT INTO cliente VALUES (7, NOW());

-- -----------------------------------------------------------------------------------
-- Listar os registros das reservas;
-- Obs.: Trocaremos os ids de cliente e funcionário para o respectivos nomes das pessoas.
-- -----------------------------------------------------------------------------------

SELECT r.id_reserva, r.check_in, r.checkout, r.descricao, r.valor_total, 
cl.nome AS "Cliente", 
func.nome AS "Reservado por:"
FROM reserva r
JOIN pessoa cl ON r.id_cliente = cl.id_pessoa
JOIN pessoa func ON r.id_funcionario = func.id_pessoa;

-- -----------------------------------------------------------------------------------
-- Registrar informações de contato e endereço dos funcionários e clientes;
-- Obs.: Vamos substituir o "Registrar" por "Listar".
-- -----------------------------------------------------------------------------------

-- Listar quantidade de clientes que possuem o mesmo DDD 
SELECT c.codigo_area "DDD", COUNT(*) AS "Quantidade"
FROM cliente cli
JOIN contato c ON cli.id_cliente = c.id_cliente
GROUP BY c.codigo_area
ORDER BY COUNT(*);

-- Listar os bairros com no mínimo dois funcionários
SELECT e.bairro, COUNT(*) AS Quantidade
FROM endereco e
JOIN pessoa p ON e.pessoa_id = p.id_pessoa
LEFT JOIN funcionario f ON p.id_pessoa = f.id_funcionario
GROUP BY e.bairro
HAVING Quantidade >= 2
ORDER BY e.bairro;

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

UPDATE cliente
SET data_criacao = '2022-11-13 10:29:04' 
WHERE id_cliente = 7;

-- -----------------------------------------------------------------------------------
-- Permitir a atualização de dados do endereço;
-- -----------------------------------------------------------------------------------

UPDATE endereco 
SET numero = numero +  1, cep = cep + 2 
WHERE id_endereco <= 3;

-- -----------------------------------------------------------------------------------
-- Permitir que os funcionários tenham acesso aos dados de cobrança;
-- Obs.: Listaremos as cobranças que possuem valor abaixo da média
-- -----------------------------------------------------------------------------------

SELECT valor_total "Valor", data_cobranca "Data", id_cobranca, id_reserva
FROM cobranca
GROUP BY id_cobranca
HAVING valor_total < (SELECT AVG(valor_total) FROM cobranca)
ORDER BY valor_total DESC;

-- -----------------------------------------------------------------------------------
-- Recuperar a data que o cliente foi cadastrado para calcular quanto tempo a pessoa é nosso cliente.
-- -----------------------------------------------------------------------------------

SELECT 
cl.id_cliente "ID",
pss.nome, 
cl.data_criacao "Criação", 
DATEDIFF(CURDATE(), cl.data_criacao) AS "Tempo (dias)"
FROM cliente cl
JOIN pessoa pss
ON pss.id_pessoa = cl.id_cliente
ORDER BY cl.data_criacao DESC, cl.id_cliente;

-- -----------------------------------------------------------------------------------
-- VIEWS
-- -----------------------------------------------------------------------------------

-- Exibir os animais que cada cliente possui
CREATE VIEW animal_cliente AS
SELECT pss.nome AS "Cliente", p.nome AS "Pet", r.classificacao AS "Raça"
FROM cliente c
LEFT JOIN pessoa pss ON c.id_cliente = pss.id_pessoa
LEFT JOIN pet p ON pss.id_pessoa = p.cliente_id
LEFT JOIN especie e ON p.id_especie = e.id_especie
LEFT JOIN raca r ON e.id_raca = r.id_raca
ORDER BY pss.nome;

SELECT * FROM animal_cliente;

-- Exibir os funcionários aniversariantes do mês atual
CREATE VIEW f_aniversiante AS
SELECT p.nome AS 'Funcionário', p.nascimento AS 'Aniversário'
FROM funcionario f
JOIN pessoa p ON f.id_funcionario = p.id_pessoa
WHERE MONTH(p.nascimento) = MONTH(CURDATE());

SELECT * FROM f_aniversiante;
