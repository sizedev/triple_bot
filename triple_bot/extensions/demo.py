from typing import cast
from interactions import Client, CommandContext, Extension, Message, extension_command as command, extension_message_command as message_command


class DemoExtension(Extension):
    @command(name="dash")
    async def dash(self, ctx: CommandContext):
        await ctx.send("Hello from the __bot__.")
    
    @message_command(name="Praise")
    async def praise(self, ctx: CommandContext):
        message = cast(Message, ctx.target)
        await ctx.send(f"{message.author.username} makes a good point in {len(message.content)} characters!")

def setup(client: Client):
    DemoExtension(client)
