from UI.Ui_job_table_view import Ui_Form
from PyQt5 import QtWidgets as qtw

class Table_view(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


if __name__=='__main__':
    # w = qtw.QWidget()
    # test =  Class_TableView()
    # test.setupUi(w)

    w = qtw.QWidget()  # we must know the exact class, generated by QtDesigner
    gw = Ui_Form()
    gw.setupUi(w)
    # w.show()

