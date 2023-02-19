**出典：[環境省生物多様性センター植生調査(1/2.5万)全県データ](http://gis.biodic.go.jp/webgis/sc-025.html?kind=vg67)** <br>
**上記に基いて**[obscraft23](https://github.com/obscraft23)**が編集加工を行ったデータを**[生物多様性センターウェブサイト利用規約](https://www.biodic.go.jp/copyright/terms_of_service.html)**に基づき出典明記の上公開するものである。** <br>
**本リポジトリに環境省生物多様性センターは一切関与していません。** <br>

![GitHub](https://img.shields.io/github/license/obscraft23/japan-vegetation-map-legend-lyr?style=for-the-badge)

## TL;DL

[環境省生物多様性センター](https://www.biodic.go.jp/)作成の1/2.5万植生図で使用されている.lyrファイルの一覧とその変換物一式です。<br>
GISの専門家ではありませんが、個人的な目的で収集したものを公開します。<br>
最終更新:2023-02-19

## lyrファイル一覧
| lyrファイル名 | QGIS SLYR(注1)での読み込み |  qml | qlr | xml | png |
|:------ |:------ |:------ |:------ |:------ |:------ |
|[凡例ver1.1.lyr](lyr/凡例ver1.1.lyr)| :white_check_mark: | [凡例ver1.1.qml](qml/凡例ver1.1.qml)|[凡例ver1.1.qlr](qlr/凡例ver1.1.qlr) | [legends.v1_1.xml](xml/legends.v1_1.xml)| [png.legends.v1_1](png/png.legends.v1_1) |
|[凡例ver1.5.lyr](lyr/凡例ver1.5.lyr)| :white_check_mark: | [凡例ver1.5.qml](qml/凡例ver1.5.qml)|[凡例ver1.5.qlr](qlr/凡例ver1.5.qlr) | [legends.v1_5.xml](xml/legends.v1_5.xml)| [png.legends.v1_5](png/png.legends.v1_5)|
|[凡例ver1.6.lyr](lyr/凡例ver1.6.lyr)| :white_check_mark: |[凡例ver1.6.qml](qml/凡例ver1.6.qml) | [凡例ver1.6.qlr](qlr/凡例ver1.6.qlr)| [legends.v1_6.xml](xml/legends.v1_6.xml)| [png.legends.v1_6](png/png.legends.v1_6)|
|[凡例ver1.7.lyr](lyr/凡例ver1.7.lyr)| :white_check_mark:| [凡例ver1.7.qml](qml/凡例ver1.7.qml)| [凡例ver1.7.qlr](qlr/凡例ver1.7.qlr)| [legends.v1_7.xml](xml/legends.v1_7.xml)| [png.legends.v1_7](png/png.legends.v1_7)|
|[凡例ver1.7_esri91.lyr](lyr/凡例ver1.7_esri91.lyr)| :white_check_mark:| [凡例ver1.7_esri91.qml](qml/凡例ver1.7_esri91.qml)| [凡例ver1.7_esri91.qlr](qlr/凡例ver1.7_esri91.qlr)| [legends.v1_7.esri91.xml](xml/legends.v1_7.esri91.xml)| [png.legends.v1_7.esri91](png/png.legends.v1_7.esri91)|
|[凡例ver2.2.lyr](lyr/凡例ver2.2.lyr)| :white_check_mark:| [凡例ver2.2.qml](qml/凡例ver2.2.qml)|[凡例ver2.2.qlr](qlr/凡例ver2.2.qlr) | [legends.v2_2.xml](xml/legends.v2_2.xml)| [png.legends.v2_2](png/png.legends.v2_2)|
|[凡例ver2.4.lyr](lyr/凡例ver2.4.lyr)| :white_check_mark:| [凡例ver2.4.qml](qml/凡例ver2.4.qml)| [凡例ver2.4.qlr](qlr/凡例ver2.4.qlr)| [legends.v2_4.xml](xml/legends.v2_4.xml)| [png.legends.v2_4](png/png.legends.v2_4)|
|[凡例ver2.5.lyr](lyr/凡例ver2.5.lyr)| :white_check_mark:|[凡例ver2.5.qml](qml/凡例ver2.5.qml) | [凡例ver2.5.qlr](qlr/凡例ver2.5.qlr)| [legends.v2_5.xml](xml/legends.v2_5.xml)| [png.legends.v2_5](png/png.legends.v2_5)|
|[凡例ver2.6.lyr](lyr/凡例ver2.6.lyr)| | | | | |
|[凡例ver2.6_esri91.lyr](lyr/凡例ver2.6_esri91.lyr)| | | | | |
|[凡例ver2.9_esri91.lyr](lyr/凡例ver2.9_esri91.lyr)| | | | | |
|[凡例ver3.0_esri91.lyr](lyr/凡例ver3.0_esri91.lyr)| | | | | |

注1: QGIS v3.28, SLYR v4.0.6 (Community Edition)

## 作成方法

+ 環境省生物多様性センター植生調査(1/2.5万)全県データ(vg67.zip)をpythonで読み込みlyrの一覧を取得・抽出<br>
[サンプルコード](abstract_lyr.py)（注: 全県データを読む場合、[Google Colaboratory](https://colab.research.google.com/?hl=ja)で30分ほどかかります）

+ lyrファイルをQGIS及びSLYR プラグインで読み込み、変換

## 問題点
+ 凡例ver2.6.lyr以降の新しいlyrファイルはプラグインのエラーが発生して読み込めなかった。

## ライセンス
[生物多様性センターウェブサイト利用規約](https://www.biodic.go.jp/copyright/terms_of_service.html)と互換性のある[CC-BY-4](https://creativecommons.org/licenses/by/4.0/legalcode.ja)を適用しています。

## 参考
+ QGIS https://qgis.org/ja/site/
+ SLYR https://github.com/north-road/slyr
+ https://qiita.com/Yfuruchin/items/aa9e1f4d9739446dcafe

## 連絡先

[![Gmail adress](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](obscraft23@gmail.com)
