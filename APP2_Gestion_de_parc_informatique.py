# Importer les packages
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox

# ----------------------------------------------Les fonctions-------------------------------------------------------
# creer la base do donnees et la table
def creer_parc():
    conn = sqlite3.connect("parc.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Pc(ID int,Marque varchar(255),OS varchar(255),Locale varchar(255));""")
    conn.commit()
    conn.close()

# Ajouter un Pc dans le parque
def inserer_Pc():
    if not lineEditId.text() or not lineEditMarque.text() or not lineEditOS.text() or not lineEditLocale.text():
        QMessageBox.critical(fen, "Erreur", "Tous les champs doivent être remplis !")
        return
    try:
        IDs = int(lineEditId.text())
        if IDs <= 0:
            QMessageBox.critical(fen, "Erreur", "Le ID (numéro d'identification) doit être un nombre positif !")
            return
    except ValueError:
        QMessageBox.critical(fen, "Erreur", "Le ID (numéro d'identification) doit être un nombre entier !")
        return
    conn = sqlite3.connect("parc.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Pc (ID, Marque, OS, Locale)VALUES (?, ?, ?, ?)""", (IDs,lineEditMarque.text(),lineEditOS.text(),lineEditLocale.text()))
    conn.commit()
    conn.close()
    afficher_parc()
    QMessageBox.information(fen, "Succès", "Le poste informatique a été ajouté avec succès !")


# Supprimer un PC dans le parc
def supprimer_Pc():
    conn = sqlite3.connect("parc.db")
    cursor = conn.cursor()
    try:
        deleted_id = int(lineEditIdAct.text())
    except ValueError:
        QMessageBox.critical(fen, "Erreur", "L'ID doit être un nombre entier !")
        conn.close()
        return
    cursor.execute("DELETE FROM Pc WHERE ID = ?", (deleted_id,))
    if cursor.rowcount == 0:
        QMessageBox.critical(fen, "Erreur", "Entrer un ID correct !")
        conn.close()
        return
    conn.commit()
    conn.close()
    afficher_parc()
    QMessageBox.information(fen, "Succès", "Le Contact a été supprimer avec succès !")

# modifier un PC dans le parc
def modifier_Pc():
    if not lineEditId.text() or not lineEditMarque.text() or not lineEditOS.text() or not lineEditLocale.text() :
        QMessageBox.critical(fen, "Erreur", "Tous les champs doivent être remplis !")
        return
    try:
        ID = int(lineEditId.text())
        if ID <= 0:
            QMessageBox.critical(fen, "Erreur", "le ID(numéro d'identification) doit etre un nombre positif !")
            return
    except ValueError:
        QMessageBox.critical(fen, "Erreur", "Le ID (numéro d'identification) doit etre un nombre entier !")
        return
    conn = sqlite3.connect("parc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT ID FROM Pc")
    max_id = cursor.fetchone()[0]
    try:
        deleted_id = int(lineEditIdAct.text())
    except ValueError:
        QMessageBox.critical(fen, "Erreur", "L'ID doit etre un nombre entier !")
        return
    if deleted_id <= 0 or deleted_id > max_id:
        QMessageBox.critical(fen, "Erreur", "Entrer un ID correct !")
        return
    else :
        cursor.execute("""UPDATE Pc SET Marque=?, OS=?, Locale=?  WHERE ID=?""",(lineEditMarque.text(),lineEditOS.text(),lineEditLocale.text(),lineEditId.text()))
        conn.commit()
        conn.close()
        afficher_parc()
        QMessageBox.information(fen, "Succès", "Le poste informatique a été modifier avec succès !")

# Afficher le parc
def afficher_parc():
    conn = sqlite3.connect("parc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pc")
    resultat = cursor.fetchall()
    conn.close()
    qtab.setRowCount(len(resultat))
    qtab.setColumnCount(4)
    qtab.setHorizontalHeaderLabels(['ID', 'Marque', 'OS', 'Locale'])
    # La Taille Des colonnes
    qtab.setColumnWidth(0, 50)
    qtab.setColumnWidth(1, 120)
    qtab.setColumnWidth(2, 120)
    qtab.setColumnWidth(3, 160)
    for i in range(len(resultat)):
        for j in range(4):
            qtab.setItem(i, j, QTableWidgetItem(str(resultat[i][j])))

# Recuperer les ligne pour le tableau
def getClickedCell(row, column):
    lineEditId.setText(qtab.item(row, 0).text())
    lineEditMarque.setText(qtab.item(row, 1).text())
    lineEditOS.setText(qtab.item(row, 2).text())
    lineEditLocale.setText(qtab.item(row, 3).text())

# --------------------------------------L'Interface Graphique---------------------------------------------------

app = QApplication([])
fen = QWidget()
fen.setWindowTitle("Parc Informatique")
fen.setGeometry(100, 100, 675, 700)

creer_parc()

# Insert
lineEditId = QLineEdit(fen)
lineEditId.setGeometry(25, 50, 120, 30)
lineEditId.setPlaceholderText("Id")

lineEditMarque = QLineEdit(fen)
lineEditMarque.setGeometry(150, 50, 120, 30)
lineEditMarque.setPlaceholderText("Marque")

lineEditOS = QLineEdit(fen)
lineEditOS.setGeometry(275, 50, 120, 30)
lineEditOS.setPlaceholderText("OS")

lineEditLocale = QLineEdit(fen)
lineEditLocale.setGeometry(400, 50, 120, 30)
lineEditLocale.setPlaceholderText("Local")

# Table
qtab = QTableWidget(fen)
qtab.setGeometry(25, 150, 625, 500)
qtab.cellClicked.connect(getClickedCell)

# Insert button
btnInserer = QPushButton("Inserer", fen)
btnInserer.setGeometry(550, 50, 100, 30)
btnInserer.clicked.connect(inserer_Pc)

# Supprimer/Modifier ID
lineEditIdAct = QLineEdit(fen)
lineEditIdAct.setGeometry(450, 100, 70, 30)
lineEditIdAct.setPlaceholderText("ID")

# Supprimer btn
btnSupprimer = QPushButton("Supprimer", fen)
btnSupprimer.setGeometry(550, 100, 100, 30)
btnSupprimer.clicked.connect(supprimer_Pc)

# Modifier btn
btnModifier = QPushButton("Modifier", fen)
btnModifier.setGeometry(25, 100, 100, 30)
btnModifier.clicked.connect(modifier_Pc)

afficher_parc()
fen.show()
app.exec()
