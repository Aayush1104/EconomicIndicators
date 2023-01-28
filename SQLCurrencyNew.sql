
Select *
From CurrencyProject..GDP
join CurrencyProject..POP
	On GDP.[Country Name] = POP.[Country Name]
	and GDP.[Country Code] = GDP.[Country Code]
order by 1

Select *, ((GDP.[2021]-GDP.[1961])/60) as [AvgIncrease/Year]
From CurrencyProject..GDP
order by 1

Select *, ((POP.[2021]-POP.[1961])/60) as [AvgPOPIncrease/Year]
From CurrencyProject..POP
order by 1

DELETE FROM GDP WHERE [Country Name]='Country Name'
DELETE FROM GDP WHERE [Country Name]='South Asia';
DELETE FROM POP WHERE [Country Name]='Country Name';
DELETE FROM POP WHERE [Country Name]='South Asia';

Select [Country Name], [2021]
From CurrencyProject..GDP
order by 2 desc

Select [Country Name], [2021]
From CurrencyProject..POP
order by 2 desc

Select GDP.[Country Name], GDP.[2021], POP.[2021], (GDP.[2021]/POP.[2021]) as [GDP Per Capita]
From CurrencyProject..GDP
join CurrencyProject..POP
	On GDP.[Country Name] = POP.[Country Name]
order by 4 desc

