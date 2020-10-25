# splatoon_command

#### WeaponDataGetCommand

武器マスタ生成のコマンド

指定フォルダ(data/weapon/)のcsvファイルから武器のデータをDBに格納する。保存されるデータは元ファイルorスキーマ参照。  
スプラ2はアップデートされないので、一度しか実行されないであろう悲しいコマンド(そして実行後にdumpしたsqlファイルがdata/weaponに…)    

```
python3 WeaponDataGetCommand.py
```