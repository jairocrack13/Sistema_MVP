from PySide6.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.main_view import MainView
from ui.student_view import StudentView
from ui.teacher_view import TeacherView
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter

class AppShell(QStackedWidget):
    PAGE_LOGIN = 0
    PAGE_ADMIN = 1
    PAGE_STUDENT = 2
    PAGE_TEACHER = 3

    def __init__(self):
        super().__init__()

        # 1. Instanciar Vistas
        self.login_view = LoginView()
        self.admin_view = MainView()
        self.student_view = StudentView()
        self.teacher_view = TeacherView()

        # 2. Instanciar Servicio
        self.auth_service = AuthService()

        # 3. Instanciar Presentador
        self.login_presenter = LoginPresenter(
            view=self.login_view,
            auth=self.auth_service,
            on_success=self._navigate_by_role
        )

        # 4. Registrar páginas en el Stack
        self.addWidget(self.login_view)   # 0
        self.addWidget(self.admin_view)   # 1
        self.addWidget(self.student_view) # 2
        self.addWidget(self.teacher_view) # 3

        self.setCurrentIndex(self.PAGE_LOGIN)
        self.setWindowTitle("Sistema Educativo MVP")
        self.resize(600, 400)

    def _navigate_by_role(self, role: str):
        if role == "admin":
            self.admin_view.set_welcome("Admin")
            self.setCurrentIndex(self.PAGE_ADMIN)
        elif role == "estudiante":
            self.setCurrentIndex(self.PAGE_STUDENT)
        elif role == "maestro":
            self.setCurrentIndex(self.PAGE_TEACHER)
