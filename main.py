from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3
import random
import easygui
import datetime
import pyautogui

database=sqlite3.connect("Data.db")
cursor=database.cursor()
cursor.execute("""create table if not exists users(id,name,pwd)""")
cursor.execute("""create table if not exists client(id,createdon,path,name,identitycard,phonenumber,age,room,services,date,note)""")


class school(QtWidgets.QMainWindow):
    def __init__(self):
        super(school, self).__init__()
        uic.loadUi("wassim.ui", self)

        self.showMaximized()
        self.setWindowTitle("manar")
        self.pushButton_signup.clicked.connect(self.signup)
        self.pushButton_5.clicked.connect(self.clearValues)
        self.pushButton_13.clicked.connect(self.import_pic)
        self.pushButton_14.clicked.connect(self.importt)
        self.frame_6.hide()
        self.label_16.hide()
        self.toolButton_11.clicked.connect(self.goToAddClient)
        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_10.clicked.connect(self.insertdata)
        self.pushButton_9.clicked.connect(self.clearData)
        self.showData()

        self.lineEdit.textChanged.connect(self.search)
        self.RisingAcademyBtn.clicked.connect(self.login)

        self.tableWidget.doubleClicked.connect(self.passData)
        self.label_27.hide()
        self.label_24.hide()
        self.tableWidget.setColumnHidden(0,True)
        self.tableWidget.setColumnHidden(1,True)
        self.tableWidget.setColumnHidden(2,True)

        self.pushButton_11.clicked.connect(self.updateData)
        self.toolButton_8.hide()
        self.tableWidget.clicked.connect(self.ShowDeleteToolBtn)
        self.dockWidget_2.hide()
        self.toolButton_8.clicked.connect(self.showdok)
        self.pushButton_15.clicked.connect(self.deleteClient)
        self.x()

        
    def x(self):
        cursor.execute("select COUNT(*) from client")
        data=cursor.fetchall()[0][0]
        self.lcdNumber.display(str(data))
        self.progressBar.setValue(data)
        print(data)

    def showdok(self):
        self.dockWidget_2.show()


    def ShowDeleteToolBtn(self):
        self.toolButton_8.show()

    def deleteClient(self):
        row=self.tableWidget.currentRow()
        Id=self.tableWidget.item(row,0).text()
        cursor.execute(f""" delete from client where id="{Id}" """)
        database.commit()
        self.showData()


    def signup(self):
        Id=random.randrange(1000000000000)
        name=self.lineEdit_3.text()
        pwd=self.lineEdit_4.text()

        cursor.execute(f"""select COUNT(*) from users where name="{name}" """)
        data2=cursor.fetchall()[0][0]
        cursor.execute(f"""select COUNT(*) from users where pwd="{pwd}" """)
        data3=cursor.fetchall()[0][0]
        cursor.execute(f"""select COUNT(*) from users where id="{Id}" """)
        data4=cursor.fetchall()[0][0]
        if data3>0:
            self.label_7.setText("password allready exists")
        elif data2>0:
            self.label_7.setText("user name exists")
        elif data4>0:
            self.label_7.setText("id already exists")
        else:
            if name=="":
                self.label_7.setText("enter ur username")
            elif pwd=="":
                self.label_7.setText("enter ur pwd")
            else:            
                cursor.execute(f"""insert into users values("{Id}","{name}","{pwd}")""")
                database.commit()
                self.label_7.clear()


    def clearValues(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()


    def import_pic(self):
        path=easygui.fileopenbox()
        image=QtGui.QPixmap(path)
        self.label_15.setPixmap(image)
        self.label_16.setText(path)



    def importt(self):
        path=easygui.fileopenbox()
        image=QtGui.QPixmap(path)
        self.label_23.setPixmap(image)
        self.label_24.setText(path)
        
    def goToAddClient(self):
        self.stackedWidget.setCurrentIndex(1)


    def insertdata(self):
        Id=random.randrange(1000000000000)
        createdon=datetime.date.today()
        name=self.lineEdit_7.text()
        identitycard=self.spinBox_2.value()
        phonenumber="0"+str(self.spinBox.value())
        age=self.spinBox_3.value()
        room=self.spinBox_4.value()
        service=self.comboBox_2.currentText()
        date=self.dateEdit.date().toString("yyyy-MM-dd")
        note=self.textEdit.toPlainText()
        path=self.label_16.text()

        cursor.execute(f"""insert into client values ("{Id}","{createdon}","{path}","{name}","{identitycard}","{phonenumber}","{age}","{room}","{service}","{date}","{note}")""")
        database.commit()
        self.showData()
        self.stackedWidget.setCurrentIndex(0)
        self.clearData()





    def clearData(self):
        try:
            self.lineEdit_7.clear()
            self.spinBox_2.setValue(0)
            self.spinBox.setValue(0)
            self.spinBox_3.setValue(0)
            self.spinBox_4.setValue(0)
            self.comboBox_2.setCurrentIndex(0)
            today=datetime.date.today()
            self.dateEdit.setDate(today)
            self.textEdit.clear()
            self.label_16.clear()

            image=QtGui.QPixmap("images/f9edc9fa-e589-4547-85c3-1c4822da8301-removebg-preview.png")
            self.label_15.setPixmap(image)
        except Exception as error:
            print("clearData error 1",error)

        
        
        
        





    def showData(self):
        try:
            cursor.execute("select * from client")
            self.Thesame()
        except Exception as error:
            print("clearData error 1",error)

    def Thesame(self):
        data=cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for i, values in enumerate(data):
            self.tableWidget.insertRow(i)
            for j, value in enumerate(values):
                self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(value)))


        

    def search(self):
        try:
            search=self.lineEdit.text()
            cursor.execute(f"""select * from client where name like "%{search}%" or
                                                            id like "%{search}%" or
                                                            phonenumber like "%{search}%" """)
            self.Thesame()
        except Exception as error:
            pyautogui.alert(error)

        
    

    def login(self):
        name=self.lineEdit_6.text()
        pwd=self.lineEdit_2.text()
        cursor.execute(f"""select * from users where name="{name}" and
                                                    pwd ="{pwd}" """)
        data=cursor.fetchone()
        if data:
            self.stackedWidget.setCurrentIndex(0)
            self.frame_4.setStyleSheet("""border:2px solid #c8c8c8;
            border-radius:10px;
            background-color: rgb(221, 221, 221);""")

            self.frame_5.setStyleSheet("""  border:2px solid #c8c8c8;
                                            border-radius:10px;
                                            background-color: rgb(221, 221, 221);""")
        else:
            self.frame_4.setStyleSheet("""
                border:2px solid red;
                border-radius:10px;
                background-color: rgb(221, 221, 221);
                """)


            self.frame_5.setStyleSheet("""  border:2px solid red;
                                            border-radius:10px;
                                            background-color: rgba(255, 0, 0,10);""")
        



    def passData(self):
        self.stackedWidget.setCurrentIndex(2)
        row=self.tableWidget.currentRow()
        Id=self.tableWidget.item(row,0).text()
        
        self.label_27.setText(Id)

        path=self.tableWidget.item(row,2).text()
        self.label_24.setText(path)

        image=QtGui.QPixmap(path)
        self.label_23.setPixmap(image)
        
        name=self.tableWidget.item(row,3).text()
        self.lineEdit_8.setText(name)

        identitycard=self.tableWidget.item(row,4).text()
        self.lineEdit_14.setText(identitycard)

        phonenumber=self.tableWidget.item(row,5).text()
        self.lineEdit_13.setText(phonenumber)
           
        age=self.tableWidget.item(row,6).text()
        self.lineEdit_12.setText(age)


    def updateData(self):
        Id=self.label_27.text()
        path=self.label_24.text()
        name=self.lineEdit_8.text()
        identitycard=self.lineEdit_14.text()
        phonenumber=self.lineEdit_13.text()
        age=self.lineEdit_12.text()
        room=self.lineEdit_11.text()
        service=self.lineEdit_15.text()
        inscriptiondate=self.lineEdit_16.text()
        note=self.textEdit_2.toPlainText()
        cursor.execute(f"""update client set name="{name}",
                                            path="{path}",
                                            identitycard="{identitycard}",
                                            phonenumber="{phonenumber}",
                                            age="{age}",
                                            room="{room}",
                                            services="{service}",
                                            date="{inscriptiondate}",
                                            note="{note}"

                                            where id="{Id}" """)
        database.commit()
        self.showData()
        self.stackedWidget.setCurrentIndex(0)
        
















































































































































    def tst(self):
        
        pyautogui.alert("Succès..")
        self.progressBar.setValue(5)
        self.lcdNumber.display("55")
        































if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = school()
    window.show()
    sys.exit(app.exec_())

