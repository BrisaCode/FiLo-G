'''
File Loader G
June 22, 2015
@author: Lucas Cotta

Main program to the File Loader G application V0.1
'''

import sys 
import os
import copy

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QMessageBox, QScrollArea

from main_window import Ui_FileLoaderG


# class for the main window
#
class Main(QtGui.QMainWindow):
    def __init__(self):

        QtGui.QMainWindow.__init__(self)
        # user interface
        #
        self.flg = Ui_FileLoaderG()
        self.flg.setupUi(self)

        # get the current path of the server directory
        #
        self.server_directory = (str(sys.argv[0])) + "/server"

        # get the current path of local directory
        #
        self.local_directory = (str(sys.argv[0])) + "/local"

            
# main function
def main():
    
    app = QtGui.QApplication([])
    window = Main()
    window.show()
    QtGui.QApplication.instance().exec_()

    # remove segmentation fault
    #
    os._exit(0)

# run the main function
if __name__ == "__main__":
    main()



