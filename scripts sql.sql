create database estoquev2;

use estoquev2;

create table PRODUTO(ID_PRODUTO INTEGER PRIMARY KEY AUTO_INCREMENT,DESCRICAO VARCHAR (50)NOT NULL,
                    TIPO VARCHAR(50)NOT NULL,FORNECEDOR VARCHAR(50) NOT NULL,ESTOQ_MIN INTEGER,ESTOQ_INI INTEGER,
                    ESTOQ_ATUAL INTEGER);
                    
show tables;

select * from PRODUTO;

insert into PRODUTO values ('TESTE','TESTE','TESTE',1,1,1);

drop table PRODUTO;