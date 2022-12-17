from interactions import Button, ButtonStyle, Client, CommandContext, Extension, \
    extension_command as command, extension_component as component

boom_button = Button(
    style = ButtonStyle.DANGER,
    label = "Boom.",
    custom_id = "boom"
)

class DigiExtension(Extension):
    @command(name="explode")
    async def explode(self, ctx: CommandContext):
        await ctx.send("...", components = boom_button)

    @component("boom")
    async def explode_response(self, ctx: CommandContext):
        await ctx.message.disable_all_components()
        await ctx.send("Boom! 💥")


def setup(client: Client):
    DigiExtension(client)