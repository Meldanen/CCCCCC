class PermissionService:

    def __init__(self, bot_id, logging_service):
        self.bot_id = bot_id
        self.logging_service = logging_service

    def is_allowed_to_use_command(self, user_id, command, special_permissions):
        return True
