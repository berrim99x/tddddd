from src.application.viewmodels.create_user_viewmodel import CreateUserViewModel

class UserPresenter:
    def present(self, response):
        return CreateUserViewModel(
            success=response.success,
            message=response.message,
            user_id=response.user_id
        )
