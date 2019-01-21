"""All constants."""

headers_init = {
    # ":authority": "www.schooldigger.com",  # for http/2
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "dnt": "1",
    "origin": "https://www.schooldigger.com",
    "referer": "https://www.schooldigger.com/go/{state}/schoolrank.aspx",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/71.0.3578.98 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

headers_page = {
    # ":authority": "www.schooldigger.com",  # for http/2
    # ":method": "POST",  # for http/2
    # ":path": "/aj/ajRankData1.aspx",  # for http/2
    # ":scheme": "https",  # for http/2
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "content-length": 0,
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "dnt": "1",
    "origin": "https://www.schooldigger.com",
    "referer": "https://www.schooldigger.com/go/{state}/"
    "schoolrank.aspx?level={level}",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/71.0.3578.98 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

main_url = "https://www.schooldigger.com/go/{state}/schoolrank.aspx?level={level}"

form_l1 = {
    "draw": None,  # critical
    "columns[0][data]": "0",
    "columns[0][name]": "",
    "columns[0][searchable]": "false",
    "columns[0][orderable]": "true",
    "columns[0][search][value]": "",
    "columns[0][search][regex]": "false",
    "columns[1][data]": "1",
    "columns[1][name]": "",
    "columns[1][searchable]": "true",
    "columns[1][orderable]": "true",
    "columns[1][search][value]": "",
    "columns[1][search][regex]": "false",
    "columns[2][data]": "2",
    "columns[2][name]": "",
    "columns[2][searchable]": "true",
    "columns[2][orderable]": "true",
    "columns[2][search][value]": "",
    "columns[2][search][regex]": "false",
    "columns[3][data]": "3",
    "columns[3][name]": "",
    "columns[3][searchable]": "true",
    "columns[3][orderable]": "true",
    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",
    "columns[4][data]": "4",
    "columns[4][name]": "",
    "columns[4][searchable]": "true",
    "columns[4][orderable]": "true",
    "columns[4][search][value]": "",
    "columns[4][search][regex]": "false",
    "columns[5][data]": "5",
    "columns[5][name]": "",
    "columns[5][searchable]": "true",
    "columns[5][orderable]": "true",
    "columns[5][search][value]": "",
    "columns[5][search][regex]": "false",
    "columns[6][data]": "6",
    "columns[6][name]": "",
    "columns[6][searchable]": "true",
    "columns[6][orderable]": "true",
    "columns[6][search][value]": "",
    "columns[6][search][regex]": "false",
    "columns[7][data]": "7",
    "columns[7][name]": "",
    "columns[7][searchable]": "true",
    "columns[7][orderable]": "true",
    "columns[7][search][value]": "",
    "columns[7][search][regex]": "false",
    "columns[8][data]": "8",
    "columns[8][name]": "",
    "columns[8][searchable]": "true",
    "columns[8][orderable]": "true",
    "columns[8][search][value]": "",
    "columns[8][search][regex]": "false",
    "columns[9][data]": "9",
    "columns[9][name]": "",
    "columns[9][searchable]": "true",
    "columns[9][orderable]": "true",
    "columns[9][search][value]": "",
    "columns[9][search][regex]": "false",
    "columns[10][data]": "10",
    "columns[10][name]": "",
    "columns[10][searchable]": "true",
    "columns[10][orderable]": "true",
    "columns[10][search][value]": "",
    "columns[10][search][regex]": "false",
    "columns[11][data]": "11",
    "columns[11][name]": "",
    "columns[11][searchable]": "true",
    "columns[11][orderable]": "true",
    "columns[11][search][value]": "",
    "columns[11][search][regex]": "false",
    "columns[12][data]": "12",
    "columns[12][name]": "",
    "columns[12][searchable]": "true",
    "columns[12][orderable]": "true",
    "columns[12][search][value]": "",
    "columns[12][search][regex]": "false",
    "columns[13][data]": "13",
    "columns[13][name]": "",
    "columns[13][searchable]": "true",
    "columns[13][orderable]": "true",
    "columns[13][search][value]": "",
    "columns[13][search][regex]": "false",
    "columns[14][data]": "14",
    "columns[14][name]": "",
    "columns[14][searchable]": "true",
    "columns[14][orderable]": "false",
    "columns[14][search][value]": "",
    "columns[14][search][regex]": "false",
    "columns[15][data]": "15",
    "columns[15][name]": "",
    "columns[15][searchable]": "true",
    "columns[15][orderable]": "true",
    "columns[15][search][value]": "",
    "columns[15][search][regex]": "false",
    "columns[16][data]": "16",
    "columns[16][name]": "",
    "columns[16][searchable]": "true",
    "columns[16][orderable]": "true",
    "columns[16][search][value]": "",
    "columns[16][search][regex]": "false",
    "columns[17][data]": "17",
    "columns[17][name]": "",
    "columns[17][searchable]": "true",
    "columns[17][orderable]": "true",
    "columns[17][search][value]": "",
    "columns[17][search][regex]": "false",
    "columns[18][data]": "18",
    "columns[18][name]": "",
    "columns[18][searchable]": "true",
    "columns[18][orderable]": "true",
    "columns[18][search][value]": "",
    "columns[18][search][regex]": "false",
    "columns[19][data]": "19",
    "columns[19][name]": "",
    "columns[19][searchable]": "true",
    "columns[19][orderable]": "true",
    "columns[19][search][value]": "",
    "columns[19][search][regex]": "false",
    "columns[20][data]": "20",
    "columns[20][name]": "",
    "columns[20][searchable]": "true",
    "columns[20][orderable]": "true",
    "columns[20][search][value]": "",
    "columns[20][search][regex]": "false",
    "columns[21][data]": "21",
    "columns[21][name]": "",
    "columns[21][searchable]": "true",
    "columns[21][orderable]": "true",
    "columns[21][search][value]": "",
    "columns[21][search][regex]": "false",
    "columns[22][data]": "22",
    "columns[22][name]": "",
    "columns[22][searchable]": "true",
    "columns[22][orderable]": "true",
    "columns[22][search][value]": "",
    "columns[22][search][regex]": "false",
    "columns[23][data]": "23",
    "columns[23][name]": "",
    "columns[23][searchable]": "true",
    "columns[23][orderable]": "true",
    "columns[23][search][value]": "",
    "columns[23][search][regex]": "false",
    "columns[24][data]": "24",
    "columns[24][name]": "",
    "columns[24][searchable]": "true",
    "columns[24][orderable]": "true",
    "columns[24][search][value]": "",
    "columns[24][search][regex]": "false",
    "columns[25][data]": "25",
    "columns[25][name]": "",
    "columns[25][searchable]": "true",
    "columns[25][orderable]": "true",
    "columns[25][search][value]": "",
    "columns[25][search][regex]": "false",
    "columns[26][data]": "26",
    "columns[26][name]": "",
    "columns[26][searchable]": "true",
    "columns[26][orderable]": "true",
    "columns[26][search][value]": "",
    "columns[26][search][regex]": "false",
    "columns[27][data]": "27",
    "columns[27][name]": "",
    "columns[27][searchable]": "true",
    "columns[27][orderable]": "true",
    "columns[27][search][value]": "",
    "columns[27][search][regex]": "false",
    "columns[28][data]": "28",
    "columns[28][name]": "",
    "columns[28][searchable]": "true",
    "columns[28][orderable]": "true",
    "columns[28][search][value]": "",
    "columns[28][search][regex]": "false",
    "columns[29][data]": "29",
    "columns[29][name]": "",
    "columns[29][searchable]": "true",
    "columns[29][orderable]": "true",
    "columns[29][search][value]": "",
    "columns[29][search][regex]": "false",
    "columns[30][data]": "30",
    "columns[30][name]": "",
    "columns[30][searchable]": "true",
    "columns[30][orderable]": "true",
    "columns[30][search][value]": "",
    "columns[30][search][regex]": "false",
    "order[0][column]": "1",
    "order[0][dir]": "asc",
    "start": None,  # critical
    "length": "50",
    "search[value]": "",
    "search[regex]": "false",
    "values[FIPS]": None,  # critical
    "values[rankType]": "0",
    "values[Level]": "1",
    "values[resAggregateYear]": "2017",
    "values[reqAggregateYear]": "2017",
    "values[resGSLInclude]": "PK,KG,01,02,03,04",  # critical
    "values[resGSHL]": "0",
    "values[resGSHH]": "13",
    "values[resGSLL]": "0",
    "values[resGSLH]": "5",
    "values[reqGSHL]": "",
    "values[reqGSHH]": "",
    "values[reqGSLL]": "",
    "values[reqGSLH]": "",
    "values[resYear]": "2018",
    "values[resYearCompare]": "2017",
    "values[reqYear]": "",
    "values[reqYearCompare]": "",
    "values[reqEntityID]": "",
    "values[reqEntitySubID]": "",
    "values[clientViewing]": "0",
    "values[chartType]": "h",
}

form_l2 = {
    "draw": None,
    "columns[0][data]": "0",
    "columns[0][name]": "",
    "columns[0][searchable]": "false",
    "columns[0][orderable]": "true",
    "columns[0][search][value]": "",
    "columns[0][search][regex]": "false",
    "columns[1][data]": "1",
    "columns[1][name]": "",
    "columns[1][searchable]": "true",
    "columns[1][orderable]": "true",
    "columns[1][search][value]": "",
    "columns[1][search][regex]": "false",
    "columns[2][data]": "2",
    "columns[2][name]": "",
    "columns[2][searchable]": "true",
    "columns[2][orderable]": "true",
    "columns[2][search][value]": "",
    "columns[2][search][regex]": "false",
    "columns[3][data]": "3",
    "columns[3][name]": "",
    "columns[3][searchable]": "true",
    "columns[3][orderable]": "true",
    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",
    "columns[4][data]": "4",
    "columns[4][name]": "",
    "columns[4][searchable]": "true",
    "columns[4][orderable]": "true",
    "columns[4][search][value]": "",
    "columns[4][search][regex]": "false",
    "columns[5][data]": "5",
    "columns[5][name]": "",
    "columns[5][searchable]": "true",
    "columns[5][orderable]": "true",
    "columns[5][search][value]": "",
    "columns[5][search][regex]": "false",
    "columns[6][data]": "6",
    "columns[6][name]": "",
    "columns[6][searchable]": "true",
    "columns[6][orderable]": "true",
    "columns[6][search][value]": "",
    "columns[6][search][regex]": "false",
    "columns[7][data]": "7",
    "columns[7][name]": "",
    "columns[7][searchable]": "true",
    "columns[7][orderable]": "true",
    "columns[7][search][value]": "",
    "columns[7][search][regex]": "false",
    "columns[8][data]": "8",
    "columns[8][name]": "",
    "columns[8][searchable]": "true",
    "columns[8][orderable]": "true",
    "columns[8][search][value]": "",
    "columns[8][search][regex]": "false",
    "columns[9][data]": "9",
    "columns[9][name]": "",
    "columns[9][searchable]": "true",
    "columns[9][orderable]": "true",
    "columns[9][search][value]": "",
    "columns[9][search][regex]": "false",
    "columns[10][data]": "10",
    "columns[10][name]": "",
    "columns[10][searchable]": "true",
    "columns[10][orderable]": "true",
    "columns[10][search][value]": "",
    "columns[10][search][regex]": "false",
    "columns[11][data]": "11",
    "columns[11][name]": "",
    "columns[11][searchable]": "true",
    "columns[11][orderable]": "true",
    "columns[11][search][value]": "",
    "columns[11][search][regex]": "false",
    "columns[12][data]": "12",
    "columns[12][name]": "",
    "columns[12][searchable]": "true",
    "columns[12][orderable]": "true",
    "columns[12][search][value]": "",
    "columns[12][search][regex]": "false",
    "columns[13][data]": "13",
    "columns[13][name]": "",
    "columns[13][searchable]": "true",
    "columns[13][orderable]": "true",
    "columns[13][search][value]": "",
    "columns[13][search][regex]": "false",
    "columns[14][data]": "14",
    "columns[14][name]": "",
    "columns[14][searchable]": "true",
    "columns[14][orderable]": "false",
    "columns[14][search][value]": "",
    "columns[14][search][regex]": "false",
    "columns[15][data]": "15",
    "columns[15][name]": "",
    "columns[15][searchable]": "true",
    "columns[15][orderable]": "true",
    "columns[15][search][value]": "",
    "columns[15][search][regex]": "false",
    "columns[16][data]": "16",
    "columns[16][name]": "",
    "columns[16][searchable]": "true",
    "columns[16][orderable]": "true",
    "columns[16][search][value]": "",
    "columns[16][search][regex]": "false",
    "columns[17][data]": "17",
    "columns[17][name]": "",
    "columns[17][searchable]": "true",
    "columns[17][orderable]": "true",
    "columns[17][search][value]": "",
    "columns[17][search][regex]": "false",
    "columns[18][data]": "18",
    "columns[18][name]": "",
    "columns[18][searchable]": "true",
    "columns[18][orderable]": "true",
    "columns[18][search][value]": "",
    "columns[18][search][regex]": "false",
    "columns[19][data]": "19",
    "columns[19][name]": "",
    "columns[19][searchable]": "true",
    "columns[19][orderable]": "true",
    "columns[19][search][value]": "",
    "columns[19][search][regex]": "false",
    "columns[20][data]": "20",
    "columns[20][name]": "",
    "columns[20][searchable]": "true",
    "columns[20][orderable]": "true",
    "columns[20][search][value]": "",
    "columns[20][search][regex]": "false",
    "columns[21][data]": "21",
    "columns[21][name]": "",
    "columns[21][searchable]": "true",
    "columns[21][orderable]": "true",
    "columns[21][search][value]": "",
    "columns[21][search][regex]": "false",
    "columns[22][data]": "22",
    "columns[22][name]": "",
    "columns[22][searchable]": "true",
    "columns[22][orderable]": "true",
    "columns[22][search][value]": "",
    "columns[22][search][regex]": "false",
    "columns[23][data]": "23",
    "columns[23][name]": "",
    "columns[23][searchable]": "true",
    "columns[23][orderable]": "true",
    "columns[23][search][value]": "",
    "columns[23][search][regex]": "false",
    "columns[24][data]": "24",
    "columns[24][name]": "",
    "columns[24][searchable]": "true",
    "columns[24][orderable]": "true",
    "columns[24][search][value]": "",
    "columns[24][search][regex]": "false",
    "columns[25][data]": "25",
    "columns[25][name]": "",
    "columns[25][searchable]": "true",
    "columns[25][orderable]": "true",
    "columns[25][search][value]": "",
    "columns[25][search][regex]": "false",
    "columns[26][data]": "26",
    "columns[26][name]": "",
    "columns[26][searchable]": "true",
    "columns[26][orderable]": "true",
    "columns[26][search][value]": "",
    "columns[26][search][regex]": "false",
    "columns[27][data]": "27",
    "columns[27][name]": "",
    "columns[27][searchable]": "true",
    "columns[27][orderable]": "true",
    "columns[27][search][value]": "",
    "columns[27][search][regex]": "false",
    "columns[28][data]": "28",
    "columns[28][name]": "",
    "columns[28][searchable]": "true",
    "columns[28][orderable]": "true",
    "columns[28][search][value]": "",
    "columns[28][search][regex]": "false",
    "columns[29][data]": "29",
    "columns[29][name]": "",
    "columns[29][searchable]": "true",
    "columns[29][orderable]": "true",
    "columns[29][search][value]": "",
    "columns[29][search][regex]": "false",
    "columns[30][data]": "30",
    "columns[30][name]": "",
    "columns[30][searchable]": "true",
    "columns[30][orderable]": "true",
    "columns[30][search][value]": "",
    "columns[30][search][regex]": "false",
    "order[0][column]": "1",
    "order[0][dir]": "asc",
    "start": None,
    "length": "50",
    "search[value]": "",
    "search[regex]": "false",
    "values[FIPS]": None,  # critical
    "values[rankType]": "0",
    "values[Level]": "2",
    "values[resAggregateYear]": "2017",
    "values[reqAggregateYear]": "2017",
    "values[GSHInclude]": "07,08,09,10,11,12",
    "values[resGSLInclude]": "PK,KG,01,02,03,04,05,06,07,08",
    "values[resGSHL]": "8",
    "values[resGSHH]": "13",
    "values[resGSLL]": "0",
    "values[resGSLH]": "9",
    "values[reqGSHL]": "",
    "values[reqGSHH]": "",
    "values[reqGSLL]": "",
    "values[reqGSLH]": "",
    "values[resYear]": "2018",
    "values[resYearCompare]": "2017",
    "values[reqYear]": "",
    "values[reqYearCompare]": "",
    "values[reqEntityID]": "",
    "values[reqEntitySubID]": "",
    "values[clientViewing]": "0",
    "values[chartType]": "h",
}

form_l3 = {
    "draw": None,
    "columns[0][data]": "0",
    "columns[0][name]": "",
    "columns[0][searchable]": "false",
    "columns[0][orderable]": "true",
    "columns[0][search][value]": "",
    "columns[0][search][regex]": "false",
    "columns[1][data]": "1",
    "columns[1][name]": "",
    "columns[1][searchable]": "true",
    "columns[1][orderable]": "true",
    "columns[1][search][value]": "",
    "columns[1][search][regex]": "false",
    "columns[2][data]": "2",
    "columns[2][name]": "",
    "columns[2][searchable]": "true",
    "columns[2][orderable]": "true",
    "columns[2][search][value]": "",
    "columns[2][search][regex]": "false",
    "columns[3][data]": "3",
    "columns[3][name]": "",
    "columns[3][searchable]": "true",
    "columns[3][orderable]": "true",
    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",
    "columns[4][data]": "4",
    "columns[4][name]": "",
    "columns[4][searchable]": "true",
    "columns[4][orderable]": "true",
    "columns[4][search][value]": "",
    "columns[4][search][regex]": "false",
    "columns[5][data]": "5",
    "columns[5][name]": "",
    "columns[5][searchable]": "true",
    "columns[5][orderable]": "true",
    "columns[5][search][value]": "",
    "columns[5][search][regex]": "false",
    "columns[6][data]": "6",
    "columns[6][name]": "",
    "columns[6][searchable]": "true",
    "columns[6][orderable]": "true",
    "columns[6][search][value]": "",
    "columns[6][search][regex]": "false",
    "columns[7][data]": "7",
    "columns[7][name]": "",
    "columns[7][searchable]": "true",
    "columns[7][orderable]": "true",
    "columns[7][search][value]": "",
    "columns[7][search][regex]": "false",
    "columns[8][data]": "8",
    "columns[8][name]": "",
    "columns[8][searchable]": "true",
    "columns[8][orderable]": "true",
    "columns[8][search][value]": "",
    "columns[8][search][regex]": "false",
    "columns[9][data]": "9",
    "columns[9][name]": "",
    "columns[9][searchable]": "true",
    "columns[9][orderable]": "true",
    "columns[9][search][value]": "",
    "columns[9][search][regex]": "false",
    "columns[10][data]": "10",
    "columns[10][name]": "",
    "columns[10][searchable]": "true",
    "columns[10][orderable]": "true",
    "columns[10][search][value]": "",
    "columns[10][search][regex]": "false",
    "columns[11][data]": "11",
    "columns[11][name]": "",
    "columns[11][searchable]": "true",
    "columns[11][orderable]": "true",
    "columns[11][search][value]": "",
    "columns[11][search][regex]": "false",
    "columns[12][data]": "12",
    "columns[12][name]": "",
    "columns[12][searchable]": "true",
    "columns[12][orderable]": "true",
    "columns[12][search][value]": "",
    "columns[12][search][regex]": "false",
    "columns[13][data]": "13",
    "columns[13][name]": "",
    "columns[13][searchable]": "true",
    "columns[13][orderable]": "true",
    "columns[13][search][value]": "",
    "columns[13][search][regex]": "false",
    "columns[14][data]": "14",
    "columns[14][name]": "",
    "columns[14][searchable]": "true",
    "columns[14][orderable]": "false",
    "columns[14][search][value]": "",
    "columns[14][search][regex]": "false",
    "columns[15][data]": "15",
    "columns[15][name]": "",
    "columns[15][searchable]": "true",
    "columns[15][orderable]": "true",
    "columns[15][search][value]": "",
    "columns[15][search][regex]": "false",
    "columns[16][data]": "16",
    "columns[16][name]": "",
    "columns[16][searchable]": "true",
    "columns[16][orderable]": "true",
    "columns[16][search][value]": "",
    "columns[16][search][regex]": "false",
    "columns[17][data]": "17",
    "columns[17][name]": "",
    "columns[17][searchable]": "true",
    "columns[17][orderable]": "true",
    "columns[17][search][value]": "",
    "columns[17][search][regex]": "false",
    "columns[18][data]": "18",
    "columns[18][name]": "",
    "columns[18][searchable]": "true",
    "columns[18][orderable]": "true",
    "columns[18][search][value]": "",
    "columns[18][search][regex]": "false",
    "columns[19][data]": "19",
    "columns[19][name]": "",
    "columns[19][searchable]": "true",
    "columns[19][orderable]": "true",
    "columns[19][search][value]": "",
    "columns[19][search][regex]": "false",
    "columns[20][data]": "20",
    "columns[20][name]": "",
    "columns[20][searchable]": "true",
    "columns[20][orderable]": "true",
    "columns[20][search][value]": "",
    "columns[20][search][regex]": "false",
    "columns[21][data]": "21",
    "columns[21][name]": "",
    "columns[21][searchable]": "true",
    "columns[21][orderable]": "true",
    "columns[21][search][value]": "",
    "columns[21][search][regex]": "false",
    "columns[22][data]": "22",
    "columns[22][name]": "",
    "columns[22][searchable]": "true",
    "columns[22][orderable]": "true",
    "columns[22][search][value]": "",
    "columns[22][search][regex]": "false",
    "columns[23][data]": "23",
    "columns[23][name]": "",
    "columns[23][searchable]": "true",
    "columns[23][orderable]": "true",
    "columns[23][search][value]": "",
    "columns[23][search][regex]": "false",
    "columns[24][data]": "24",
    "columns[24][name]": "",
    "columns[24][searchable]": "true",
    "columns[24][orderable]": "true",
    "columns[24][search][value]": "",
    "columns[24][search][regex]": "false",
    "columns[25][data]": "25",
    "columns[25][name]": "",
    "columns[25][searchable]": "true",
    "columns[25][orderable]": "true",
    "columns[25][search][value]": "",
    "columns[25][search][regex]": "false",
    "columns[26][data]": "26",
    "columns[26][name]": "",
    "columns[26][searchable]": "true",
    "columns[26][orderable]": "true",
    "columns[26][search][value]": "",
    "columns[26][search][regex]": "false",
    "columns[27][data]": "27",
    "columns[27][name]": "",
    "columns[27][searchable]": "true",
    "columns[27][orderable]": "true",
    "columns[27][search][value]": "",
    "columns[27][search][regex]": "false",
    "columns[28][data]": "28",
    "columns[28][name]": "",
    "columns[28][searchable]": "true",
    "columns[28][orderable]": "true",
    "columns[28][search][value]": "",
    "columns[28][search][regex]": "false",
    "columns[29][data]": "29",
    "columns[29][name]": "",
    "columns[29][searchable]": "true",
    "columns[29][orderable]": "true",
    "columns[29][search][value]": "",
    "columns[29][search][regex]": "false",
    "columns[30][data]": "30",
    "columns[30][name]": "",
    "columns[30][searchable]": "true",
    "columns[30][orderable]": "true",
    "columns[30][search][value]": "",
    "columns[30][search][regex]": "false",
    "order[0][column]": "1",
    "order[0][dir]": "asc",
    "start": None,
    "length": "50",
    "search[value]": "",
    "search[regex]": "false",
    "values[FIPS]": None,  # critical
    "values[rankType]": "0",
    "values[Level]": "3",
    "values[resAggregateYear]": "2017",
    "values[reqAggregateYear]": "2017",
    "values[GSHInclude]": "12",
    "values[resGSHL]": "13",
    "values[resGSHH]": "13",
    "values[resGSLL]": "0",
    "values[resGSLH]": "13",
    "values[reqGSHL]": "",
    "values[reqGSHH]": "",
    "values[reqGSLL]": "",
    "values[reqGSLH]": "",
    "values[resYear]": "2018",
    "values[resYearCompare]": "2017",
    "values[reqYear]": "",
    "values[reqYearCompare]": "",
    "values[reqEntityID]": "",
    "values[reqEntitySubID]": "",
    "values[clientViewing]": "0",
    "values[chartType]": "h"
}
# school level to form
forms = {
    1: form_l1,
    2: form_l2,
    3: form_l3,
}

school_level = {1: "elementary", 2: "middle", 3: "high"}

school_level_to_year = {1: "PK,KG,01,02,03,04", 2: "05,06,07,08", 3: "09,10,11,12"}

entry_point = "https://www.schooldigger.com/aj/ajRankData1.aspx"

state_codes = [
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "DC",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
]

state_to_fips = {
    "AL": "01",
    "AK": "02",
    "AZ": "04",
    "AR": "05",
    "CA": "06",
    "CO": "08",
    "CT": "09",
    "DE": "10",
    "FL": "12",
    "GA": "13",
    "HI": "15",
    "ID": "16",
    "IL": "17",
    "IN": "18",
    "IA": "19",
    "KS": "20",
    "KY": "21",
    "LA": "22",
    "ME": "23",
    "MD": "24",
    "MA": "25",
    "MI": "26",
    "MN": "27",
    "MS": "28",
    "MO": "29",
    "MT": "30",
    "NE": "31",
    "NV": "32",
    "NH": "33",
    "NJ": "34",
    "NM": "35",
    "NY": "36",
    "NC": "37",
    "ND": "38",
    "OH": "39",
    "OK": "40",
    "OR": "41",
    "PA": "42",
    "RI": "44",
    "SC": "45",
    "SD": "46",
    "TN": "47",
    "TX": "48",
    "UT": "49",
    "VT": "50",
    "VA": "51",
    "WA": "53",
    "WV": "54",
    "WI": "55",
    "WY": "56",
    "DC": "11",
    "AS": "60",
    "GU": "66",
    "MP": "69",
    "PR": "72",
    "VI": "78",
 }