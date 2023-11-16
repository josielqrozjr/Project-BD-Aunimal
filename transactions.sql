-- Linguagem de Transação de Dados (DQL - do inglês Data Transaction Language)

USE aunimal_hotel_pet;

-- primeira transação: commit
SET autocommit = FALSE;
START TRANSACTION;
SELECT * FROM clientes WHERE id > 7;
INSERT INTO servico (valor_total, descricao) VALUES (25, 'adestramento');
COMMIT;

-- segunda transação: commit
SET autocommit = FALSE;
START TRANSACTION;
DELETE FROM funcionario WHERE id = 7;
INSERT INTO funcionario (email, telefone) VALUES ('joaovitorjsjsjsj@gmail.com', 43998785532);
SET @pessoa_id := (SELECT LAST_INSERT_ID());
COMMIT;

-- terceira transação:commit
SET autocommit = FALSE;
START TRANSACTION;
UPDATE aunimal_hotel_pet.pessoa SET nome = 'Mariana Alves', email = 'mariana@gmail.com' WHERE pessoa.id_pessoa = '2';
INSERT INTO aunimal_hotel_pet.raca (classificacao) VALUES ('Corgi');
COMMIT;

-- quarta transação:commit
SET autocommit = FALSE;
START TRANSACTION;
SELECT * FROM aunimal_hotel_pet.pet WHERE id_pet < 6;
INSERT INTO aunimal_hotel_pet.pet (data_criacao, nome, peso, sexo, pelagem, porte, nascimento, descricao, id_especie, cliente_id)
VALUES (now(), 'Patolino', 47, 'M', 'Preta', 'M', '2020-06-10', 'Cachorro Fedido', 7, 13);
INSERT INTO aunimal_hotel_pet.servico (valor_total, descricao) VALUES ('550', 'Pet Táxi');
COMMIT;


-- primeira transação rollback
SET autocommit = FALSE;
START TRANSACTION;
SELECT reserva;
DELETE FROM reserva WHERE valor_total > 870;
ROLLBACK;

-- segunda transação: rollback
SET autocommit = FALSE;
START TRANSACTION;
INSERT INTO pet_servico (id_pet, id_servico) VALUES (90, 2);
UPDATE servico SET valor_total = valor_total - 2 WHERE servico.id = 3;
-- o erro aqui ocontece pois não existe cliente 13
ROLLBACK;

-- terceira transação: rollback
SET autocommit = FALSE;
START TRANSACTION;
UPDATE aunimal_hotel_pet.raca SET classificacao = 'Haski Siberiano' WHERE raca.id_raca = '8';
INSERT INTO aunimal_hotel_pet.forma (descricao) VALUES ('Fiado');
ROLLBACK;

-- quarta transação: rollback
SET autocommit = FALSE;
START TRANSACTION;
INSERT INTO aunimal_hotel_pet.especie (tipo, id_raca) VALUES ('CACHORRO', 3);
INSERT INTO aunimal_hotel_pet.raca (classificacao) VALUES ('Dálmata');
UPDATE aunimal_hotel_pet.pet SET nome = 'Marmaduke', pelagem = 'Laranja', sexo = 'M', peso = '23', descricao = 'Alto e magro'
WHERE pet.id_pet = 5;
ROLLBACK;


-- primeira transação back to savepoint
Use aunimal_hotel_pet;
SET autocommit = FALSE;
INSERT INTO raca (classificacao) VALUES ('Spitz');
SAVEPOINT add_client_funcio;
INSERT INTO pessoa (nome, cpf, sexo, nascimento, rg, email, est_civil, nacionalidade, data_criacao) VALUES ('Paula de Monteiro', '12345778765', 'F', '1995-10-04', '97123458703', 'pvp@pucpr.edu', 'SOLTEIRO', 'Brasil', now());
INSERT INTO cliente (id_cliente, data_criacao) VALUES (LAST_INSERT_ID(), NOW());
INSERT INTO funcionario (data_criacao, profissao, salario) VALUES (now(), 'tosador', 1300.00);
ROLLBACK TO SAVEPOINT add_client_funcio;
COMMIT;

-- segunda transação rollback to savepoint
SET autocommit = FALSE;
START TRANSACTION;
INSERT INTO aunimal_hotel_pet.contato (codigo_pais, codigo_area, numero, id_pessoa) VALUES (45, 13, 963228585, 2);
UPDATE aunimal_hotel_pet.servico set valor_total = 355 WHERE servico.id_servico = 6;
SAVEPOINT insert_update_contato;
INSERT INTO aunimal_hotel_pet.contato (codigo_pais, codigo_area, numero, id_pessoa) VALUES (55, 41, 998852635, 3);
ROLLBACK TO SAVEPOINT insert_update_contato;
COMMIT;
