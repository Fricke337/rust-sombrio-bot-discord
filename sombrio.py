import discord
from discord.ext import commands
from discord.ui import Button, View

# --- CONFIGURATION ---
TOKEN = 'SE_FOREM_USAR_MEU_PROJETO_COLOQUEM_O_TOKEN_AQUI'

class TicketView(View):
    def __init__(self, category_type):
        super().__init__(timeout=None)
        self.category_type = category_type

    @discord.ui.button(label="Abrir Chamado", style=discord.ButtonStyle.green, emoji="🎟️", custom_id="ticket_view:open")
    async def open_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        
        channel_name = f"{self.category_type}-{user.name}"
        channel = await guild.create_text_channel(channel_name, overwrites=overwrites)
        
        await interaction.response.send_message(f"Chamado aberto em {channel.mention}", ephemeral=True)
        
        content = (
            f"🛡️ **CENTRAL DE DENÚNCIAS**\n{user.mention}, anexe evidências para análise."
            if self.category_type == "denuncia" else
            f"🎟️ **SUPORTE / VIP**\n{user.mention}, informe sua dúvida ou interesse."
        )
        await channel.send(content)

class SombrioBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        self.add_view(TicketView("ticket"))
        self.add_view(TicketView("denuncia"))
        print(f'System Online: {self.user}')

bot = SombrioBot()

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_ticket(ctx):
    embed = discord.Embed(
        title="🎟️ SUPORTE E VIP",
        description="Clique no botão abaixo para iniciar um atendimento privado.",
        color=0x2ecc71
    )
    await ctx.send(embed=embed, view=TicketView("ticket"))

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_denuncia(ctx):
    embed = discord.Embed(
        title="🚫 CENTRAL DE DENÚNCIAS",
        description="Clique no botão abaixo para reportar irregularidades.",
        color=0xff0000
    )
    await ctx.send(embed=embed, view=TicketView("denuncia"))

@bot.command()
@commands.has_permissions(administrator=True)
async def regras(ctx):
    embed = discord.Embed(
        title="🔗 DIRETRIZES DO SERVIDOR",
        description="Normas obrigatórias para a convivência e gameplay.",
        color=0x3498db
    )
    embed.add_field(name="Limite de Grupo", value="Máximo de 3 membros (Trio).", inline=False)
    embed.add_field(name="Fair Play", value="Proibido alianças e comportamentos tóxicos.", inline=False)
    embed.set_footer(text="A administração reserva-se o direito de punição imediata.")
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run(TOKEN)