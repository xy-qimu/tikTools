import sys
import pandas as pd
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from tikToolsUI import Ui_MainWindow
from tools import genDDL_mysql, genSelect


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])



# 自定义一个窗口类
class TikTools(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()   # 调用父类的构造方法
        icon = QIcon(r"D:\Desktop\HubCode\pycharm\tikTools\icon.png")   # pyinstaller在打包成exe时, 需使用绝对路径才能生效
        self.setWindowIcon(icon)
        self.setupUi(self)   # 初始化构造界面
        self.btn_select_file.clicked.connect(self.open_excel_file)    # 事件绑定
        self.btn_gen_ddl.clicked.connect(self.gen_ddl_content)        # 事件绑定
        self.radioBtn_msql.clicked.connect(self.set_db_type_msql)
        self.radioBtn_psql.clicked.connect(self.set_db_type_psql)
        self.menu_about.triggered.connect(self.about_info)

        self.btn_gen_select.clicked.connect(self.gen_select_content)
        self.db_type = 'psql'

    def open_excel_file(self):
        home_dir =  self.txt_file_name.text()
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir,filter="Excel Files (*.xlsx)")

        if self.fname[0]:
            self.txt_file_name.setText(self.fname[0])

            df = pd.read_excel(self.fname[0],sheet_name='目录',usecols=[0,3,4,5],nrows=21)
            df.dropna(subset=['表名'],inplace=True)
            df.index = df.index + 1
            self.model = TableModel(df)
            self.table_file_content.setModel(self.model)

            header = self.table_file_content.horizontalHeader()
            font = QFont()
            font.setBold(True)

            header.setFont(font)

    def gen_ddl_content(self):
        fname = self.fname[0]
        if self.db_type == 'psql':
            sql_content = genDDL_psql.gen_ddl(fname)
        else:
            sql_content = genDDL_mysql.gen_ddl(fname)

        self.txt_ddl_content.setText(sql_content)
        QMessageBox.information(self, "成功提示！", sql_content[:25])

    def about_info(self):
        QMessageBox.information(self, "关于", f"""Author：tik.xie\nVersion：v1.1""")

    def gen_select_content(self):
        sql = genSelect.gen_select()
        self.txt_gen_select.setText(sql)

    def set_db_type_psql(self):
        self.db_type = 'psql'

    def set_db_type_msql(self):
        self.db_type = 'msql'

# 主程序入口
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = TikTools()
    window.show()

    sys.exit(app.exec())