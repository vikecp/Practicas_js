--- Pruebas
insert into Paises (Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico)
		values ('AR', 'Aargentina', 'ARG', NULL);

----violacion del tipo de dato cod_pais char(2)
INSERT INTO Paises (Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico)
		VALUES ('AUS','Australia',  'AUS',36)
---Anulacion de llave primaria
INSERT INTO Paises (Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico)
		VALUES (NULL,'Australia',  'AUS',36);

----- Duplicacion de la llave primaria
INSERT INTO Paises (Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico)
		VALUES ('AR','Australia',  'AUS',36)

--- Restrincion de longitud de la llave primaria, checar que siempre sea = 2 no < a 2
INSERT INTO Paises (Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico)
		VALUES ('A','Australia',  'AUS',36)

------ Que un campo sea unico/ violacion de llave unica UNIQUE CHECK cod_iso3 
INSERT INTO Paises (Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico)
		VALUES ('AUS','Australia',  'AUS',36);

---- se pueden insertar los registros en cualquier orden
INSERT INTO Paises (Cod_ISO3, Cod_Pais, Nombre,  Cod_Telefonico)
		VALUES ('AUS','AT','Australia',36)


------ ORDENAR COMO SE VERA, PORQUE LOS CONJUNTOS NO TIENEN ORDEN!
select * from Paises order by Nombre DESC

------------------------------------------------------------------------
------Otra forma de inserccion-------------------------

INSERT INTO Paises (Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico)
SELECT 'AUS','Australia',  'AUS',36;



-------------------------------------------------------------
-------- Transacion con diferentes instrucciones-------------
---- la ley del todo, o se ejecuatan todas o ninguna

BEGIN TRY
	BEGIN TRAN
		INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3) VALUES ('SV','El salvador','SLV');
		INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3) VALUES ('FI','Finlandia','FIN');
		INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3) VALUES ('FR','Francia','FRA');
		INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3) VALUES ('DE','Alemania','DEU');
		INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3) VALUES ('GT','Guatemala','GTM');
		INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3) VALUES ('HN','Honduras','HND');
		INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3) VALUES ('HU','Hungria','HUN');-----LLAVE PRIMARIA DUPLICADA
	COMMIT;
	PRINT 'TRANSACCION EXITOSA';
END TRY
BEGIN CATCH
	ROLLBACK;
	PRINT 'TRANSACCION FALLIDA';
END CATCH;

-----------------------Creamos unos estados

INSERT INTO Estados (Cod_Estado, Cod_Pais, Nombre) VALUES('UL','DE','BADEN');

INSERT INTO Estados (Cod_Estado, Cod_Pais, Nombre) VALUES('SW','GB','SOUTH WEST ENGLAND');

INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico) VALUES ('GB','GRAN BRETAÑA','GBR',44);

INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico) VALUES ('EU','ESTADOS UNIDOS','USA',1);


INSERT INTO Estados (Cod_Estado, Cod_Pais, Nombre) VALUES('WI','US','WISCONSIN');
INSERT INTO Estados (Cod_Estado, Cod_Pais, Nombre) VALUES('CA','US','CALIFORNIA');


-----ELIMINAR LA RESTRINCION DE COD_ESTADO NO SOLO SEA = 2

ALTER TABLE Estados
	DROP CONSTRAINT Len_Estado

INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico) VALUES ('VE','VENEZUELA','VEN',58);

INSERT INTO Estados (Cod_Estado, Cod_Pais, Nombre) VALUES('Y','VE','CARABOBO');

---- crear la nueva restrincion

------------------------------------------------------------
--------------ACTUALIZACION Y ELIMINACIONES EN CASCADA------

SELECT * FROM Estados WHERE Cod_Estado = 'Y'
SELECT * FROM Paises WHERE Cod_Pais = 'XX'

UPDATE Paises
SET Cod_Pais = 'XX' -----PONER EL VALOR XX EN EL CAMPO COD_PAIS
WHERE Cod_Pais = 'VE';


DELETE Paises
WHERE Cod_Pais = 'XX'

---------------------------------------INSERT DEPARTAMENTOOS

INSERT INTO Departamentos (Academia, Nombre, Director, Fec_Inicio)
VALUES  (1, 'BD', -1, '20150302'),
		(1, 'MATE', -1, '20150302'),
		(1, 'CIENCIAS', -1, '20150302'),
		(1, 'MODELADO', -1, '20150302');

ALTER TABLE Departamentos
DROP FK__Departame__Direc__4222D4EF

SELECT * FROM Departamentos

---- CREAR LA NUEVA RESTRINCION
ALTER TABLE Departamentos
	WITH NOCHECK
	ADD CONSTRAINT FK_Prof_Director
		FOREIGN KEY (Director)
		REFERENCES Profesores (Cod_Prof)
				ON UPDATE NO ACTION
				ON DELETE NO ACTION
