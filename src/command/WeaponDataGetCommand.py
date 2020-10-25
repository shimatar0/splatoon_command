import mysql.connector
import csv

# データ読み込み
def createWeapon():
    with open('../../data/weapon/weapon2.csv', 'r') as f:
        reader = csv.reader(f)
        # ラベルはスキップ
        header = next(reader)
        conn = mysql.connector.connect(
                                user='root',  
                                host='localhost',
                                database='splatoon'  
                            )
        cursor = conn.cursor()
        for row in reader:
            category = row[0]
            full_name = row[5]
            short_name = row[6]
            sub_weapon = row[7]
            special = row[8]
            main_performance_up = row[11]
            
        # DB保存
            sql = 'INSERT INTO weapon (category, full_name, short_name, sub_weapon, special, main_performance_up) VALUES (%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (category, full_name, short_name, sub_weapon, special, main_performance_up))

        conn.commit()
        cursor.close()
        conn.close()


# main
if __name__ == "__main__":
    createWeapon()