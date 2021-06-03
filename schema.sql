-- Insert the data from .csv
DROP TABLE IF EXISTS [austin_weather];
CREATE TABLE [austin_weather] (
	[Date] nvarchar(10),
	[TempHighF] nvarchar(4),
	[TempAvgF] nvarchar(8),
	[TempLowF] nvarchar(8),
	[DewPointHighF] nvarchar(8),
	[DewPointAvgF] nvarchar(8),
	[DewPointLowF] nvarchar(8),
	[HumidityHighPercent] nvarchar(8),
	[HumidityAvgPercent] nvarchar(8),
	[HumidityLowPercent] nvarchar(8),
	[SeaLevelPressureHighInches] nvarchar(8),
	[SeaLevelPressureAvgInches] nvarchar(8),
	[SeaLevelPressureLowInches] nvarchar(8),
	[VisibilityHighMiles] nvarchar(8),
	[VisibilityAvgMiles] nvarchar(8),
	[VisibilityLowMiles] nvarchar(8),
	[WindHighMPH] nvarchar(8),
	[WindAvgMPH] nvarchar(8),
	[WindGustMPH] nvarchar(8),
	[PrecipitationSumInches] nvarchar(8),
	[Events] nvarchar(100)
);

-- Inserting into austin_weather table
TRUNCATE TABLE [austin_weather];
BULK INSERT [austin_weather]
FROM 'D:\���\������ �� (4 �������)\austin_weather.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '0x0a'
)
GO


-- =============== CREATING STORAGE ===============
-- Create date dimension
DROP TABLE IF EXISTS [DateDim];
CREATE TABLE [DateDim] (
	[DateID] int IDENTITY(1,1) PRIMARY KEY,
	[Day] int,      -- ����
	[Month] int,    -- ̳����
	[Year] int      -- г�
);

-- Create weather table
DROP TABLE IF EXISTS [Weather];
CREATE TABLE [Weather] (
	[WeatherID] int IDENTITY(1,1) PRIMARY KEY NOT NULL,
	[DateID] int,                  -- ��������� �� ����
	[Temperature] int,             -- ����������� (�� �����������)
	[DewPoint] int,                -- ����� ���� (�� �����������)
	[Humidity] int,                -- �������� (³������)
	[SeaLvlPressure] float,        -- ���� �� ��� ���� (�����)
	[Visibility] int,              -- �������� (���)
	[Wind] int,                    -- �������� ���� (���� � ������)

	CONSTRAINT FK_DateID FOREIGN KEY (DateID) REFERENCES [DateDim](DateID) ON DELETE CASCADE
);

SELECT * FROM DateDim
SELECT * FROM Weather
