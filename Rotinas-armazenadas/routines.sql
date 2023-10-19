-- -----------------------------------------------------------------------------------
-- STORED PROCEDURES
-- -----------------------------------------------------------------------------------

-- Excluir registro de clientes e também seus dados pessoais
DELIMITER $$
CREATE PROCEDURE deletar_cliente(IN _cliente_id INT)
BEGIN
    DELETE FROM cliente WHERE id_cliente = _cliente_id;
    DELETE FROM pessoa WHERE id_pessoa = _cliente_id;
    DELETE FROM endereco WHERE id_endereco = _cliente_id;
    DELETE FROM contato WHERE id_contato = _cliente_id;
END $$
DELIMITER ;

-- Cadastrar novo cliente


-- -----------------------------------------------------------------------------------
-- STORED PROCEDURES
-- -----------------------------------------------------------------------------------

-- Exibir o dia do nascimento
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