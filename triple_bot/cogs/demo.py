from interactions import Client, CommandContext, Extension, extension_command as command


class DemoExtension(Extension):
    @command(name="dash")
    async def dash(self, ctx: CommandContext):
        await ctx.send("Hello from the __bot__.")

def setup(client: Client):
    DemoExtension(client)
