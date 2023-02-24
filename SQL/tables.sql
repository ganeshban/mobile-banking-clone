Create database cloneMobBanking

use cloneMobBanking



CREATE Table tblusers(
    SN BIGINT PRIMARY KEY Identity(1,1),
    username VARCHAR(50) NOT NULL UNIQUE,
    userPass VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    isActive BIT DEFAULT 1,
)
-----------------------------------------------------------------------------------------


CREATE Table tblLoginHistory(
    SN BIGINT PRIMARY KEY Identity(1,1),
    userID BIGINT REFERENCES tblusers(SN),
    loginDateTime DateTime DEFAULT CURRENT_TIMESTAMP,
    logOutDateTime DateTime DEFAULT NULL
)

CREATE PROCEDURE procAddLoginHistory 
	@uid BIGINT,
	@did BIGINT
AS
BEGIN
	INSERT INTO tblLoginHistory VALUES (@uid,  CURRENT_TIMESTAMP, NULL)
END

-----------------------------------------------------------------------------------------
CREATE PROCEDURE ProcLogIn
	@username VARCHAR(50),
	@password VARCHAR(50)
AS
BEGIN
	DECLARE @uid BIGINT
	DECLARE @hid BIGINT

	SET @uid=0
	SET @hid=0

	SET @uid = isNULL((SELECT sn FROM tblusers WHERE username=@username AND userPass=@password AND isActive=1),0)
	IF(@uid = 0)
	BEGIN
		PRINT 'Either username or password is wrong /nLogin Faild' 
		RETURN 0

	END


	SET @hid = isNULL((SELECT SN FROM tblLoginHistory WHERE userID=@uid AND logOutDateTime is NULL),0)
	IF(@hid != 0)
	BEGIN
		PRINT 'This user is already Logedin, Please Logout first. /nLogin Faild' 
		RETURN 0

	END

	IF (@hid=0 AND @uid>0 )
	BEGIN
		exec procAddLoginHistory @uid
		PRINT 'Login Success !!!'
		RETURN 1
	END

END
-----------------------------------------------------------------------------------------

exec ProcLogIn 'ganesh','gan123'
