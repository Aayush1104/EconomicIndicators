import requests
import pyodbc
import json

connection = pyodbc.connect('Driver={SQL Server};' 'Server=AAYUSHPC\SQLEXPRESS;' 'Database=CurrencyProject;' 'Trusted_Connection=yes;')

if connection:
    print("Connection Successful")

def get_currency():
    url = 'https://api.exchangerate.host/latest'
    payload = {'base': 'USD'}
    response = requests.get(url, payload)
    if response.status_code == 200:
        return response.json()

def make_array():
    CurrMap = {'AED': 'United Arab Emirates dirham','AFN': 'Afghan afghani','ALL': 'Albanian lek','AMD': 'Armenian dram','ANG': 'Netherlands Antillean guilder','AOA': 'Angolan kwanza','ARS': 'Argentine peso','AUD': 'Australian dollar','AWG': 'Aruban florin','AZN': 'Azerbaijani manat','BAM': 'Bosnia and Herzegovina convertible mark','BBD': 'Barbadian dollar','BDT': 'Bangladeshi taka','BGN': 'Bulgarian lev','BHD': 'Bahraini dinar','BIF': 'Burundian franc','BMD': 'Bermudian dollar','BND': 'Brunei dollar','BOB': 'Bolivian boliviano','BRL': 'Brazilian real','BSD': 'Bahamian dollar','BTC': 'Bitcoin','BTN': 'Bhutanese ngultrum','BWP': 'Botswana pula','BYN': 'Belarusian ruble','BZD': 'Belize dollar','CAD': 'Canadian dollar','CDF': 'Congolese franc','CHF': 'Swiss franc','CLF': 'Unidad de Fomento','CLP': 'Chilean peso','CNH': 'Offshore Chinese yuan','CNY': 'Renminbi', 'COP': 'Colombian Peso','CRC': 'Costa Rican colon','CUC': 'Cuban convertible peso','CUP': 'Cuban peso','CVE': 'Cape Verdean escudo','CZK': 'Czech koruna','DJF': 'Djiboutian franc','DKK': 'Danish krone','DOP': 'Dominican peso','DZD': 'Algerian dinar','EGP': 'Egyptian pound','ERN':'Eritrean Nakfa','ETB': 'Ethiopian birr','EUR': 'Euro','FJD': 'Fijian dollar','FKP': 'Falkland Islands pound','GBP': 'British pound','GEL': 'Georgian lari','GGP': 'Guernsey pound','GHS': 'Ghanaian cedi','GIP': 'Gibraltar pound','GMD': 'Gambian dalasi','GNF': 'Guinean franc','GTQ': 'Guatemalan quetzal','GYD': 'Guyanese dollar','HKD': 'Hong Kong dollar','HNL': 'Honduran lempira','HRK': 'Croatian kuna','HTG': 'Haitian gourde','HUF': 'Hungarian forint','IDR': 'Indonesian rupiah','ILS': 'Israeli new sheqel','IMP': 'Manx pound','INR': 'Indian rupee','IQD': 'Iraqi dinar','IRR': 'Iranian rial','ISK': 'Icelandic krona','JEP': 'Jersey pound','JMD': 'Jamaican dollar','JOD': 'Jordanian dinar','JPY': 'Japanese yen','KES': 'Kenyan shilling','KGS': 'Kyrgyzstani som','KHR': 'Cambodian riel','KMF': 'Comorian franc','KPW': 'North Korean won','KRW': 'South Korean won','KWD': 'Kuwaiti dinar','KYD': 'Cayman Islands dollar','KZT': 'Kazakhstani tenge','LAK': 'Lao kip','LBP': 'Lebanese pound','LKR': 'Sri Lankan rupee','LRD':'Liberian dollar','LSL': 'Lesotho loti','LYD': 'Libyan dinar','MAD': 'Moroccan dirham','MDL': 'Moldovan leu','MGA': 'Malagasy ariary','MKD':'Macedonian denar','MMK': 'Myanmar kyat','MNT': 'Mongolian tugrik','MOP': 'Macanese pataca','MRU': 'Mauritanian ouguiya','MUR': 'Mauritian rupee','MVR': 'Maldivian rufiyaa','MWK': 'Malawian kwacha','MXN': 'Mexican peso','MYR': 'Malaysian ringgit','MZN': 'Mozambican metical','NAD': 'Namibian dollar','NGN': 'Nigerian naira','NIO': 'Nicaraguan cordoba','NOK': 'Norwegian krone','NPR': 'Nepalese rupee','NZD': 'New Zealand dollar','OMR': 'Omani rial','PAB': 'Panamanian balboa','PEN': 'Peruvian nuevo sol','PGK': 'Papua New Guinea Kina','PHP': 'Philippine Peso','PKR': 'Pakistani Rupee','PLN': 'Polish Zloty','PYG': 'Paraguayan Guarani','QAR': 'Qatari Riyal','RON': 'Romanian Leu','RSD': 'Serbian Dinar','RUB': 'Russian Ruble', 'RWF': 'Rwandan Franc','SAR': 'Saudi Riyal','SBD': 'Solomon Islands Dollar','SCR': 'Seychelles Rupee','SDG': 'Sudanese Pound','SEK': 'Swedish Krona','SGD': 'Singapore Dollar','SHP': 'Saint Helena Pound','SLL': 'Sierra Leonean Leone','SOS': 'Somali Shilling','SRD': 'Surinamese Dollar','SSP': 'South Sudanese Pound','STD': 'São Tomé and Príncipe Dobra','STN': 'El Salvador Colon','SVC':'Salvadoran colón','SYP': 'Syrian Pound','SZL': 'Swazi Lilangeni','THB': 'Thai Baht','TJS': 'Tajikistani Somoni','TMT': 'Turkmenistani Manat','TND': 'Tunisian Dinar','TOP': 'Tongan Pa\'anga','TRY': 'Turkish Lira','TTD': 'Trinidad and Tobago Dollar','TWD': 'New Taiwan Dollar','TZS': 'Tanzanian Shilling','UAH': 'Ukrainian Hryvnia','UGX': 'Ugandan Shilling','USD': 'United States Dollar','UYU': 'Uruguayan Peso','UZS': 'Uzbekistani Som','VES': 'Venezuelan Bolívar','VND': 'Vietnamese Dong','VUV': 'Vanuatu Vatu','WST': 'Samoan Tala','XAF': 'Central African CFA Franc','XAG': 'Silver (troy ounce)','XAU': 'Gold (troy ounce)','XCD': 'East Caribbean Dollar','XDR': 'Special Drawing Rights','XOF': 'West African CFA Franc','XPD': 'Palladium (ounce)','XPF': 'CFP Franc','XPT': 'Platinum (troy ounce)','YER': 'Yemeni Rial','ZAR': 'South African Rand','ZMW': 'Zambian Kwacha','ZWL': 'Zimbabwean Dollar'}
    return CurrMap

def insert_currency():
    data = get_currency()
    cursor = connection.cursor()
    CurrencyMap = make_array()
    cursor.execute("DELETE FROM CurrencyTable")
    for key in data['rates']:
        cursor.execute("INSERT INTO CurrencyTable(Rate, ISO, Currency) VALUES (?,?,?);", (data['rates'][key], key, CurrencyMap[key]))
        connection.commit()

insert_currency()
    