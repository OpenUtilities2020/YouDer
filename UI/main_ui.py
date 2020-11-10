# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_YouDer(object):
    def setupUi(self, YouDer):
        if not YouDer.objectName():
            YouDer.setObjectName(u"YouDer")
        YouDer.resize(1614, 526)
        self.centralwidget = QWidget(YouDer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_base = QFrame(self.centralwidget)
        self.frame_base.setObjectName(u"frame_base")
        self.frame_base.setStyleSheet(u"")
        self.frame_base.setFrameShape(QFrame.NoFrame)
        self.frame_base.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_base)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_base)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 25))
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.frame_top.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(50, 0))
        self.frame_toggle.setMaximumSize(QSize(50, 16777215))
        self.frame_toggle.setStyleSheet(u"")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.frame_toggle.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toggle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.button_toggle = QPushButton(self.frame_toggle)
        self.button_toggle.setObjectName(u"button_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_toggle.sizePolicy().hasHeightForWidth())
        self.button_toggle.setSizePolicy(sizePolicy)
        self.button_toggle.setMinimumSize(QSize(50, 0))
        self.button_toggle.setMaximumSize(QSize(100, 16777215))
        self.button_toggle.setStyleSheet(u"")
        self.button_toggle.setText(u"")
        icon = QIcon()
        icon.addFile(u":/toggle/icons/white/toggle_hor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_toggle.setIcon(icon)
        self.button_toggle.setIconSize(QSize(42, 42))

        self.horizontalLayout_3.addWidget(self.button_toggle)


        self.horizontalLayout_2.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_top_right.sizePolicy().hasHeightForWidth())
        self.frame_top_right.setSizePolicy(sizePolicy1)
        self.frame_top_right.setStyleSheet(u"")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_top_right)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_main = QFrame(self.frame_base)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main_left = QFrame(self.frame_main)
        self.frame_main_left.setObjectName(u"frame_main_left")
        self.frame_main_left.setMinimumSize(QSize(50, 0))
        self.frame_main_left.setMaximumSize(QSize(50, 16777215))
        self.frame_main_left.setFrameShape(QFrame.NoFrame)
        self.frame_main_left.setFrameShadow(QFrame.Raised)
        self.frame_main_left.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_main_left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_for_button = QFrame(self.frame_main_left)
        self.frame_for_button.setObjectName(u"frame_for_button")
        self.frame_for_button.setMinimumSize(QSize(0, 125))
        self.frame_for_button.setFrameShape(QFrame.NoFrame)
        self.frame_for_button.setFrameShadow(QFrame.Raised)
        self.frame_for_button.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_for_button)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.button_home = QPushButton(self.frame_for_button)
        self.button_home.setObjectName(u"button_home")
        sizePolicy.setHeightForWidth(self.button_home.sizePolicy().hasHeightForWidth())
        self.button_home.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Product Sans")
        font.setPointSize(14)
        self.button_home.setFont(font)
        self.button_home.setStyleSheet(u"")
        self.button_home.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/home/icons/white/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_home.setIcon(icon1)
        self.button_home.setIconSize(QSize(36, 36))

        self.verticalLayout_4.addWidget(self.button_home)

        self.button_settings = QPushButton(self.frame_for_button)
        self.button_settings.setObjectName(u"button_settings")
        sizePolicy.setHeightForWidth(self.button_settings.sizePolicy().hasHeightForWidth())
        self.button_settings.setSizePolicy(sizePolicy)
        self.button_settings.setFont(font)
        self.button_settings.setStyleSheet(u"")
        self.button_settings.setText(u"")
        icon2 = QIcon()
        icon2.addFile(u":/settings/icons/white/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_settings.setIcon(icon2)
        self.button_settings.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.button_settings)


        self.verticalLayout_3.addWidget(self.frame_for_button, 0, Qt.AlignTop)

        self.frame_at_middle_of_left = QFrame(self.frame_main_left)
        self.frame_at_middle_of_left.setObjectName(u"frame_at_middle_of_left")
        self.frame_at_middle_of_left.setFrameShape(QFrame.StyledPanel)
        self.frame_at_middle_of_left.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_at_middle_of_left)

        self.frame_for_about_button = QFrame(self.frame_main_left)
        self.frame_for_about_button.setObjectName(u"frame_for_about_button")
        self.frame_for_about_button.setMaximumSize(QSize(16777215, 70))
        self.frame_for_about_button.setFrameShape(QFrame.NoFrame)
        self.frame_for_about_button.setFrameShadow(QFrame.Raised)
        self.frame_for_about_button.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_for_about_button)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.button_about = QPushButton(self.frame_for_about_button)
        self.button_about.setObjectName(u"button_about")
        sizePolicy.setHeightForWidth(self.button_about.sizePolicy().hasHeightForWidth())
        self.button_about.setSizePolicy(sizePolicy)
        self.button_about.setFont(font)
        self.button_about.setStyleSheet(u"")
        self.button_about.setText(u"")
        icon3 = QIcon()
        icon3.addFile(u":/about/icons/white/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_about.setIcon(icon3)
        self.button_about.setIconSize(QSize(36, 36))

        self.verticalLayout_5.addWidget(self.button_about, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.frame_for_about_button)


        self.horizontalLayout.addWidget(self.frame_main_left)

        self.frame_mian_right = QFrame(self.frame_main)
        self.frame_mian_right.setObjectName(u"frame_mian_right")
        self.frame_mian_right.setStyleSheet(u"")
        self.frame_mian_right.setFrameShape(QFrame.NoFrame)
        self.frame_mian_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_mian_right)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pages = QStackedWidget(self.frame_mian_right)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"")
        self.pages.setFrameShadow(QFrame.Raised)
        self.pages.setLineWidth(0)
        self.pages.setMidLineWidth(0)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_7 = QVBoxLayout(self.page_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_home = QFrame(self.page_home)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setStyleSheet(u"")
        self.frame_home.setFrameShape(QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_home)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_home_top = QFrame(self.frame_home)
        self.frame_home_top.setObjectName(u"frame_home_top")
        self.frame_home_top.setMaximumSize(QSize(16777215, 100))
        self.frame_home_top.setFrameShape(QFrame.NoFrame)
        self.frame_home_top.setFrameShadow(QFrame.Raised)
        self.frame_home_top.setLineWidth(0)
        self.layoutWidget = QWidget(self.frame_home_top)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 612, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setSpacing(45)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.button_paste = QPushButton(self.layoutWidget)
        self.button_paste.setObjectName(u"button_paste")
        sizePolicy.setHeightForWidth(self.button_paste.sizePolicy().hasHeightForWidth())
        self.button_paste.setSizePolicy(sizePolicy)
        self.button_paste.setMinimumSize(QSize(80, 30))
        font1 = QFont()
        font1.setFamily(u"Product Sans")
        font1.setPointSize(12)
        self.button_paste.setFont(font1)
        self.button_paste.setStyleSheet(u"")
        self.button_paste.setText(u"Paste")
        icon4 = QIcon()
        icon4.addFile(u":/paste/icons/white/paste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_paste.setIcon(icon4)
        self.button_paste.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.button_paste)

        self.link_linedit = QLineEdit(self.layoutWidget)
        self.link_linedit.setObjectName(u"link_linedit")
        self.link_linedit.setMinimumSize(QSize(350, 25))
        self.link_linedit.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.link_linedit)

        self.button_getinfo = QPushButton(self.layoutWidget)
        self.button_getinfo.setObjectName(u"button_getinfo")
        sizePolicy.setHeightForWidth(self.button_getinfo.sizePolicy().hasHeightForWidth())
        self.button_getinfo.setSizePolicy(sizePolicy)
        self.button_getinfo.setMinimumSize(QSize(90, 30))
        self.button_getinfo.setFont(font1)
        self.button_getinfo.setStyleSheet(u"")
        self.button_getinfo.setText(u"Get Info")
        icon5 = QIcon()
        icon5.addFile(u":/getinfo/icons/white/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_getinfo.setIcon(icon5)
        self.button_getinfo.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.button_getinfo)


        self.verticalLayout_8.addWidget(self.frame_home_top)

        self.frame_home_middle = QFrame(self.frame_home)
        self.frame_home_middle.setObjectName(u"frame_home_middle")
        self.frame_home_middle.setFrameShape(QFrame.NoFrame)
        self.frame_home_middle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_home_middle)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_for_thumbnail = QFrame(self.frame_home_middle)
        self.frame_for_thumbnail.setObjectName(u"frame_for_thumbnail")
        self.frame_for_thumbnail.setMinimumSize(QSize(300, 0))
        self.frame_for_thumbnail.setMaximumSize(QSize(400, 16777215))
        self.frame_for_thumbnail.setFrameShape(QFrame.NoFrame)
        self.frame_for_thumbnail.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_for_thumbnail)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_for_thubnail_label = QFrame(self.frame_for_thumbnail)
        self.frame_for_thubnail_label.setObjectName(u"frame_for_thubnail_label")
        self.frame_for_thubnail_label.setFrameShape(QFrame.StyledPanel)
        self.frame_for_thubnail_label.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_for_thubnail_label)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.thubnail_label = QLabel(self.frame_for_thubnail_label)
        self.thubnail_label.setObjectName(u"thubnail_label")

        self.verticalLayout_10.addWidget(self.thubnail_label)


        self.verticalLayout_9.addWidget(self.frame_for_thubnail_label)

        self.frame_for_views = QFrame(self.frame_for_thumbnail)
        self.frame_for_views.setObjectName(u"frame_for_views")
        self.frame_for_views.setMaximumSize(QSize(16777215, 35))
        self.frame_for_views.setFrameShape(QFrame.StyledPanel)
        self.frame_for_views.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_for_views)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.eye_icon_label = QLabel(self.frame_for_views)
        self.eye_icon_label.setObjectName(u"eye_icon_label")
        self.eye_icon_label.setPixmap(QPixmap(u":/eye/icons/white/eye.png"))
        self.eye_icon_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.eye_icon_label)

        self.views = QLabel(self.frame_for_views)
        self.views.setObjectName(u"views")
        self.views.setFont(font1)
        self.views.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.views)

        self.video_length_icon_label = QLabel(self.frame_for_views)
        self.video_length_icon_label.setObjectName(u"video_length_icon_label")
        self.video_length_icon_label.setPixmap(QPixmap(u":/video_length/icons/white/video_length.png"))
        self.video_length_icon_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.video_length_icon_label)

        self.length_label = QLabel(self.frame_for_views)
        self.length_label.setObjectName(u"length_label")
        self.length_label.setFont(font1)
        self.length_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.length_label)


        self.verticalLayout_9.addWidget(self.frame_for_views)


        self.horizontalLayout_5.addWidget(self.frame_for_thumbnail, 0, Qt.AlignTop)

        self.frame_for_title_and_combo = QFrame(self.frame_home_middle)
        self.frame_for_title_and_combo.setObjectName(u"frame_for_title_and_combo")
        self.frame_for_title_and_combo.setMinimumSize(QSize(400, 0))
        self.frame_for_title_and_combo.setMaximumSize(QSize(450, 16777215))
        font2 = QFont()
        font2.setPointSize(7)
        self.frame_for_title_and_combo.setFont(font2)
        self.frame_for_title_and_combo.setFrameShape(QFrame.NoFrame)
        self.frame_for_title_and_combo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_for_title_and_combo)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_for_title_label = QFrame(self.frame_for_title_and_combo)
        self.frame_for_title_label.setObjectName(u"frame_for_title_label")
        self.frame_for_title_label.setFrameShape(QFrame.NoFrame)
        self.frame_for_title_label.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_for_title_label)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.title_label = QLabel(self.frame_for_title_label)
        self.title_label.setObjectName(u"title_label")
        font3 = QFont()
        font3.setFamily(u"Product Sans")
        font3.setPointSize(13)
        self.title_label.setFont(font3)
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.title_label.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.title_label)


        self.verticalLayout_12.addWidget(self.frame_for_title_label, 0, Qt.AlignTop)

        self.frame_for_combo_box = QFrame(self.frame_for_title_and_combo)
        self.frame_for_combo_box.setObjectName(u"frame_for_combo_box")
        self.frame_for_combo_box.setMaximumSize(QSize(16777215, 35))
        self.frame_for_combo_box.setStyleSheet(u"")
        self.frame_for_combo_box.setFrameShape(QFrame.NoFrame)
        self.frame_for_combo_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_for_combo_box)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.combobox = QComboBox(self.frame_for_combo_box)
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.setObjectName(u"combobox")
        self.combobox.setMinimumSize(QSize(275, 25))
        self.combobox.setMaximumSize(QSize(275, 16777215))
        font4 = QFont()
        font4.setFamily(u"Product Sans")
        font4.setPointSize(10)
        self.combobox.setFont(font4)
        self.combobox.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.combobox)


        self.verticalLayout_12.addWidget(self.frame_for_combo_box, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_5.addWidget(self.frame_for_title_and_combo)


        self.verticalLayout_8.addWidget(self.frame_home_middle, 0, Qt.AlignLeft)

        self.frame_home_bottom = QFrame(self.frame_home)
        self.frame_home_bottom.setObjectName(u"frame_home_bottom")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_home_bottom.sizePolicy().hasHeightForWidth())
        self.frame_home_bottom.setSizePolicy(sizePolicy2)
        self.frame_home_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_home_bottom.setFrameShadow(QFrame.Raised)
        self.frame_home_bottom.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_home_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_for_progress = QFrame(self.frame_home_bottom)
        self.frame_for_progress.setObjectName(u"frame_for_progress")
        self.frame_for_progress.setMinimumSize(QSize(0, 0))
        self.frame_for_progress.setMaximumSize(QSize(16777215, 250))
        self.frame_for_progress.setFrameShape(QFrame.NoFrame)
        self.frame_for_progress.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_for_progress)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalSpacer_5 = QSpacerItem(67, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.horizontalSpacer_5)

        self.frame_for_progress_top = QFrame(self.frame_for_progress)
        self.frame_for_progress_top.setObjectName(u"frame_for_progress_top")
        sizePolicy1.setHeightForWidth(self.frame_for_progress_top.sizePolicy().hasHeightForWidth())
        self.frame_for_progress_top.setSizePolicy(sizePolicy1)
        self.frame_for_progress_top.setStyleSheet(u"")
        self.frame_for_progress_top.setFrameShape(QFrame.NoFrame)
        self.frame_for_progress_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_for_progress_top)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.status_bar = QLabel(self.frame_for_progress_top)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setMinimumSize(QSize(400, 0))
        font5 = QFont()
        font5.setFamily(u"Product Sans")
        font5.setPointSize(11)
        self.status_bar.setFont(font5)
        self.status_bar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.status_bar.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.status_bar)

        self.progressbar = QProgressBar(self.frame_for_progress_top)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setMinimumSize(QSize(150, 0))
        self.progressbar.setMaximumSize(QSize(200, 16777215))
        self.progressbar.setStyleSheet(u"")
        self.progressbar.setValue(54)
        self.progressbar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.progressbar)


        self.verticalLayout_25.addWidget(self.frame_for_progress_top)


        self.horizontalLayout_7.addWidget(self.frame_for_progress)

        self.frame_for_download = QFrame(self.frame_home_bottom)
        self.frame_for_download.setObjectName(u"frame_for_download")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_for_download.sizePolicy().hasHeightForWidth())
        self.frame_for_download.setSizePolicy(sizePolicy3)
        self.frame_for_download.setMaximumSize(QSize(300, 16777215))
        self.frame_for_download.setFrameShape(QFrame.StyledPanel)
        self.frame_for_download.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_for_download)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_for_save_as = QFrame(self.frame_for_download)
        self.frame_for_save_as.setObjectName(u"frame_for_save_as")
        self.frame_for_save_as.setFrameShape(QFrame.StyledPanel)
        self.frame_for_save_as.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_for_save_as)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.save_as_label = QLabel(self.frame_for_save_as)
        self.save_as_label.setObjectName(u"save_as_label")
        self.save_as_label.setFont(font4)

        self.horizontalLayout_10.addWidget(self.save_as_label)

        self.save_as_linedit = QLineEdit(self.frame_for_save_as)
        self.save_as_linedit.setObjectName(u"save_as_linedit")
        self.save_as_linedit.setMinimumSize(QSize(150, 0))
        self.save_as_linedit.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.save_as_linedit)

        self.toolButton = QToolButton(self.frame_for_save_as)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.toolButton)


        self.verticalLayout_14.addWidget(self.frame_for_save_as)

        self.frame_for_download_button = QFrame(self.frame_for_download)
        self.frame_for_download_button.setObjectName(u"frame_for_download_button")
        self.frame_for_download_button.setMaximumSize(QSize(16777215, 150))
        self.frame_for_download_button.setFrameShape(QFrame.StyledPanel)
        self.frame_for_download_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_for_download_button)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(269, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.download_button = QPushButton(self.frame_for_download_button)
        self.download_button.setObjectName(u"download_button")
        sizePolicy.setHeightForWidth(self.download_button.sizePolicy().hasHeightForWidth())
        self.download_button.setSizePolicy(sizePolicy)
        self.download_button.setMinimumSize(QSize(150, 45))
        self.download_button.setMaximumSize(QSize(150, 50))
        self.download_button.setFont(font1)
        self.download_button.setStyleSheet(u"")
        self.download_button.setText(u"Download")
        icon6 = QIcon()
        icon6.addFile(u":/download/icons/white/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.download_button.setIcon(icon6)
        self.download_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.download_button)


        self.verticalLayout_14.addWidget(self.frame_for_download_button, 0, Qt.AlignBottom)


        self.horizontalLayout_7.addWidget(self.frame_for_download)


        self.verticalLayout_8.addWidget(self.frame_home_bottom)


        self.verticalLayout_7.addWidget(self.frame_home)

        self.pages.addWidget(self.page_home)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_15 = QVBoxLayout(self.page_settings)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_settings_main = QFrame(self.page_settings)
        self.frame_settings_main.setObjectName(u"frame_settings_main")
        self.frame_settings_main.setStyleSheet(u"")
        self.frame_settings_main.setFrameShape(QFrame.NoFrame)
        self.frame_settings_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_settings_main)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_settings_top = QFrame(self.frame_settings_main)
        self.frame_settings_top.setObjectName(u"frame_settings_top")
        self.frame_settings_top.setFrameShape(QFrame.NoFrame)
        self.frame_settings_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_settings_top)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_for_settings_widget = QFrame(self.frame_settings_top)
        self.frame_for_settings_widget.setObjectName(u"frame_for_settings_widget")
        self.frame_for_settings_widget.setMinimumSize(QSize(0, 300))
        self.frame_for_settings_widget.setFrameShape(QFrame.StyledPanel)
        self.frame_for_settings_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_for_settings_widget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_3 = QFrame(self.frame_for_settings_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.choose_you_theme_label = QLabel(self.frame_3)
        self.choose_you_theme_label.setObjectName(u"choose_you_theme_label")
        font6 = QFont()
        font6.setFamily(u"Product Sans")
        font6.setPointSize(24)
        self.choose_you_theme_label.setFont(font6)
        self.choose_you_theme_label.setStyleSheet(u"")
        self.choose_you_theme_label.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.choose_you_theme_label)


        self.verticalLayout_18.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_for_settings_widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame_4)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 20, 241, 51))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.night_mode_label = QLabel(self.layoutWidget1)
        self.night_mode_label.setObjectName(u"night_mode_label")
        self.night_mode_label.setFont(font1)
        self.night_mode_label.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.night_mode_label)

        self.dark_mode_onoff_button = QPushButton(self.layoutWidget1)
        self.dark_mode_onoff_button.setObjectName(u"dark_mode_onoff_button")
        self.dark_mode_onoff_button.setMaximumSize(QSize(80, 30))
        self.dark_mode_onoff_button.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/toggle_off/icons/white/toggle_off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dark_mode_onoff_button.setIcon(icon7)
        self.dark_mode_onoff_button.setIconSize(QSize(80, 30))

        self.horizontalLayout_13.addWidget(self.dark_mode_onoff_button)

        self.layoutWidget2 = QWidget(self.frame_4)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(80, 80, 321, 61))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.default_radio_button = QRadioButton(self.layoutWidget2)
        self.default_radio_button.setObjectName(u"default_radio_button")
        self.default_radio_button.setFont(font)
        self.default_radio_button.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.default_radio_button)

        self.green_radio_button = QRadioButton(self.layoutWidget2)
        self.green_radio_button.setObjectName(u"green_radio_button")
        self.green_radio_button.setFont(font)
        self.green_radio_button.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.green_radio_button)

        self.pink_radio_button = QRadioButton(self.layoutWidget2)
        self.pink_radio_button.setObjectName(u"pink_radio_button")
        self.pink_radio_button.setFont(font)
        self.pink_radio_button.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.pink_radio_button)


        self.verticalLayout_18.addWidget(self.frame_4)


        self.horizontalLayout_11.addWidget(self.frame_for_settings_widget)

        self.frame_for_gear_icon = QFrame(self.frame_settings_top)
        self.frame_for_gear_icon.setObjectName(u"frame_for_gear_icon")
        self.frame_for_gear_icon.setMaximumSize(QSize(300, 16777215))
        self.frame_for_gear_icon.setFrameShape(QFrame.StyledPanel)
        self.frame_for_gear_icon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_for_gear_icon)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_for_gear_icon = QLabel(self.frame_for_gear_icon)
        self.label_for_gear_icon.setObjectName(u"label_for_gear_icon")
        self.label_for_gear_icon.setPixmap(QPixmap(u":/gear_icon/icons/white/settings_gear.png"))

        self.verticalLayout_17.addWidget(self.label_for_gear_icon)


        self.horizontalLayout_11.addWidget(self.frame_for_gear_icon)


        self.verticalLayout_16.addWidget(self.frame_settings_top)

        self.frame_settings_bottom = QFrame(self.frame_settings_main)
        self.frame_settings_bottom.setObjectName(u"frame_settings_bottom")
        self.frame_settings_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_bottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_settings_bottom)


        self.verticalLayout_15.addWidget(self.frame_settings_main)

        self.pages.addWidget(self.page_settings)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.verticalLayout_20 = QVBoxLayout(self.page_about)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_about_main = QFrame(self.page_about)
        self.frame_about_main.setObjectName(u"frame_about_main")
        self.frame_about_main.setStyleSheet(u"")
        self.frame_about_main.setFrameShape(QFrame.StyledPanel)
        self.frame_about_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_about_main)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_about_main_bottom = QFrame(self.frame_about_main)
        self.frame_about_main_bottom.setObjectName(u"frame_about_main_bottom")
        self.frame_about_main_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_about_main_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_about_main_bottom)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_about_main_left = QFrame(self.frame_about_main_bottom)
        self.frame_about_main_left.setObjectName(u"frame_about_main_left")
        self.frame_about_main_left.setMinimumSize(QSize(250, 0))
        self.frame_about_main_left.setMaximumSize(QSize(250, 300))
        self.frame_about_main_left.setFrameShape(QFrame.NoFrame)
        self.frame_about_main_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_about_main_left)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_for_logo = QLabel(self.frame_about_main_left)
        self.label_for_logo.setObjectName(u"label_for_logo")
        self.label_for_logo.setPixmap(QPixmap(u":/icon/icons/icon.png"))
        self.label_for_logo.setScaledContents(True)

        self.verticalLayout_22.addWidget(self.label_for_logo)


        self.horizontalLayout_14.addWidget(self.frame_about_main_left)

        self.frame_about_main_right = QFrame(self.frame_about_main_bottom)
        self.frame_about_main_right.setObjectName(u"frame_about_main_right")
        self.frame_about_main_right.setFrameShape(QFrame.StyledPanel)
        self.frame_about_main_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_about_main_right)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_for_info_label = QFrame(self.frame_about_main_right)
        self.frame_for_info_label.setObjectName(u"frame_for_info_label")
        self.frame_for_info_label.setMinimumSize(QSize(500, 0))
        self.frame_for_info_label.setFrameShape(QFrame.StyledPanel)
        self.frame_for_info_label.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_for_info_label)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_info = QLabel(self.frame_for_info_label)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setMinimumSize(QSize(250, 0))
        font7 = QFont()
        font7.setFamily(u"Product Sans")
        font7.setPointSize(16)
        self.label_info.setFont(font7)
        self.label_info.setStyleSheet(u"")
        self.label_info.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.label_info)


        self.verticalLayout_23.addWidget(self.frame_for_info_label)

        self.frame_for_info_extra_links = QFrame(self.frame_about_main_right)
        self.frame_for_info_extra_links.setObjectName(u"frame_for_info_extra_links")
        self.frame_for_info_extra_links.setFrameShape(QFrame.StyledPanel)
        self.frame_for_info_extra_links.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_for_info_extra_links)
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_4 = QSpacerItem(296, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)

        self.youtube_button = QPushButton(self.frame_for_info_extra_links)
        self.youtube_button.setObjectName(u"youtube_button")
        self.youtube_button.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"\n"
"\n"
"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/youtube_icon/icons/black/youtube_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.youtube_button.setIcon(icon8)
        self.youtube_button.setIconSize(QSize(64, 64))

        self.horizontalLayout_15.addWidget(self.youtube_button)

        self.telegram_button = QPushButton(self.frame_for_info_extra_links)
        self.telegram_button.setObjectName(u"telegram_button")
        self.telegram_button.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"\n"
"\n"
"\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/telegram/icons/white/telegram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.telegram_button.setIcon(icon9)
        self.telegram_button.setIconSize(QSize(64, 64))

        self.horizontalLayout_15.addWidget(self.telegram_button)

        self.github_button = QPushButton(self.frame_for_info_extra_links)
        self.github_button.setObjectName(u"github_button")
        self.github_button.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"\n"
"\n"
"\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/github/icons/white/github_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.github_button.setIcon(icon10)
        self.github_button.setIconSize(QSize(64, 64))

        self.horizontalLayout_15.addWidget(self.github_button)

        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)


        self.verticalLayout_23.addWidget(self.frame_for_info_extra_links)


        self.horizontalLayout_14.addWidget(self.frame_about_main_right)


        self.verticalLayout_21.addWidget(self.frame_about_main_bottom)

        self.frame_about_main_top = QFrame(self.frame_about_main)
        self.frame_about_main_top.setObjectName(u"frame_about_main_top")
        self.frame_about_main_top.setFrameShape(QFrame.NoFrame)
        self.frame_about_main_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_about_main_top)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_6 = QSpacerItem(750, 126, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer)

        self.version_label = QLabel(self.frame_about_main_top)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setMinimumSize(QSize(250, 0))
        self.version_label.setMaximumSize(QSize(150, 16777215))
        self.version_label.setFont(font1)

        self.verticalLayout_26.addWidget(self.version_label)


        self.horizontalLayout_16.addLayout(self.verticalLayout_26)


        self.verticalLayout_21.addWidget(self.frame_about_main_top, 0, Qt.AlignBottom)


        self.verticalLayout_20.addWidget(self.frame_about_main)

        self.pages.addWidget(self.page_about)

        self.verticalLayout_6.addWidget(self.pages)


        self.horizontalLayout.addWidget(self.frame_mian_right)


        self.verticalLayout_2.addWidget(self.frame_main)


        self.verticalLayout.addWidget(self.frame_base)

        YouDer.setCentralWidget(self.centralwidget)

        self.retranslateUi(YouDer)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(YouDer)
    # setupUi

    def retranslateUi(self, YouDer):
        YouDer.setWindowTitle(QCoreApplication.translate("YouDer", u"MainWindow", None))
        self.thubnail_label.setText("")
        self.eye_icon_label.setText("")
        self.views.setText(QCoreApplication.translate("YouDer", u"125K", None))
        self.video_length_icon_label.setText("")
        self.length_label.setText(QCoreApplication.translate("YouDer", u"00:00:00", None))
        self.title_label.setText(QCoreApplication.translate("YouDer", u"You Der is Free Open Sourced Youtube video downloader by Open utilites.....", None))
        self.combobox.setItemText(0, QCoreApplication.translate("YouDer", u"1080p Video- 45 Mb", None))
        self.combobox.setItemText(1, QCoreApplication.translate("YouDer", u" 720p Video- 33 Mb", None))
        self.combobox.setItemText(2, QCoreApplication.translate("YouDer", u"480p Video- 24 Mb", None))

        self.status_bar.setText(QCoreApplication.translate("YouDer", u"Progress :", None))
        self.save_as_label.setText(QCoreApplication.translate("YouDer", u"Save as", None))
        self.toolButton.setText(QCoreApplication.translate("YouDer", u"...", None))
        self.choose_you_theme_label.setText(QCoreApplication.translate("YouDer", u"Choose your Theme . . . ", None))
        self.night_mode_label.setText(QCoreApplication.translate("YouDer", u"Night Mode ", None))
        self.dark_mode_onoff_button.setText("")
        self.default_radio_button.setText(QCoreApplication.translate("YouDer", u"Default", None))
        self.green_radio_button.setText(QCoreApplication.translate("YouDer", u"Green", None))
        self.pink_radio_button.setText(QCoreApplication.translate("YouDer", u"Pink", None))
        self.label_for_gear_icon.setText("")
        self.label_for_logo.setText("")
        self.label_info.setText(QCoreApplication.translate("YouDer", u"<html><head/><body><p><span style=\" font-weight:600;\">YouDer</span> is Free ,Open Sourced Youtube Video Downloader.YouDer is build on <span style=\" font-weight:600;\">Qt,Pytube</span> and <span style=\" font-weight:600;\">Python.</span>YouDer is a product of <span style=\" font-weight:600;\">OpenUtilites</span>.</p></body></html>", None))
        self.youtube_button.setText("")
        self.telegram_button.setText("")
        self.github_button.setText("")
        self.version_label.setText(QCoreApplication.translate("YouDer", u"YouDer Version 2.0", None))
    # retranslateUi

