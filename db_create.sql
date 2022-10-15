DROP TABLE IF EXISTS phone CASCADE;
DROP TABLE IF EXISTS client CASCADE;
CREATE  TABLE IF NOT EXISTS client (id_client serial PRIMARY KEY, client_name varchar(40) not null, client_famil varchar(40) not null, client_email varchar(40));
CREATE  TABLE IF NOT EXISTS phone (id_phone serial PRIMARY KEY,	id_client serial REFERENCES client(id_client), phone_number varchar(40) not null);
DELETE FROM phone;	
DELETE FROM client;	
INSERT INTO client VALUES (DEFAULT,'Ivanov','Ivan','ivan@mail.ru'); --id, фамилия, имя, email
INSERT INTO client VALUES (DEFAULT,'Petrov','Petr','peter@mail.ru');
INSERT INTO client VALUES (DEFAULT,'Sidorov','Sidor','sidr@gmail.com');
INSERT INTO client VALUES (DEFAULT,'Kuznecov','Ivan','vanya@inet.gov');
INSERT INTO client VALUES (DEFAULT,'Gusev','Alexander','sasha82@mail.ru');
INSERT INTO client VALUES (DEFAULT,'Pushkin','Dmitriy','pds@mail.com');
INSERT INTO client VALUES (DEFAULT,'Hamidulin','Nikolay','nikolas@mail.ru');
INSERT INTO client VALUES (DEFAULT,'Koshelkov','Evgeniy','panda@mail.ru');
INSERT INTO client VALUES (DEFAULT,'Ivanov','Kostya');
INSERT INTO client VALUES (DEFAULT,'Ivanov2','Kostya2','test@test.by');
INSERT INTO phone VALUES (DEFAULT,1,'8999876'); --id, телефонный номе, id клиента
INSERT INTO phone VALUES (DEFAULT,2,'123456');
INSERT INTO phone VALUES (DEFAULT,4,'566776');
INSERT INTO phone VALUES (DEFAULT,5,'243');
INSERT INTO phone VALUES (DEFAULT,7,'542452');
INSERT INTO phone VALUES (DEFAULT,7,'6524526');
INSERT INTO phone VALUES (DEFAULT,7,'111111');
INSERT INTO phone VALUES (DEFAULT,9,'86');