-------------------------
-- Creacion de la bd --
-------------------------
CREATE DATABASE Academia;

-- Usar la bd --

USE Academia;

--- Crear tabla de paises ---

CREATE TABLE Paises
(
Cod_Pais char(2) PRIMARY KEY CHECK (LEN(Cod_Pais)=2),
Nombre varchar(50) NOT NULL,
Cod_ISO3 char(3) NOT NULL UNIQUE CHECK (LEN(Cod_ISO3)=3),
Cod_Telefonico smallint
);

-- Crear tabla estados ----

CREATE TABLE Estados
(
Cod_Estado char(2) PRIMARY KEY,
-- Creamos la restrincion como un objeto separado y le damos nombre
CONSTRAINT Len_Estado CHECK (LEN(Cod_Estado)=2),
Cod_Pais char(2) FOREIGN KEY REFERENCES Paises (Cod_Pais)
				 ON UPDATE CASCADE
				 ON DELETE CASCADE,
Nombre varchar(50) NOT NULL,
Cod_Telefonico smallint
);


--- Create table academias ----

CREATE TABLE Academias
(
Cod_Acad tinyint IDENTITY (1,1) PRIMARY KEY,
Nombre varchar(50) NOT NULL,
Fec_Fundacion DATE NOT null,
Numero varchar(10) NOT NULL,
Calle varchar(30) NOT NULL,
Ciudad varchar(30) NOT NULL,
Estado char(2) NULL
----Sideseamos agregar un nombre
	CONSTRAINT FK_Academias_Estados FOREIGN KEY
									REFERENCES Estados (Cod_Estado)
										ON UPDATE CASCADE
										ON DELETE SET NULL,
Cod_Postal varchar(10)
);


--- Tabla profesores
CREATE TABLE Profesores
(
Cod_Prof smallint IDENTITY (1,1) PRIMARY KEY,
SSN varchar(11) UNIQUE CHECK (LEN(SSN)=11),
Nombre varchar(30) NOT NULL,
APellido varchar(30) NOT NULL,
Numero varchar(30) NOT NULL,
Calle varchar(30) NOT NULL,
Ciudad varchar(30) NOT NULL,
Estado char(2) FOREIGN KEY REFERENCES Estados (Cod_Estado)
							ON UPDATE CASCADE
							ON DELETE SET NULL,
Cod_Postal varchar(10) NOT NULL,
Telefono varchar(15),
Sueldo money DEFAULT (0)
);


--- Tabla de departamentos

CREATE TABLE Departamentos
(
Cod_Dpto Smallint IDENTITY (1,1) PRIMARY KEY,
Academia tinyint NOT NULL
		    FOREIGN KEY REFERENCES Academias (Cod_Acad)
			    ON UPDATE CASCADE
			    ON DELETE CASCADE,
Nombre varchar(30) NOT NULL,
Director smallint NOT NULL DEFAULT (-1)
			FOREIGN KEY REFERENCES Profesores (Cod_Prof)
				ON UPDATE NO ACTION
				ON DELETE NO ACTION,
Fec_Inicio DATE NOT NULL
);


--- Tabla de relacion entre departamentos y profesores
-- Eliminamos los eventos en cascada
CREATE TABLE Dptos_Profesores
(
Cod_Dpto smallint NOT NULL
	FOREIGN KEY REFERENCES Departamentos (Cod_Dpto),
Cod_Prof Smallint NOT NULL
	FOREIGN KEY REFERENCES Profesores (Cod_Prof)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-------------------------------------------
----  Tabla de materias sin la  restrinccion
------------------------------------------
CREATE TABLE Materias
(
Cod_Materia smallint IDENTITY (1,1) PRIMARY KEY,
Nombre varchar(30) NOT NULL,
Electiva bit NOT NULL Default (0),
Peso tinyint NOT NULL default (1) Check (Peso > 0)
);

--- crear la restrincion pero a nivel de la tabla y no del campo peso.
alter table Materias
add constraint CheckPesoMateria
	check (Peso <= (case Electiva when 0 then 6 else 2 end));




----------------------------------------
----- Tabla cursos
---------------------------------------

CREATE TABLE Cursos
(
Cod_Curso int IDENTITY (1,1) PRIMARY KEY,
Cod_Prof smallint
	FOREIGN KEY REFERENCES Profesores (Cod_Prof)
		ON DELETE SET NULL,
Cod_Materia Smallint
	FOREIGN KEY REFERENCES Materias (Cod_Materia)
		ON DELETE CASCADE,
Aula int not null,
Hora_Inicio time Not null,
Hora_Fin time not null,
Duracion_Mins AS (DATEDIFF(MINUTE, Hora_Inicio, Hora_Fin))
--- no se define el tipo de dato
);


--------- RESTRINCCION A NIVEL DE LA TABLA

ALTER TABLE  Cursos
ADD CONSTRAINT CheckHoras
	Check(Hora_Inicio < Hora_Fin);


ALTER TABLE  Cursos
	 ADD Activo BIT NOT NULL Default(1);


--------------------------------------------------
----- Funcion para checar si una aula esta ocupada ------
--------------------------------------------------
CREATE FUNCTION fn_Aula_Ocupada
(
	--- PArametros
	@ID INT,
	@Aula INT,
	@Inicio Time,
	@Fin time
)
RETURNS bit ---la funcion retornara 0 / 1
AS
BEGIN
	DECLARE @AulaOCupada BIT = 0; ---se asume de una vez que la aula no esta ocupada
	--- EXists devulve 0 si el conjunto es vacio y 1 si almenos hay 1 elemnto

	IF EXISTS	(
				SELECT *
				FROM Cursos
				WHERE Cod_Curso <> @ID AND
				Aula = @Aula AND
				Activo = 1 AND
				(
					@Inicio BETWEEN Hora_Inicio AND Hora_Fin OR
					@Fin BETWEEN Hora_Inicio AND Hora_Fin OR
					(@Inicio <= Hora_Inicio AND @Fin >= Hora_Fin)
				)
	)
	SET @AulaOCupada = 1;

RETURN @AulaOcupada;
END;

------------------------------------------------------
-----Creamos la restrincion 
-----Solo se pueden crear cursos, si el aula esta disponible
---------------------------------------------------------

ALTER TABLE Cursos
 ADD CONSTRAINT CheckAulaOcupada
	CHECK (dbo.fn_Aula_Ocupada (Cod_Curso, Aula, Hora_Inicio, Hora_Fin)=0);


-------------------------------------------------------
----- libros-----
------------------------------------------------------
CREATE TABLE Libros
(
Cod_libro int IDENTITY (1,1) PRIMARY KEY,
ISBN char(13) NOT NULL UNIQUE CHECK (LEN(ISBN)=13 AND ISNUMERIC(ISBN)=1),
Titulo varchar(100) NOT NULL,
Autor varchar(100) NOT NULL,
Año Smallint,
Edicion char(3),
Editorial varchar(100),
Paginas smallint
);

----Tabla de Relacion Cursos y libros
create table Cursos_libros
(
Cod_Curso int not null
		foreign key references Cursos (Cod_Curso)
			on update cascade
			on delete cascade,
Cod_libro int not null
		foreign key references Libros (Cod_libro)
			on update cascade
			on delete cascade
);
------------------------------------------------------
------Tabla de alumnos--------------------------------
------------------------------------------------------

CREATE TABLE Alumnos
(
Cod_Alumno int IDENTITY (1,1) PRIMARY KEY,
SSN varchar(11) UNIQUE CHECK (LEN(SSN)=11),
Nombre varchar(30) NOT NULL,
Apellido varchar(30) NOT NULL,
Numero varchar(10) NOT NULL,
Calle varchar(30) NOT NULL,
Ciudad varchar(30) NOT NULL,
Estado char(2) FOREIGN KEY REFERENCES Estados (Cod_Estado)
					ON UPDATE CASCADE
					ON DELETE SET NULL,
Cod_Postal varchar(10) NOT NULL,
Telefono varchar(10),
Fecha_Nac Date,
Lugar_Nac varchar(50)
);

------------------------------------------------------
------La relacion Tabla de alumnos con Cursos---------
------------------------------------------------------

create table Cursos_Alumnos
(
Cod_Alumno int
	FOREIGN KEY REFERENCES Alumnos(Cod_Alumno)
					ON UPDATE CASCADE
					ON DELETE CASCADE,
Cod_Curso int
	FOREIGN KEY REFERENCES Cursos (Cod_Curso)
					ON UPDATE CASCADE
					ON DELETE CASCADE
PRIMARY KEY (Cod_Alumno, Cod_Curso),
Calificacion tinyint,
Fecha_Insc Date,
Ausencias tinyint
);












/**----------------------------------------
   Manejar el comportameinto deseado de un trigger
--------------------------------------------*/
CREATE TRIGGER tgr_Borrar_Dptos_Profesores
	ON Departamentos
	FOR DELETE
AS
BEGIN

	DELETE Dptos_Profesores
	WHERE Cod_Dpto IN(
						SELECT Cod_Dpto
						FROM DELETED
						);
END;


--------- MODIFICACION
CREATE TRIGGER trg_Modificar_Dptos_Profesores
	ON Departamentos
	FOR UPDATE
AS
BEGIN

	UPDATE Dptos_Profesores
	SET Cod_Dpto = A.Cod_Nuevo ---->actualicemos al nuevo codigo
	FROM (
		SELECT D.Cod_Dpto AS Cod_Anterior,
			   I.Cod_Dpto AS Cod_Nuevo
		FROM DELETED D -----> datos antes de la modificacion
			 Join 
			 INSERTED I ----> despues de la moficacion
			 ON 
			 D.Cod_Dpto = I.Cod_Dpto
	    Where D.Cod_Dpto <> I.Cod_Dpto
		) A
	WHERE Cod_Dpto = Cod_Anterior;
END;



