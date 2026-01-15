# Importer les packages necessaires
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox

# ----------------------------------------------Les fonctions-------------------------------------------------------
# 1-creer la base do donnees et la table
def creer_carnet():
    conn = sqlite3.connect("projet.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Persons(ID INTEGER PRIMARY KEY AUTOINCREMENT,Nom varchar(255),Prenom varchar(255),Telephone int,Mail varchar(255));""")
    conn.commit()
    conn.close()

# 2-Ajouter un contact dans le carnet
def inserer_contact():
    if not lineEditNom.text() or not lineEditPreNom.text() or not lineEditTel.text() or not lineEditMail.text():
        QMessageBox.critical(fen, "Erreur", "Tous les champs doivent être remplis !")
        return
    try:
        tel = int(lineEditTel.text())
        if tel <= 0:
            QMessageBox.critical(fen, "Erreur", "Le téléphone doit être un nombre positif !")
            return
    except ValueError:
        QMessageBox.critical(fen, "Erreur", "Le téléphone doit être un nombre entier !")
        return
    conn = sqlite3.connect("projet.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Persons (Nom, Prenom, Telephone, Mail)VALUES (?, ?, ?, ?)""", (lineEditNom.text(),lineEditPreNom.text(),lineEditTel.text(),lineEditMail.text()))
    conn.commit()
    conn.close()
    afficher_carnet()
    QMessageBox.information(fen, "Succès", "Le contact a été ajouté avec succès !")


# 3-Supprimer un contact dans le carnet
def supprimer_contact():
    conn = sqlite3.connect("projet.db")
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(ID) FROM Persons")
    max_id = cursor.fetchone()[0]
    try:
        deleted_id = int(lineEditID.text())
    except ValueError:
        QMessageBox.critical(fen, "Erreur", "L'ID doit être un nombre entier !")
        return
    if deleted_id <= 0 or deleted_id > max_id:
        QMessageBox.critical(fen, "Erreur", "Entrer un ID correct !")
        return
    else:
        deleted_id = int(lineEditID.text())
        cursor.execute("DELETE FROM Persons WHERE ID = ?", (deleted_id,))
        cursor.execute("UPDATE Persons SET ID = ID - 1 WHERE ID > ?", (deleted_id,))
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='Persons'")
        conn.commit()
        conn.close()
        afficher_carnet()
        QMessageBox.information(fen, "Succès", "Le contact a été supprimer avec succès !")

# 4-Modifier un contact dans le carnet
def modifier_contact():
    if not lineEditNom.text() or not lineEditPreNom.text() or not lineEditTel.text() or not lineEditMail.text():
        QMessageBox.critical(fen, "Erreur", "Tous les champs doivent être remplis !")
        return
    try:
        tel = int(lineEditTel.text())
        if tel <= 0:
            QMessageBox.critical(fen, "Erreur", "Le téléphone doit être un nombre positif !")
            return
    except ValueError:
        QMessageBox.critical(fen, "Erreur", "Le téléphone doit être un nombre entier !")
        return
    conn = sqlite3.connect("projet.db")
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(ID) FROM Persons")
    max_id = cursor.fetchone()[0]
    try:
        deleted_id = int(lineEditID.text())
    except ValueError:
        QMessageBox.critical(fen, "Erreur", "L'ID doit être un nombre entier !")
        return
    if deleted_id <= 0 or deleted_id > max_id:
        QMessageBox.critical(fen, "Erreur", "Entrer un ID correct !")
        return
    else :
        cursor.execute("""UPDATE Persons SET Nom=?, Prenom=?, Telephone=?, Mail=?WHERE ID=?""",(lineEditNom.text(),lineEditPreNom.text(),lineEditTel.text(),lineEditMail.text(),lineEditID.text()))
        conn.commit()
        conn.close()
        afficher_carnet()
        QMessageBox.information(fen, "Succès", "Le contact a été modifier avec succès !")

# 5-Afficher le carnet
def afficher_carnet():
    conn = sqlite3.connect("projet.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Persons")
    resultat = cursor.fetchall()
    conn.close()
    qtab.setRowCount(len(resultat))
    qtab.setColumnCount(5)
    qtab.setHorizontalHeaderLabels(['ID', 'Nom', 'Prenom', 'Telephone', 'Mail'])
    # La Taille Des colonnes
    qtab.setColumnWidth(0, 50)
    qtab.setColumnWidth(1, 120)
    qtab.setColumnWidth(2, 120)
    qtab.setColumnWidth(3, 160)
    qtab.setColumnWidth(4, 155)
    for i in range(len(resultat)):
        for j in range(5):
            qtab.setItem(i, j, QTableWidgetItem(str(resultat[i][j])))

# 6-Recuperer les ligne dans le tableau
def getClickedCell(row, column):
    lineEditID.setText(qtab.item(row, 0).text())
    lineEditNom.setText(qtab.item(row, 1).text())
    lineEditPreNom.setText(qtab.item(row, 2).text())
    lineEditTel.setText(qtab.item(row, 3).text())
    lineEditMail.setText(qtab.item(row, 4).text())

# ----------------------------------------Interface Graphique------------------------------------------------------

app = QApplication([])
fen = QWidget()
fen.setWindowTitle("Carnet")
fen.setGeometry(100, 100, 675, 700)

creer_carnet()

# Entrer
lineEditNom = QLineEdit(fen)
lineEditNom.setGeometry(25, 50, 120, 30)
lineEditNom.setPlaceholderText("Nom")

lineEditPreNom = QLineEdit(fen)
lineEditPreNom.setGeometry(150, 50, 120, 30)
lineEditPreNom.setPlaceholderText("Prenom")

lineEditTel = QLineEdit(fen)
lineEditTel.setGeometry(275, 50, 120, 30)
lineEditTel.setPlaceholderText("Telephone")

lineEditMail = QLineEdit(fen)
lineEditMail.setGeometry(400, 50, 120, 30)
lineEditMail.setPlaceholderText("Mail")

# Insert button
btnInserer = QPushButton("Inserer", fen)
btnInserer.setGeometry(550, 50, 100, 30)
btnInserer.clicked.connect(inserer_contact)

# Table
qtab = QTableWidget(fen)
qtab.setGeometry(25, 150, 625, 500)
qtab.cellClicked.connect(getClickedCell)

# Supprimer par ID
lineEditID = QLineEdit(fen)
lineEditID.setGeometry(450, 100, 70, 30)
lineEditID.setPlaceholderText("ID")

btnSupprimer = QPushButton("Supprimer", fen)
btnSupprimer.setGeometry(550, 100, 100, 30)
btnSupprimer.clicked.connect(supprimer_contact)

# Modifier
btnModifier = QPushButton("Modifier", fen)
btnModifier.setGeometry(25, 100, 100, 30)
btnModifier.clicked.connect(modifier_contact)


afficher_carnet()
fen.show()
app.exec()
