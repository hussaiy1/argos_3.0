from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/776417294187757568/f0xqLpTY_ksAeuw8WU__AMtAROp21mBSAmAHzru66n0kbOvNWlpzHVQZ0V18Qou65iPB", username="Argos")


def send_hook(url)
    embed = DiscordEmbed(
        title="ARGOS", description="Product Avaialable", color=242424
    )
    embed.set_author(
        name="link",
        url=url,
    )
    #embed.set_footer(text="Embed Footer Text")
    #embed.set_timestamp()
    ## Set `inline=False` for the embed field to occupy the whole line
    #embed.add_embed_field(name="Field 1", value="Lorem ipsum", inline=False)
    #embed.add_embed_field(name="Field 2", value="dolor sit", inline=False)
    #embed.add_embed_field(name="Field 3", value="amet consetetur")
    #embed.add_embed_field(name="Field 4", value="sadipscing elitr")

    webhook.add_embed(embed)
    response = webhook.execute()