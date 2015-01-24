# 臺語辭補完計畫（Holo-at-on）

Supplement of Holo terms. 替臺語辭典增加一寡仔現代詞彙。

## Requirements

* Python 2.7+
* BeautifulSoup (3.2.1)
* pandas (0.15.2)

## Descriptions

### 臺灣縣市鄉鎮區名

* `all_mapping.csv`
	* 來源：[臺灣閩南語常用詞辭典 - 臺灣縣市鄉鎮區名](http://twblg.dict.edu.tw/holodict_new/index/xiangzhen_level1.jsp?county=1)
	* 內容：包含縣市與鄉鎮區的臺語讀音。		
		目前欠:				
		* 桃園(這馬變直轄市)：八德區、蘆竹區、桃園區、平鎮區、龜山區、中壢區、楊梅區、復興區、新屋區、大園區、觀音區、龍潭區、大溪區
		* 高雄：那瑪夏區
		* 南海島
		* 南沙群島、東沙群島
	* 程式：`code/get.py`, `code/check.py`
	* 落尾翻新：2015-01-25	

### 縣市鄉鎮市區 (Zip Code) + 路名

* `Zip32_10312.csv`
	* 來源：[3+2碼郵遞區號Excel檔 103/12 (zip檔)](http://www.post.gov.tw/post/internet/Download/all_list.jsp?ID=2201)
	* 檔案：`data/Zip32_10312.csv`
	* 內容：
	* 版本：2014-12	
	* 程式：`code/check.py`, 'code/zipCode.py'
	* 落尾翻新：2015-01-25

### 國家教育研究院雙語詞彙

來源：[國家教育研究院](http://terms.naer.edu.tw/download/)

* 外國地名譯名	
	* 內容：
	* 版本：2015-01-20	
	* 程式：
	* 落尾翻新：2015-01-25
* 人體解剖學
* 力學名詞
* 土木工程


