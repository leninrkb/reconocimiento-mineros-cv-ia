from app_escritorio.conexionBD import Datos
from app_escritorio.components import components

from PyQt5.QtGui  import QIcon, QFont, QTextDocument
from PyQt5.QtCore import Qt, QTextCodec, QByteArray, QTranslator, QLocale, QLibraryInfo
from PyQt5.QtWidgets import (QApplication, QTreeWidgetItem, QDialog, QPushButton, QTableWidget, QFileDialog,
                             QMessageBox, QToolBar,QTableWidgetItem, QAbstractItemView)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PIL import Image

# =============== CLASE visualizarImprimirExportar =================

class visualizarImprimirExportar(QDialog):
    def __init__(self, parent=None):
        super(visualizarImprimirExportar, self).__init__()
        
        self.setWindowTitle("Visualizar Datos y Exportar a PDF")
        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(721, 700)

        self.initUI()

    def initUI(self):
        self.documento = QTextDocument()

      # =================== WIDGETS QPUSHBUTTON ==================

        '''buttonBuscar = QPushButton("Buscar empleados", self)
        buttonBuscar.setFixedSize(426, 26)
        buttonBuscar.move(20, 20)

        buttonLimpiar = QPushButton("Limpiar tabla", self)
        buttonLimpiar.setFixedSize(140, 26)
        buttonLimpiar.move(452, 20)'''

    # =================== WIDGET QTABLEWIDGET ===================
        self.tableWidget = QTableWidget(self)

      # =================== WIDGETS QPUSHBUTTON ==================

        buttonVistaPrevia = QPushButton("Vista previa", self)
        buttonVistaPrevia.setFixedSize(140, 26)
        buttonVistaPrevia.move(156, 565)

        buttonImprimir = QPushButton("Imprimir", self)
        buttonImprimir.setFixedSize(140, 26)
        buttonImprimir.move(304, 565)

        buttonExportarPDF = QPushButton("Exportar a PDF", self)
        buttonExportarPDF.setFixedSize(140, 26)
        buttonExportarPDF.move(452, 565)

      # =================== EVENTOS QPUSHBUTTON ==================

        #llamado para buscar
        #buttonBuscar.clicked.connect(self.Buscar)
        #buttonLimpiar.clicked.connect(self.limpiarTabla)
        
        buttonVistaPrevia.clicked.connect(self.vistaPrevia)
        buttonImprimir.clicked.connect(self.Imprimir)
        buttonExportarPDF.clicked.connect(self.exportarPDF)

  # ======================= FUNCIONES ============================
    def configurar_Tabla(self):
        colum_labels = ("Cédula", "Nombre", "Apellido", "Fecha y Hora de Ingreso", "Evidencia")
        self.tableWidget.setColumnCount(len(colum_labels))
        self.tableWidget.setHorizontalHeaderLabels(colum_labels)
        self.tableWidget.setColumnWidth(4,200)
        self.tableWidget.verticalHeader().setDefaultSectionSize(150)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setFixedSize(721,500 )

    def llenar_Tabla(self):
        bd = Datos()
        results = bd.obtenerRegistroEmpleado()
        self.tableWidget.setRowCount(len(results))
        datos = ""

        for (index_row, row) in enumerate(results): 
            datos += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><img src='%s' style='width:50px;height:50px;'></td></tr>" %row
            for (index_cell, cell) in enumerate(row):
                if index_cell == 4:
                    self.tableWidget.setCellWidget(
                        index_row, index_cell,components.ReporteImg(cell)
                    )
                else:
                    self.tableWidget.setItem(
                        index_row, index_cell, QTableWidgetItem(str(cell))
                    )
        reporteHtml = """
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset="UTF-8">
            <style>
            h3 {
                font-family: Helvetica-Bold;
                text-align: center;
            }
            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
                }
            td {
                text-align: left;
                padding-top: 4px;
                padding-right: 6px;
                padding-bottom: 2px;
                padding-left: 6px;
            }
            th {
                text-align: left;
                padding: 4px;
                background-color: #6ba52a;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #dddddd;
            }
            </style>
            </head>

            <body>
            <header>
                <img src="img/logo.jpg" width="800" height="70"/>
            </header>

            <h3>Reportes Empleados<br/></h3>

            <table align="left" width="100%" cellspacing="0">
            <tr>
                <th>Cédula</th>
                <th>Nombre</th>
                <th>Apellido</th>
                <th>Fecha y Hora de Ingreso</th>
                <th>Evidencia de Ingreso</th>
            </tr>
            [DATOS]
            </table>

            </body>
            </html>
""".replace("[DATOS]", datos)

        datos = QByteArray()
        datos.append(str(reporteHtml))
        codec = QTextCodec.codecForHtml(datos)
        unistr = codec.toUnicode(datos)

        if Qt.mightBeRichText(unistr):
            self.documento.setHtml(unistr)
        else:
            self.documento.setPlainText(unistr)

    def limpiarTabla(self):
        self.documento.clear()
        self.treeWidgetUsuarios.clear()

    def vistaPrevia(self):
        if not self.documento.isEmpty():
            impresion = QPrinter(QPrinter.HighResolution)
            
            vista = QPrintPreviewDialog(impresion, self)
            vista.setWindowTitle("Vista previa")
            vista.setWindowFlags(Qt.Window)
            vista.resize(1000, 600)

            exportarPDF = vista.findChildren(QToolBar)
            exportarPDF[0].addAction(QIcon("exportarPDF.png"), "Exportar a PDF", self.exportarPDF)
            
            vista.paintRequested.connect(self.vistaPreviaImpresion)
            vista.exec_()
        else:
            QMessageBox.critical(self, "Vista previa", "No hay datos para visualizar.   ",
                                 QMessageBox.Ok)

    def vistaPreviaImpresion(self, impresion):
        self.documento.print_(impresion)

    def Imprimir(self):
        if not self.documento.isEmpty():
            impresion = QPrinter(QPrinter.HighResolution)
            
            dlg = QPrintDialog(impresion, self)
            dlg.setWindowTitle("Imprimir documento")

            if dlg.exec_() == QPrintDialog.Accepted:
                self.documento.print_(impresion)

            del dlg
        else:
            QMessageBox.critical(self, "Imprimir", "No hay datos para imprimir.   ",
                                 QMessageBox.Ok)

    def exportarPDF(self):
        if not self.documento.isEmpty():
            nombreArchivo, _ = QFileDialog.getSaveFileName(self, "Exportar a PDF", "Listado de empleados",
                                                           "Archivos PDF (*.pdf);;All Files (*)",
                                                           options=QFileDialog.Options())

            if nombreArchivo:
                # if QFileInfo(nombreArchivo).suffix():
                #     nombreArchivo += ".pdf"

                impresion = QPrinter(QPrinter.HighResolution)
                impresion.setOutputFormat(QPrinter.PdfFormat)
                impresion.setOutputFileName(nombreArchivo)
                self.documento.print_(impresion)

                QMessageBox.information(self, "Exportar a PDF", "Datos exportados con éxito.   ",
                                        QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Exportar a PDF", "No hay datos para exportar.   ",
                                 QMessageBox.Ok)


# ================================================================   

if __name__ == '__main__':

    import sys

    aplicacion = QApplication(sys.argv)

    qt_traductor = QTranslator()
    qt_traductor.load("qtbase_" + QLocale.system().name(),
                       QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    aplicacion.installTranslator(qt_traductor)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")

    aplicacion.setFont(fuente)
    
    ventana = visualizarImprimirExportar()
    #ventana.Buscar()
    ventana.configurar_Tabla()
    ventana.llenar_Tabla()
    ventana.show()
    

    sys.exit(aplicacion.exec_())