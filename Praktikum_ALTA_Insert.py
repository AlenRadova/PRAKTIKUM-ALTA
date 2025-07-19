import sqlite3

connect_to_db = sqlite3.connect("Cars.db")

k = connect_to_db.cursor()

k.execute("""
    INSERT INTO TBCars (
        id,
        name,
        brand,
        model,
        price
    )
    VALUES 
        ('101', 'Ferrarri 599XX 2012', 'Ferrari', 'Carbon', 15000),
        ('102', 'Lamborghini Revuelto 2024', 'Lamborghini', 'Carbon', 25000)
""")


connect_to_db.commit()
connect_to_db.close()