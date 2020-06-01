import os

DEFAULT_STATIC_FOLDER = os.path.join(__path__[0], 'static')
CUSTOM_STATIC_FOLDERS = []
from dayu_widgets.theme import MTheme

dayu_theme = MTheme('dark', primary_color=MTheme.blue)
dayu_theme.default_size = dayu_theme.small
dayu_theme = MTheme('light')

from dayu_widgets.spin_box import MSpinBox, MDoubleSpinBox, MDateTimeEdit, MDateEdit, MTimeEdit
from dayu_widgets.alert import MAlert
from dayu_widgets.avatar import MAvatar
from dayu_widgets.badge import MBadge
from dayu_widgets.breadcrumb import MBreadcrumb
from dayu_widgets.browser import MClickBrowserFilePushButton, MClickBrowserFileToolButton, \
    MClickBrowserFolderPushButton, MClickBrowserFolderToolButton, \
    MDragFileButton, MDragFolderButton
from dayu_widgets.button_group import MPushButtonGroup, MRadioButtonGroup, MCheckBoxGroup, MToolButtonGroup
from dayu_widgets.card import MCard, MMeta
from dayu_widgets.carousel import MCarousel
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.collapse import MCollapse
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.flow_layout import MFlowLayout
from dayu_widgets.item_model import MTableModel, MSortFilterModel
from dayu_widgets.item_view import MTableView, MTreeView, MBigView, MListView
from dayu_widgets.item_view_full_set import MItemViewFullSet
from dayu_widgets.item_view_set import MItemViewSet
from dayu_widgets.label import MLabel
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.line_tab_widget import MLineTabWidget
from dayu_widgets.loading import MLoading, MLoadingWrapper
from dayu_widgets.menu import MMenu
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from dayu_widgets.message import MMessage
from dayu_widgets.page import MPage
from dayu_widgets.progress_bar import MProgressBar
from dayu_widgets.push_button import MPushButton
from dayu_widgets.radio_button import MRadioButton
from dayu_widgets.sequence_file import MSequenceFile
from dayu_widgets.slider import MSlider
from dayu_widgets.switch import MSwitch
from dayu_widgets.tab_widget import MTabWidget
from dayu_widgets.toast import MToast
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.text_edit import MTextEdit