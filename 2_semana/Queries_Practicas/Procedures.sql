-----------Store procedures----------------------
---- grupo de instrucciones sql que se almacenan como objeto en la metadata de la bd

CREATE PROCEDURE Paises_Insertar
	@Cod_Pais char(2),  -------SON LOS PARAMETROS
	@Nombre varchar(50),
	@Cod_ISO3 char(3),
	@Cod_Telefonico smallint = NULL
AS
BEGIN
	INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico)
				VALUES (@Cod_Pais,@Nombre, @Cod_ISO3, @Cod_Telefonico);
END;


-----------EJECUTAR PROCEDURE
EXEC Paises_Insertar
	@Cod_Pais = 'TWN',
	@Nombre = 'Taiwan',
	@Cod_ISO3 = 'TWN'

	Select * from Paises


	------------------------- modificar el procedure
ALTER PROCEDURE Paises_Insertar
	@Cod_Pais char(2),  -------SON LOS PARAMETROS
	@Nombre varchar(50),
	@Cod_ISO3 char(3),
	@Cod_Telefonico smallint = NULL
AS
BEGIN
	DECLARE @Msg nvarchar(4000),
			@Err INT;

	BEGIN TRY
	INSERT INTO Paises(Cod_Pais, Nombre, Cod_ISO3, Cod_Telefonico)
				VALUES (@Cod_Pais,@Nombre, @Cod_ISO3, @Cod_Telefonico);
	END TRY
	BEGIN CATCH
		SET  @Err = @@ERROR;
		IF @Err = 547
			SET @Msg = 'LOS DATOS INGRESADOS SON INCORRECTOS';
		ELSE IF @Err =2627
				SET @Msg = 'EL PAIS YA EXISTE';
		ELSE
			SET @Msg= ERROR_MESSAGE();

		PRINT @Msg;

		RETURN -1;
	END CATCH;
	RETURN 0;
END;

/**********************************************
		CRUD con procedures
**********************************************/

CREATE PROCEDURE Estados_insertar
	@Cod_Estado char(2),
	@Cod_Pais char(2),
	@Nombre varchar(50),
	@Cod_Telefonico smallint = NULL
AS
BEGIN 
	INSERT INTO Estados (Cod_Estado, Cod_Pais, Nombre, Cod_Telefonico) 
				VALUES (@Cod_Estado, @Cod_Pais, @Nombre, @Cod_Telefonico);
END

--------------MODIFICAR

CREATE PROCEDURE Estados_Modificar
	@Cod_Estado char(2),
	@Cod_Pais char(2),
	@Nombre varchar(50),
	@Cod_Telefonico smallint = NULL
AS
BEGIN 
	UPDATE Estados
	SET Cod_Estado = @Cod_Estado, 
		Cod_Pais = @Cod_Pais, 
		Nombre =  @Nombre, 
		Cod_Telefonico = @Cod_Telefonico
	WHERE Cod_Estado = @Cod_Estado
	
END


-------------ELIMINAR
CREATE PROCEDURE Estados_Eliminar
	@Cod_Estado char(2)
AS
BEGIN 
	DELETE Estados
	WHERE Cod_Estado = @Cod_Estado;
END















