from errbot import BotPlugin, botcmd
from pyfiglet import Figlet

class AsciiArt(BotPlugin):
    """ Ascii Art related commands. """

    @botcmd
    def big(self, mess, args):
        """ Generates a big version of what you want to say."""
        return "```\n" + Figlet(font='slant').renderText(args) + "\n```"

