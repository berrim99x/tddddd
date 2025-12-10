class UserPresenter:
    def present(self, response):
        return {
            "success": response.success,
            "message": response.message,
            "user_id": response.user_id
        }
