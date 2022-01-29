# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_video.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


from youder.ui import resources_rc

class Ui_widget_main(object):
    def setupUi(self, widget_main):
        if not widget_main.objectName():
            widget_main.setObjectName(u"widget_main")
        widget_main.resize(452, 222)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_main.sizePolicy().hasHeightForWidth())
        widget_main.setSizePolicy(sizePolicy)
        widget_main.setMaximumSize(QSize(483, 245))
        self.verticalLayout = QVBoxLayout(widget_main)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(10, 1, 0, 10)
        self.frame_main_history = QFrame(widget_main)
        self.frame_main_history.setObjectName(u"frame_main_history")
        sizePolicy.setHeightForWidth(self.frame_main_history.sizePolicy().hasHeightForWidth())
        self.frame_main_history.setSizePolicy(sizePolicy)
        self.frame_main_history.setFrameShape(QFrame.NoFrame)
        self.frame_main_history.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main_history)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_up = QFrame(self.frame_main_history)
        self.frame_up.setObjectName(u"frame_up")
        self.frame_up.setMaximumSize(QSize(483, 195))
        self.frame_up.setFrameShape(QFrame.StyledPanel)
        self.frame_up.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_up)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_thumbnail = QFrame(self.frame_up)
        self.frame_thumbnail.setObjectName(u"frame_thumbnail")
        self.frame_thumbnail.setFrameShape(QFrame.StyledPanel)
        self.frame_thumbnail.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_thumbnail)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 0, 0)
        self.thumbnail = QLabel(self.frame_thumbnail)
        self.thumbnail.setObjectName(u"thumbnail")

        self.horizontalLayout_2.addWidget(self.thumbnail)


        self.horizontalLayout.addWidget(self.frame_thumbnail)

        self.frame_left_bottom = QFrame(self.frame_up)
        self.frame_left_bottom.setObjectName(u"frame_left_bottom")
        self.frame_left_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_left_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_bottom)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title_label = QLabel(self.frame_left_bottom)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setFamily(u"Product Sans")
        font.setPointSize(13)
        self.title_label.setFont(font)
        self.title_label.setTextFormat(Qt.RichText)
        self.title_label.setScaledContents(True)
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.title_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.title_label)


        self.horizontalLayout.addWidget(self.frame_left_bottom)


        self.verticalLayout_2.addWidget(self.frame_up)

        self.frame_down = QFrame(self.frame_main_history)
        self.frame_down.setObjectName(u"frame_down")
        self.frame_down.setMinimumSize(QSize(0, 50))
        self.frame_down.setMaximumSize(QSize(483, 50))
        self.frame_down.setFrameShape(QFrame.StyledPanel)
        self.frame_down.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_down)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.delete_button = QPushButton(self.frame_down)
        self.delete_button.setObjectName(u"delete_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/history/icons/white/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon)
        self.delete_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.delete_button)

        self.youtube = QPushButton(self.frame_down)
        self.youtube.setObjectName(u"youtube")
        sizePolicy1.setHeightForWidth(self.youtube.sizePolicy().hasHeightForWidth())
        self.youtube.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/youtube_icon/icons/black/youtube_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.youtube.setIcon(icon1)
        self.youtube.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.youtube)

        self.run = QPushButton(self.frame_down)
        self.run.setObjectName(u"run")
        sizePolicy1.setHeightForWidth(self.run.sizePolicy().hasHeightForWidth())
        self.run.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/history/icons/white/reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.run.setIcon(icon2)
        self.run.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.run)

        self.play = QPushButton(self.frame_down)
        self.play.setObjectName(u"play")
        sizePolicy1.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u":/history/icons/white/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play.setIcon(icon3)
        self.play.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.play)

        self.open = QPushButton(self.frame_down)
        self.open.setObjectName(u"open")
        sizePolicy1.setHeightForWidth(self.open.sizePolicy().hasHeightForWidth())
        self.open.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/history/icons/white/folder_new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open.setIcon(icon4)
        self.open.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.open)


        self.verticalLayout_2.addWidget(self.frame_down)


        self.verticalLayout.addWidget(self.frame_main_history)


        self.retranslateUi(widget_main)

        QMetaObject.connectSlotsByName(widget_main)
    # setupUi

    def retranslateUi(self, widget_main):
        widget_main.setWindowTitle(QCoreApplication.translate("widget_main", u"Form", None))
        self.thumbnail.setText(QCoreApplication.translate("widget_main", u"TextLabel", None))
        self.title_label.setText(QCoreApplication.translate("widget_main", u"You Der is Free Open Sourced Youtube video downloader by Open utilites.....", None))
        self.delete_button.setText("")
        self.youtube.setText("")
        self.run.setText("")
        self.play.setText("")
        self.open.setText("")
    # retranslateUi

