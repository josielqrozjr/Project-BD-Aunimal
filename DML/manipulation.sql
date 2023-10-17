/* Linguagem de Manipulação de Dados (DML - do inglês Data Manipulation Language):*/

USE aunimal_hotel_pet;


-- -----------------------------------------------------------------------------------
-- Inserir ao menos 6 registros em cada uma das tabelas do banco de dados.
-- -----------------------------------------------------------------------------------

INSERT INTO pessoa (nome, nascimento, cpf, rg, sexo, email, est_civil, nacionalidade, data_criacao)
VALUES 
('Ana Souza Luz Wosche', '1992-07-12', '78901234567', '78901234501', 'F', 'ana.souza@gmail.com', 'SEPARADO', 'Brasil', NOW()),
('Lucas Gabriel Oliveira', '1998-04-25', '89012345678', '89012345602', 'M', 'lucas.oliveira@gmail.com', 'DIVORCIADO', 'Brasil', NOW()),
('Camila Silva Sobrinho', '1997-09-03', '90123456789', '90123456703', 'F', 'camila.sobrinho@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('Fernando Rodrigo Pereira', '1984-11-30', '12345678909', '12345878904', 'M', 'fernando.rodrigo@gmail.com', 'CASADO', 'Brasil', NOW()),
('Larissa Santos Flow', '1990-03-15', '23456789098', '23456789005', 'F', 'larissa.flow@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('Ricardo Lima de Sousa', '1986-01-08', '34567890187', '34567890106', 'M', 'ricardo.lima@gmail.com', 'CASADO', 'Brasil', NOW()),
('Josiel Queiroz Júnior', '1994-05-15', '12345678910', '12345978907', 'M', 'josiel.queiroz@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('Rafaela Vecchi Pelentier', '1996-08-20', '23456789012', '23456789008', 'F', 'rafaela.vecchi@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('João Vitor de Lima Antunes', '1998-03-10', '34567890123', '34567890109', 'M', 'joao.antunes@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('Ana Pereira Dias', '1995-11-18', '45678901234', '45678901210', 'F', 'ana.dias@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('Roberto Loures Raposo', '1988-09-05', '56789012345', '56789012311', 'M', 'roberto.raposo@gmail.com', 'CASADO', 'Brasil', NOW()),
('Juliana Mascarenhas Soares', '1989-12-30', '67890123456', '67890123412', 'F', 'juliana.mascarenhas@gmail.com', 'VIUVO', 'Brasil', NOW());

INSERT INTO cliente (id_cliente, data_criacao)
VALUES (1, NOW()), (2, NOW()), (3, NOW()), (4, NOW()), (5, NOW()), (6, NOW());

INSERT INTO funcionario (id_funcionario, data_criacao, profissao, salario)
VALUES
(6, NOW(), 'Treinador', 2500.00),
(7, NOW(), 'CEO', 8500.00),
(8, NOW(), 'CEO', 8500.00),
(9, NOW(), 'CEO', 8500.00),
(10, NOW(), 'Analista Administrativo', 2200.00),
(11, NOW(), 'Cuidador', 2860.00),
(12, NOW(), 'Médico veterinário', 3200.00);
       
       
INSERT INTO reserva (check_in, checkout, descricao, valor_total, id_cliente, id_funcionario)
VALUES 
('2023-10-20 12:00:00', '2023-10-25 10:00:00', 'Reserva para férias', 500.00, 1, 10),
('2023-11-05 14:00:00', '2023-11-10 11:00:00', 'Reserva para viagem de negócios', 600.00, 2, 10),
('2023-11-15 10:00:00', '2023-11-20 09:00:00', 'Reserva para evento especial', 700.00, 3, 10),
('2023-12-01 15:00:00', '2023-12-06 13:00:00', 'Reserva para feriado', 550.00, 4, 10),
('2023-12-10 11:00:00', '2023-12-15 08:00:00', 'Reserva para fim de semana', 450.00, 5, 10),
('2023-12-20 16:00:00', '2023-12-28 12:00:00', 'Reserva para Natal', 880.00, 6, 10);

INSERT INTO cobranca (data_cobranca, valor_total, id_reserva, id_funcionario)
VALUES 
('2023-10-26 14:00:00', 500.00, 1, 10),
('2023-11-11 12:00:00', 600.00, 2, 7),
('2023-11-21 09:00:00', 700.00, 3, 10),
('2023-12-07 16:00:00', 550.00, 4, 8),
('2023-12-16 10:00:00', 450.00, 5, 9),
('2024-01-02 18:00:00', 880.00, 6, 10);

INSERT INTO forma (descricao) 
VALUES 
('Cartão de Crédito'), 
('Cartão de Débito'), 
('Dinheiro'), 
('Transferência Bancária'), 
('PIX'), 
('Boleto');

INSERT INTO raca (classificacao) 
VALUES ('Persa'), ('Siamês'), ('Poodle'), ('Bulldog'), ('Golden Retriever'), ('Maine Coon');

INSERT INTO especie (tipo, id_raca) 
VALUES ('GATO', 1), ('GATO', 2), ('CACHORRO', 3), ('CACHORRO', 4), ('CACHORRO', 5), ('GATO', 6);

INSERT INTO pet (data_criacao, nome, peso, sexo, pelagem, porte, nascimento, descricao, id_especie, cliente_id)
VALUES 
(NOW(), 'Tom', 4.5, 'M', 'Cinza', 'M', '2019-02-14', 'Gato adorável', 1, 1),
(NOW(), 'Luna', 3.2, 'F', 'Preto', 'P', '2020-06-05', 'Gata curiosa', 2, 2),
(NOW(), 'Max', 8.0, 'M', 'Branco', 'G', '2017-12-18', 'Cachorro brincalhão', 3, 3),
(NOW(), 'Bella', 5.5, 'F', 'Marrom', 'M', '2018-08-22', 'Cachorra dócil', 4, 4),
(NOW(), 'Loki', 7.8, 'M', 'Amarelo', 'G', '2016-05-10', 'Cachorro amigável', 5, 5),
(NOW(), 'Lilo', 6.3, 'M', 'Tricolor', 'M', '2017-09-03', 'Gato brincalhão', 6, 6);

INSERT INTO servico (valor_total, descricao) 
VALUES 
(100.00, 'Banho e Tosa'), 
(30.00, 'Passeio Diário'), 
(35.00, 'Hospedagem Padrão'), 
(60.00, 'Hospedagem VIP'), 
(90.00, 'Treinamento Comportamental'), 
(180.00, 'Consulta Veterinária');

INSERT INTO pagamento (valor, data_pagamento, mes_referencia, id_funcionario)
VALUES 
(2500.00, '2023-10-05 14:00:00', '2023-10-01', 6),
(8700.00, '2023-11-05 12:00:00', '2023-11-01', 7),
(8800.00, '2023-11-05 09:00:00', '2023-11-01', 8),
(8800.00, '2023-12-05 16:00:00', '2023-12-01', 9),
(2800.00, '2023-12-05 10:00:00', '2023-12-01', 10),
(2860.00, '2023-12-05 18:00:00', '2023-12-01', 11),
(3200.00, '2023-12-05 18:00:00', '2023-12-01', 12),
(3230.00, '2023-12-05 18:00:00', '2023-12-01', 12);

INSERT INTO endereco (data_criacao, cep, logradouro, numero, bairro, cidade, estado, pessoa_id)
VALUES 
(NOW(), '80090060', 'Rua Marechal Deodoro', 234, 'Centro', 'Curitiba', 'PR', 1),
(NOW(), '80100050', 'Avenida República Argentina', 567, 'Água Verde', 'Curitiba', 'PR', 2),
(NOW(), '80110040', 'Rua Chile', 890, 'Rebouças', 'Curitiba', 'PR', 3),
(NOW(), '80120030', 'Avenida Iguaçu', 111, 'Água Verde', 'Curitiba', 'PR', 4),
(NOW(), '80130020', 'Rua Nilo Peçanha', 222, 'Bacacheri', 'Curitiba', 'PR', 5),
(NOW(), '80020040', 'Rua das Flores', 123, 'Centro', 'Curitiba', 'PR', 6),
(NOW(), '80030030', 'Avenida Sete de Setembro', 456, 'Batel', 'Curitiba', 'PR', 7),
(NOW(), '80040020', 'Rua Comendador Araújo', 789, 'Centro', 'Curitiba', 'PR', 8),
(NOW(), '80050010', 'Rua XV de Novembro', 101, 'Centro', 'Curitiba', 'PR', 9),
(NOW(), '80060000', 'Rua Visconde de Nácar', 112, 'Centro', 'Curitiba', 'PR', 10),
(NOW(), '80080070', 'Avenida Silva Jardim', 123, 'Batel', 'Curitiba', 'PR', 11),
(NOW(), '80070090', 'Avenida João Gualberto', 131, 'Alto da Glória', 'Curitiba', 'PR', 12);

INSERT INTO contato (codigo_pais, codigo_area, numero, id_cliente)
VALUES 
(55, 11, 123456789, 1),
(55, 41, 234567890, 2),
(55, 51, 345678901, 3),
(55, 41, 456789012, 4),
(55, 41, 567890123, 5),
(55, 41, 678901234, 6),
(55, 94, 789012345, 7),
(55, 41, 890123456, 8),
(55, 41, 901234567, 9),
(55, 93, 112233445, 10),
(55, 12, 223344556, 11),
(55, 41, 334455667, 12);

INSERT INTO cobranca_forma (valor, parcela, id_cobranca, id_forma)
VALUES 
(500.00, 'À vista', 1, 1),
(600.00, 'À vista', 2, 2),
(700.00, 'À vista', 3, 3),
(550.00, 'À vista', 4, 4),
(450.00, 'À vista', 5, 5),
(880.00, 'À vista', 6, 6);

INSERT INTO funcionario_servico (id_funcionario, id_servico)
VALUES 
(11, 1),
(6, 2),
(11, 3),
(11, 4),
(6, 5),
(12, 6);

INSERT INTO pet_servico (id_pet, id_servico)
VALUES 
(1, 1), (1, 6),
(2, 2), (2, 5),
(3, 3), (3, 4),
(4, 4), (4, 2),
(5, 5), (5, 2),
(6, 6), (6, 1);

INSERT INTO pet_reserva (id_pet, id_reserva)
VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6);

INSERT INTO reserva_servico (id_reserva, id_servico)
VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6);


-- -----------------------------------------------------------------------------------      
-- Criar 5 instruções de atualização de registros em diferentes tabelas.
-- -----------------------------------------------------------------------------------

UPDATE funcionario
SET profissao = 'Gerente Administrativo', salario = 3990.00
WHERE id_funcionario = 10;

UPDATE contato
SET numero = 987654321
WHERE id_cliente = 7;

UPDATE pagamento
SET mes_referencia = '2023-11-01'
WHERE id_funcionario = 9;

UPDATE servico
SET descricao = 'Hospedagem Promocional'
WHERE id_servico = 3;

UPDATE pessoa
SET est_civil = 'CASADO'
WHERE id_pessoa = 2;


-- -----------------------------------------------------------------------------------
-- Criar 5 instruções de exclusão de registros em diferentes tabelas.
-- -----------------------------------------------------------------------------------

DELETE FROM endereco WHERE pessoa_id = 1;
DELETE FROM contato WHERE id_cliente = 2;
DELETE FROM pagamento WHERE id_funcionario = 3;
DELETE FROM servico WHERE id_servico = 8;
DELETE FROM funcionario_servico WHERE id_funcionario = 11;