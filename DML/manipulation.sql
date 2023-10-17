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
(3200.00, '2023-12-05 18:00:00', '2023-12-01', 12);

SELECT * from pagamento;







-- -----------------------------------------------------------------------------------      
-- Criar 5 instruções de atualização de registros em diferentes tabelas.
-- -----------------------------------------------------------------------------------


-- -----------------------------------------------------------------------------------
-- Criar 5 instruções de exclusão de registros em diferentes tabelas.
-- -----------------------------------------------------------------------------------
