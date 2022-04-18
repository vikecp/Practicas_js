--- Disparador(trigger):
--- Son objetos de la bd que se ejecutan automaticamente al Insertar, modificar, y/o eliminar 
--- datos de una tabla o vista

-- DML Trigger 

--- Ventajas :
---- Ejecutados automaticamente
---- seguridad
---- Auditoria
---- Manejo de errores
---- Reutilizar codigo
---- Encapsulamiento

---- Desventajas
-- los triggers forman parte de la metadata de la bd.


---Script para triggers

USE tempdb;

--Crear las tablas
CREATE TABLE Facturas (Factura INT, Cliente INT, Fecha DATETIME, Total Money DEfault (0));
CREATE TABLE Facturas_Detalles ( Factura INT, Detalle INT, Producto varchar(10), Total money);

--- Creacion del trigger
CREATE TRIGGER Detalles_Modificados
ON Facturas_Detalles
AFTER UPDATE, INSERT, DELETE
AS
BEGIN
	UPDATE	Facturas
	SET		Total = Total + Total_Detalles
	FROM	(
			SELECT Factura AS Fct, SUM(Total) AS Total_Detalles
			FROM	(
					SELECT Factura, Total FROM Inserted
					UNION ALL
					SELECT Factura , -Total  FROM Deleted
					) T
			GROUP BY Factura
			) A
	WHERE Factura = Fct;
END;


--- Comprobar si funciona el trigger

Select * from Facturas;
Select * from Facturas_Detalles;
--- Crear datos fcturas
insert into Facturas (Factura, Cliente, Fecha)
Values (1,10,'20171005'),
	   (2,15,'20171005');

--- Creacion de un detalle
insert into Facturas_Detalles (Factura, Detalle, Producto, Total) 
values (1,1,'bici roja', 100);

--- Creacion multiple detalle en la 1 factura
insert into Facturas_Detalles (Factura, Detalle, Producto, Total) 
values (2,1,'bici-azul',100),
	   (2,2, 'gafas',25),
	   (2,3, 'Guantes',25);


--- Creacion de detalles en diferentes facturas
insert into Facturas_Detalles (Factura, Detalle, Producto, Total) 
values (1,2,'bici-azul',150),
	   (1,3, 'gafas',25),
	   (1,4, 'Guantes',10);


--- Creacion de detalles en diferentes facturas

BEGIN TRANSACTION;
	INSERT INTO Facturas_Detalles (Factura, Detalle, Producto, Total) Values(2, 5, 'Rueda', 40)
	INSERT INTO Facturas_Detalles (Factura, Detalle, Producto, Total) Values(1, 4, 'Guantes', 25)
	INSERT INTO Facturas_Detalles (Factura, Detalle, Producto, Total) Values(2, 6, 'Bici-verde', 100);
	INSERT INTO Facturas_Detalles (Factura, Detalle, Producto, Total) Values(2, 4, 'Revistas', 10);
COMMIT;

Select * from Facturas;
Select * from Facturas_Detalles ORDER BY Factura, Detalle;

delete Facturas_Detalles where Detalle = 4;

---- Modificacion de detalles

UPDATE Facturas_Detalles
SET Total = 15
Where Producto='gafas';

update Facturas_Detalles
set Total = total * .9
Where Factura = 1 AND Detalle = 2;

--- eliminar
delete Facturas_Detalles where Producto='Bici-verde'





--- la importancia del all
ALTER TRIGGER Detalles_Modificados
ON Facturas_Detalles
AFTER UPDATE, INSERT, DELETE
AS
BEGIN
	UPDATE	Facturas
	SET		Total = Total + Total_Detalles
	FROM	(
			SELECT Factura AS Fct, SUM(Total) AS Total_Detalles
			FROM	(
					SELECT Factura, Total FROM Inserted
					UNION 
					SELECT Factura , -Total  FROM Deleted
					) T
			GROUP BY Factura
			) A
	WHERE Factura = Fct;
END;


--- eliminamos todos los datos de las tablas

TRUNCATE TABLE Facturas;
TRUNCATE TABLE Facturas_Detalles;

Select * from Facturas;
Select * from Facturas_Detalles ORDER BY Factura, Detalle;

--- crear todo de nuevo

--- Crear datos fcturas
insert into Facturas (Factura, Cliente, Fecha)
Values (1,10,'20171005'),
	   (2,15,'20171005');

--- Creacion de un detalle
insert into Facturas_Detalles (Factura, Detalle, Producto, Total) 
values (1,1,'bici-roja', 100);

--- Creacion multiple detalle en la 1 factura
insert into Facturas_Detalles (Factura, Detalle, Producto, Total) 
values (2,1,'Bici-roja',100),
	   (2,2, 'Gafas',25),
	   (2,3, 'Guantes',25);


--- Simular la tabla inserted
Create table insertados (Factura int, total money)
insert into insertados (Factura, total)
	values (2, 100),
		   (2,25),
		   (2,25);

select * from insertados

---- simular tabla deleted
Create table elimindados (Factura int, total money);
select * from elimindados;



--- hagamos limpieza

DROP TABLE Facturas, Facturas_Detalles, insertados, elimindados;