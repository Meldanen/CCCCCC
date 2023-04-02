from services.LoggingService import LoggingService
from services.PermissionsService import PermissionService
from discord.ext import commands


class CCCCCCBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.logging_service = LoggingService()
        self.get_gnomed_bad_luck_protection = 0

    @commands.Cog.listener()
    async def on_ready(self):
        self.permission_service = PermissionService(self.bot.user.id, self.logging_service)
        self.logging_service.info(f'{self.bot.user.name} is here to please the Green Cone!')