-- -----------------------------------------------------------------------------------
-- STORED PROCEDURES
-- -----------------------------------------------------------------------------------

-- Excluir registro de clientes e também seus dados pessoais
DELIMITER $$
CREATE PROCEDURE DeletarCliente(
    IN cliente_id INT
)
BEGIN
    DELETE FROM cliente WHERE id_cliente = cliente_id;
    DELETE FROM pessoa WHERE id_pessoa = cliente_id;
END//
DELIMITER ;
