#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2018.5
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import dayu_theme
from dayu_widgets.MButtonGroup import MToolButtonGroup
from dayu_widgets.MItemModel import MSortFilterModel, MTableModel
from dayu_widgets.MItemView import MTableView, MBigView
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.MPage import MPage
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.qt import *


class MItemViewFullSet(QWidget):
    sig_double_clicked = Signal(QModelIndex)
    sig_left_clicked = Signal(QModelIndex)
    sig_current_changed = Signal(QModelIndex, QModelIndex)
    sig_current_row_changed = Signal(QModelIndex, QModelIndex)
    sig_current_column_changed = Signal(QModelIndex, QModelIndex)
    sig_selection_changed = Signal(QItemSelection, QItemSelection)
    sig_context_menu = Signal(object)

    def __init__(self, table_view=True, big_view=False, parent=None):
        super(MItemViewFullSet, self).__init__(parent)
        self.sort_filter_model = MSortFilterModel()
        self.source_model = MTableModel()
        self.sort_filter_model.setSourceModel(self.source_model)

        self.stack_widget = QStackedWidget()

        self.view_button_grp = MToolButtonGroup(type=MToolButton.IconOnlyType, exclusive=True)
        data_group = []
        if table_view:
            self.table_view = MTableView(show_row_count=True)
            self.table_view.doubleClicked.connect(self.sig_double_clicked)
            self.table_view.pressed.connect(self.slot_left_clicked)
            self.table_view.setModel(self.sort_filter_model)
            self.stack_widget.addWidget(self.table_view)
            data_group.append({'icon': MIcon('table_view.svg'),
                               'icon_checked': MIcon('table_view.svg', dayu_theme.color.get('primary')),
                               'checkable': True,
                               'tooltip': u'Table View'})
        if big_view:
            self.big_view = MBigView()
            self.big_view.doubleClicked.connect(self.sig_double_clicked)
            self.big_view.pressed.connect(self.slot_left_clicked)
            self.big_view.setModel(self.sort_filter_model)
            self.stack_widget.addWidget(self.big_view)
            data_group.append({'icon': MIcon('big_view.svg'),
                               'icon_checked': MIcon('big_view.svg', dayu_theme.color.get('primary')),
                               'checkable': True,
                               'tooltip': u'Big View'})

        # 设置多个view 共享 MItemSelectionModel
        leader_view = self.stack_widget.widget(0)
        self.selection_model = leader_view.selectionModel()
        for index in range(self.stack_widget.count()):
            if index == 0:
                continue
            other_view = self.stack_widget.widget(index)
            other_view.setSelectionModel(self.selection_model)

        self.selection_model.currentChanged.connect(self.sig_current_changed)
        self.selection_model.currentRowChanged.connect(self.sig_current_row_changed)
        self.selection_model.currentColumnChanged.connect(self.sig_current_column_changed)
        self.selection_model.selectionChanged.connect(self.sig_selection_changed)

        self.tool_bar = QWidget()
        self.top_lay = QHBoxLayout()
        self.top_lay.setContentsMargins(0, 0, 0, 0)
        if data_group and len(data_group) > 1:
            self.view_button_grp.sig_checked_changed.connect(self.stack_widget.setCurrentIndex)
            self.view_button_grp.set_button_list(data_group)
            self.view_button_grp.set_checked(0)
            self.top_lay.addWidget(self.view_button_grp)
        search_size = dayu_theme.size.small
        self.search_line_edit = MLineEdit.search(size=search_size)
        self.search_attr_button = MToolButton(type=MToolButton.IconOnlyType, icon=MIcon('down_fill.svg'),
                                              size=search_size)
        self.search_line_edit.add_prefix_widget(self.search_attr_button)
        self.search_line_edit.textChanged.connect(self.sort_filter_model.set_search_pattern)

        self.top_lay.addStretch()
        self.top_lay.addWidget(self.search_line_edit)
        self.tool_bar.setLayout(self.top_lay)

        self.page_set = MPage()
        self.main_lay = QVBoxLayout()
        self.main_lay.setSpacing(5)
        self.main_lay.setContentsMargins(0, 0, 0, 0)
        self.main_lay.addWidget(self.tool_bar)
        self.main_lay.addWidget(self.stack_widget)
        self.main_lay.addWidget(self.page_set)
        self.setLayout(self.main_lay)

    def enable_context_menu(self):
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.enable_context_menu(True)
            view.sig_context_menu.connect(self.sig_context_menu)

    def set_no_data_text(self, text):
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.set_no_data_text(text)

    def set_selection_mode(self, mode):
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.setSelectionMode(mode)

    def tool_bar_visible(self, flag):
        self.tool_bar.setVisible(flag)

    @Slot(QModelIndex)
    def slot_left_clicked(self, start_index):
        button = QApplication.mouseButtons()
        if button == Qt.LeftButton:
            real_index = self.sort_filter_model.mapToSource(start_index)
            self.sig_left_clicked.emit(real_index)

    def set_header_list(self, header_list):
        self.source_model.set_header_list(header_list)
        self.sort_filter_model.set_header_list(header_list)
        self.sort_filter_model.setSourceModel(self.source_model)
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.set_header_list(header_list)

    def tool_bar_append_widget(self, widget):
        self.top_lay.addWidget(widget)

    def tool_bar_insert_widget(self, widget):
        self.top_lay.insertWidget(0, widget)

    @Slot()
    def setup_data(self, data_list):
        self.source_model.clear()
        if data_list:
            self.source_model.set_data_list(data_list)
        self.set_record_count(len(data_list))

    @Slot(int)
    def set_record_count(self, total):
        self.page_set.set_total(total)

    def get_data(self):
        return self.source_model.get_data_list()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MItemViewFullSet()
    dayu_theme.apply(test)
    test.set_header_list(
        [{'label': 'Name', 'key': 'name', 'editable': True, 'selectable': True, 'exclusive': False, 'width': 200,
          }])
    # only_work_check_box = QCheckBox('Show Special Tasks')
    # only_work_check_box.setChecked(False)
    # only_work_check_box.stateChanged.connect(test.slot_update)
    # test.add_button(only_work_check_box)
    test.setup_data([{'name': ['xiaoming'], 'name_list': ['li', 'haha', 'xiaoming']}])
    test.show()
    sys.exit(app.exec_())
