#import mysql.connector
import csv

#conn = mysql.connector.connect(host='127.0.0.1')

#cursor = conn.cursor()

# データ読み込み
def createWeapon():
    with open('../../data/weapon/statink-weapon2.csv', 'r') as f:
        reader = csv.reader(f)
        # ラベルはスキップ
        header = next(reader)
        for row in reader:
            print(row[2])

# DB保存

# main
if __name__ == "__main__":
    createWeapon()