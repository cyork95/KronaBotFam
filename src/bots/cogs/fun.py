import asyncio
import random
import discord
from discord.ext import commands
import re

ball_response = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]
fav_quotes = [
    "\"The greatest glory in living lies not in never falling, but in rising every time we fall.\" -Nelson Mandela",
    "\"The way to get started is to quit talking and begin doing.\" -Walt Disney",
    "\"Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is "
    "living with the results of other people's thinking.\" -Steve Jobs",
    "\"If life were predictable it would cease to be life, and be without flavor.\" -Eleanor Roosevelt",
    "\"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, "
    "you'll never have enough.\" -Oprah Winfrey",
    "\"If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.\" "
    "-James Cameron",
    "\"Life is what happens when you're busy making other plans.\" -John Lennon"
    "\"Spread love everywhere you go. Let no one ever come to you without leaving happier.\" -Mother Teresa",
    "\"When you reach the end of your rope, tie a knot in it and hang on.\" -Franklin D. Roosevelt",
    "\"Always remember that you are absolutely unique. Just like everyone else.\" -Margaret Mead",
    "\"Don't judge each day by the harvest you reap but by the seeds that you plant.\" -Robert Louis Stevenson",
    "\"The future belongs to those who believe in the beauty of their dreams.\" -Eleanor Roosevelt",
    "\"Tell me and I forget. Teach me and I remember. Involve me and I learn.\" -Benjamin Franklin",
    "\"The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the "
    "heart.\" -Helen Keller",
    "\"It is during our darkest moments that we must focus to see the light.\" -Aristotle",
    "\"Whoever is happy will make others happy too.\" -Anne Frank",
    "\"Do not go where the path may lead, go instead where there is no path and leave a trail.\" -Ralph Waldo Emerson",
    "\"You will face many defeats in life, but never let yourself be defeated.\" -Maya Angelou",
    "\"The greatest glory in living lies not in never falling, but in rising every time we fall.\" -Nelson Mandela",
    "\"In the end, it's not the years in your life that count. It's the life in your years.\" -Abraham Lincoln",
    "\"Never let the fear of striking out keep you from playing the game.\" -Babe Ruth",
    "\"Life is either a daring adventure or nothing at all.\" -Helen Keller",
    "\"Many of life's failures are people who did not realize how close they were to success when they gave up.\" "
    "-Thomas A. Edison",
    "\"You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.\" "
    "-Dr. Seuss",
    "\"Success is not final; failure is not fatal: It is the courage to continue that counts.\" -Winston S. Churchill",
    "\"Success usually comes to those who are too busy to be looking for it.\" -Henry David Thoreau",
    "\"If you really look closely, most overnight successes took a long time.\" -Steve Jobs",
    "\"The secret of success is to do the common thing uncommonly well.\" -John D. Rockefeller Jr.",
    "\"I find that the harder I work, the more luck I seem to have.\" -Thomas Jefferson",
    "\"The real test is not whether you avoid this failure, because you won't. It's whether you let it harden or shame "
    "you into inaction, or whether you learn from it; whether you choose to persevere.\" -Barack Obama",
    "\"You miss 100% of the shots you don't take.\" -Wayne Gretzky",
    "\"Whether you think you can or you think you can't, you're right.\" -Henry Ford",
    "\"I have learned over the years that when one's mind is made up, this diminishes fear.\" -Rosa Parks",
    "\"I alone cannot change the world, but I can cast a stone across the water to create many ripples.\" "
    "-Mother Teresa",
    "\"Nothing is impossible, the word itself says, ‘I'm possible!'\" -Audrey Hepburn",
    "\"The question isn't who is going to let me; it's who is going to stop me.\" -Ayn Rand",
    "\"The only person you are destined to become is the person you decide to be.\" -Ralph Waldo Emerson"
]


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def dice(self, ctx, *, msg="1"):
        """Roll dice. Optionally input # of dice and # of sides. Ex: [p]dice 5 12"""
        await ctx.message.delete()
        invalid = 'Invalid syntax. Ex: `>dice 4` - roll four normal dice. `>dice 4 12` - roll four 12 sided dice.'
        dice_rolls = []
        dice_roll_ints = []
        try:
            dice, sides = re.split("[d\s]", msg)
        except ValueError:
            dice = msg
            sides = "6"
        try:
            for roll in range(int(dice)):
                result = random.randint(1, int(sides))
                dice_rolls.append(str(result))
                dice_roll_ints.append(result)
        except ValueError:
            return await ctx.send(self.client.bot_prefix + invalid)
        embed = discord.Embed(title="Dice rolls:", description=' '.join(dice_rolls))
        embed.add_field(name="Total:", value=sum(dice_roll_ints))
        await ctx.send("", embed=embed)

    @dice.error
    async def dice_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you give the number of dice and then the number of sides?')
        await ctx.send(embed=embed)

    @commands.command(aliases=['8ball'])
    async def eight_ball(self, ctx, *, question):
        await ctx.message.delete()
        await ctx.send(f'Question:    {question}\nAnswer:    {random.choice(ball_response)}')

    @eight_ball.error
    async def eight_ball_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you give it a question?')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['pick'])
    async def choose(self, ctx, *, choices: str):
        """Choose randomly from the options you give. [p]choose this | that"""
        await ctx.message.delete()
        await ctx.send('I choose: ``{}``'.format(random.choice(choices.split(","))))

    @choose.error
    async def choose_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you make sure to have only a \",\" separating the choices?')
        await ctx.send(embed=embed)

    @commands.command()
    async def flip_coin(self, ctx):
        """Flip a coin!"""
        await ctx.message.delete()
        await ctx.send('*Flipping...*')
        await asyncio.sleep(3)
        await ctx.send(content=random.choice(('Heads!', 'Tails!')))

    @flip_coin.error
    async def flip_coin_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add any extra parameters?')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
