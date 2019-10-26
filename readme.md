# Devil Survivor Compendium

A terminal compendium for Devil Survivor Overclocked. Data scraped from [PukiWiki](http://wikinavi.net/dsoc/index.php?%E4%BB%B2%E9%AD%94%2F%E7%A8%AE%E6%97%8F%E5%88%A5).

## Usage

```
$ python compendium.py -h
usage: compendium.py [-h] [-r RACE] [-n NAME] [-l LIST] [-k KEY] [-a]

optional arguments:
  -h, --help            show this help message and exit
  -r RACE, --race RACE  filter by race (comma separated string)
  -n NAME, --name NAME  filter by name (comma separated string)
  -l LIST, --list LIST  number of results to display
  -k KEY, --key KEY     field to sort results by
  -a, --asc             display results in ascending order
```

```
$ python compendium.py -l 3 -r 魔王、女神
魔王 ルシファー (LIMITED)
  LV 99    HP 999   MP 516
  力 29    魔 30    体 28    速 28
  物 耐    火 耐    氷 耐
  電 耐    衝 耐    魔 無
  ー
  ー
  覇王の盟約

女神 アマテラス (LIMITED)
  LV 73    HP 465   MP 306
  力 21    魔 29    体 20    速 19
  物 ー    火 無    氷 ー
  電 ー    衝 無    魔 ー
  常世の祈り、 リカームロス
  ー
  女神の慈愛

女神 ブラックマリア
  LV 66    HP 415   MP 294
  力 20    魔 26    体 17    速 19
  物 ー    火 ー    氷 吸
  電 弱    衝 耐    魔 ー
  ディアラハン
  氷結吸収
  女神の慈愛
```
