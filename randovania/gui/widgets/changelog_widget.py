from __future__ import annotations

from PySide6 import QtCore, QtWidgets

from randovania.gui.widgets.delayed_text_label import DelayedTextLabel


class ChangeLogWidget(QtWidgets.QWidget):
    def __init__(self, all_change_logs: dict[str, str], all_change_log_publish_dates: dict[str, str]):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.select_version = QtWidgets.QComboBox(self)
        self.select_version.currentIndexChanged.connect(lambda: self.select_version_index_changed())

        layout.addWidget(self.select_version)

        self.changelog = QtWidgets.QStackedWidget(self)
        layout.addWidget(self.changelog)

        for version_name, version_text in all_change_logs.items():
            body = f"{all_change_log_publish_dates[version_name]}\n\n{version_text}"

            scroll_area = QtWidgets.QScrollArea()
            scroll_area.setObjectName(f"scroll_area {version_name}")
            scroll_area.setWidgetResizable(True)

            label = DelayedTextLabel()
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            label.setObjectName(f"label {version_name}")
            label.setOpenExternalLinks(True)
            label.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
            label.setText(body)
            label.setWordWrap(True)

            scroll_area.setWidget(label)
            self.changelog.addWidget(scroll_area)

            self.select_version.addItem(version_name)

        self.changelog.setCurrentIndex(0)

    def select_version_index_changed(self):
        selected_widget: QtWidgets.QScrollArea = self.findChild(
            QtWidgets.QScrollArea, f"scroll_area {self.select_version.currentText()}"
        )

        self.changelog.setCurrentWidget(selected_widget)
