use aunimal_hotel_pet;

-- -----------------------------------------------------------------------------------
-- STORED PROCEDURES
-- -----------------------------------------------------------------------------------

-- Excluir registro de reserva e os dados associados
DELIMITER $$
CREATE PROCEDURE deletar_reserva (IN _reserva_id INT)
BEGIN
    DELETE FROM cobranca_forma WHERE id_cobranca = _reserva_id;
    DELETE FROM cobranca WHERE id_reserva = _reserva_id;
	DELETE FROM pet_reserva WHERE id_reserva = _reserva_id;
	DELETE FROM reserva_servico WHERE id_reserva = _reserva_id;
	DELETE FROM reserva WHERE id_reserva = _reserva_id;
END $$
DELIMITER ;
-- (TESTE) CALL deletar_reserva(1);

-- Cadastrar novo funcionário e seus dados pessoais
DELIMITER %%
CREATE PROCEDURE formulario_admissao (
	IN p_nome VARCHAR(100),
	IN p_nascimento DATE,
    IN p_cpf CHAR(11),
    IN p_rg CHAR(11),
    IN p_sexo ENUM('M', 'F', 'NI'),
    IN p_email VARCHAR(50),
    IN p_est_civil ENUM('SOLTEIRO', 'CASADO', 'DIVORCIADO', 'SEPARADO', 'VIUVO'),
    IN p_nacionalidade VARCHAR(100),
    IN f_profissao VARCHAR(100),
    IN f_salario DECIMAL(10, 2),
    IN c_codigo_pais TINYINT,
    IN c_codigo_area TINYINT,
    IN c_numero BIGINT,
    IN e_cep CHAR(8),
    IN e_logradouro VARCHAR(50),
    IN e_numero SMALLINT UNSIGNED,
    IN e_bairro VARCHAR(50),
    IN e_cidade VARCHAR(100),
    IN e_estado VARCHAR(100))
BEGIN
    DECLARE pessoa_id INT;

    INSERT INTO pessoa
    VALUES (NULL, p_nome, p_nascimento, p_cpf, p_rg, p_sexo, p_email, p_est_civil, p_nacionalidade, NOW());

    -- Obter o último ID da pessoa cadastrada
    SET pessoa_id = LAST_INSERT_ID();

    INSERT INTO contato
    VALUES (c_codigo_pais, c_codigo_area, c_numero, pessoa_id);

    INSERT INTO endereco
    VALUES (NULL, NOW(), e_cep, e_logradouro, e_numero, e_bairro, e_cidade, e_estado, pessoa_id);

    INSERT INTO funcionario
    VALUES (pessoa_id, NOW(), f_profissao, f_salario);
END %%
DELIMITER ;

/* Para testar
CALL formulario_admissao
('Luciana Milão Rego', '1992-07-12', '78901234467', '78901201', 'F', 'luciana.milao@outlook.com', 'CASADO', 'Brasil',
'Assistente Administrativo', 1800.00,
89, 51, 345678901,
'80050010', 'Rua XV de Novembro', 79, 'Centro', 'Curitiba', 'PR');
*/

-- Atualizar todos os dados de um pet
DELIMITER ||
CREATE PROCEDURE atualizar_pet (
	IN _id_pet INT,
	IN _classificacao VARCHAR(100),
    IN _tipo ENUM('GATO','CACHORRO'),
    IN _nome VARCHAR(100),
    IN _peso DECIMAL(5,2),
    IN _sexo ENUM('M','F'),
    IN _pelagem VARCHAR(100),
    IN _porte ENUM('PP','P','M','G','GG'),
    IN _nascimento DATE,
    IN _descricao TINYTEXT,
    IN _id_especie INT)
BEGIN
	DECLARE analisar_pet INT;
    DECLARE analisar_especie INT;
    
	SELECT COUNT(*) INTO analisar_pet FROM pet WHERE id_pet = _id_pet;
    SELECT COUNT(*) INTO analisar_especie FROM especie WHERE id_especie = _id_especie;
    
	IF analisar_pet = 1 AND analisar_especie = 1 THEN
		UPDATE pet 
			SET nome = _nome,
				peso = _peso,
				sexo = _sexo,
				pelagem = _pelagem,
				porte = _porte,
				nascimento = _nascimento,
				descricao = _descricao,
                id_especie = _id_especie
		WHERE id_pet = _id_pet;
	ELSE 
    SELECT ('Pet não encontrado, verifique o ID!');
    END IF;
END ||
DELIMITER ;
-- (TESTE) CALL atualizar_pet(inserir);

-- -----------------------------------------------------------------------------------
-- FUNCTIONS
-- -----------------------------------------------------------------------------------

-- Exibir o dia do nascimento
-- (Prof. usei essa função, pois fui fazendo junto com o senhor no dia da aula e também por ter gostado muito)
DELIMITER ||
CREATE FUNCTION dia_nasc (_data DATE)
RETURNS VARCHAR(200) DETERMINISTIC

BEGIN
DECLARE dia_semana VARCHAR(200);

CASE DAYOFWEEK(_data)
WHEN 1 THEN SET dia_semana := "Domingo";
WHEN 2 THEN SET dia_semana := "Segunda";
WHEN 3 THEN SET dia_semana := "Terça";
WHEN 4 THEN SET dia_semana := "Quarta";
WHEN 5 THEN SET dia_semana := "Quinta";
WHEN 6 THEN SET dia_semana := "Sexta";
ELSE SET dia_semana := "Sábado";
END CASE;
RETURN dia_semana;

END ||
DELIMITER ;
-- (TESTE) SELECT dia_nasc('2000-11-13');

-- Faturamento total por serviço
DELIMITER ||
CREATE FUNCTION faturamento_servico (id_servico INT)
RETURNS DECIMAL(10,2) DETERMINISTIC
BEGIN
    
    RETURN (SELECT SUM(s.valor_total)
    FROM servico s
    JOIN reserva_servico rs ON s.id_servico = rs.id_servico
    WHERE s.id_servico = id_servico);
    
END ||
DELIMITER ;
-- (TESTE) SELECT faturamento_servico(6);

-- Exibir o resultado de uma busca pelo CPF e informar se é cliente ou funcionário
DELIMITER ||
CREATE FUNCTION busca_cpf(cpf_pessoa CHAR(11))
RETURNS VARCHAR(50) DETERMINISTIC
BEGIN
	DECLARE id_pessoa_ INT;
    DECLARE is_cliente INT; 
    DECLARE is_funcionario INT;
    SELECT id_pessoa INTO id_pessoa_ FROM pessoa WHERE cpf = cpf_pessoa;
    SELECT COUNT(id_cliente) INTO is_cliente FROM cliente WHERE id_cliente = id_pessoa_;
    SELECT COUNT(id_funcionario) INTO is_funcionario FROM funcionario WHERE id_funcionario = id_pessoa_;
    
    IF is_cliente = 1 AND is_funcionario = 1 THEN
		RETURN (SELECT ('Ambos'));
	
    ELSEIF is_cliente = 1 THEN
			RETURN (SELECT ('Cliente'));
            
	ELSEIF is_funcionario = 1 THEN
			RETURN (SELECT ('Funcionário'));
	
	ELSE 
    RETURN (SELECT ('Pessoa ainda não definida como cliente ou funcionário!'));
	END IF;
END ||
DELIMITER ;
-- (TESTE) SELECT busca_cpf('12345678910');

-- -----------------------------------------------------------------------------------
-- TRIGGERS
-- -----------------------------------------------------------------------------------

-- Adicionar data de criação de endereço
DELIMITER $$
CREATE TRIGGER add_data_endereco
BEFORE INSERT ON endereco
FOR EACH ROW
BEGIN 
	SET NEW.data_criacao = NOW();
END $$
DELIMITER ;

/* Para testar
INSERT INTO endereco (cep, logradouro, numero, bairro, cidade, estado, pessoa_id)
VALUES 
('50090060', 'Rua Marechal Deodoro', 234, 'Centro', 'Curitiba', 'PR', 7);
*/

-- Verificar se existe a pessoa antes de associar um contato a ela
DELIMITER %%
CREATE TRIGGER verificar_pessoa_ctt
BEFORE INSERT ON contato
FOR EACH ROW 
BEGIN
	DECLARE verificar_pessoa INT;
	SET verificar_pessoa = 
		(SELECT COUNT(*) 
		FROM pessoa pss
		WHERE pss.id_pessoa = NEW.id_pessoa);
	IF verificar_pessoa = 0 THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ID da pessoa não encontrado!';
	END IF ;
END %%
DELIMITER ;

/* Para testar
INSERT INTO contato
VALUES (55, 12, 133456789, 20);
*/

-- Verificar pet e serviço antes de adicionar em pet_servico
DELIMITER ||
CREATE TRIGGER verificar_pet_serv
BEFORE INSERT ON pet_servico
FOR EACH ROW
BEGIN
	DECLARE ver_pet INT;
    DECLARE ver_servico INT;
    
    SET ver_pet = 
		(SELECT COUNT(*) 
        FROM pet 
        WHERE id_pet = NEW.id_pet);
    SET ver_servico = 
		(SELECT COUNT(*) 
        FROM servico 
        WHERE id_servico = NEW.id_servico);
    
    IF ver_pet = 0 OR ver_servico = 0 THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ID pet ou serviço não encontrado!';
    END IF;
END ||
DELIMITER ;

/* Para testar
INSERT INTO pet_servico (id_pet, id_servico)
VALUES 
(4, 33);
*/