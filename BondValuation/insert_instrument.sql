

declare @ID int = 0
declare @TICKER VARCHAR(255) = 'S_UDIBONO_401115'
DECLARE @INSTRUMENT_TYPE VARCHAR(255) = 'BOND'

--INSERT INTO INSTRUMENT VALUES
--(@ID,@TICKER,@INSTRUMENT_TYPE)

INSERT INTO BOND_BD_TEST VALUES
(@ID,@TICKER,@INSTRUMENT_TYPE,'UDI',0.04,100.0,'FIJO','Act/360','True Period Fixed','Semi-Annual (182/360)','Semi-Annual (182/360)','20401115')


select * FROM BOND_BD_TEST 
--truncate table BOND_BD_TEST
--truncate table INSTRUMENT
SELECT * FROM BOND_BD_TEST
select * from INSTRUMENT 



SELECT * FROM Bonos.Instrumento WHERE NOMBRE = 'S_UDIBONO_401115'


select * from valmer.Vector where instrumento = 'S_UDIBONO_401115'

instrumento = 'M_BONOS_381118'
valDate = dt.datetime(2022,1,3)
dataValmer = valmer.ValmerVector(valDate, instrumento)
notional = 100
tasaCupon = 0.085
yield_rate = 0.08
fechaVencimiento = dt.datetime(2038,11,18)
#fechaEmision = valDate
yieldComposition = "Semi-Annual (182/360)"
paymentComposition = yieldComposition
dayCountConvention = "Act/360"
paymentConvention = "Following"
yieldCalcMethod = "None"
holidays = cMXN.holidays(valDate, fechaVencimiento)